"""Rest skill api"""
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api, abort
from pydantic import ValidationError
from department_app.schemas import SkillSchema
from department_app.service import CRUDSkill

skill_api = Blueprint('skill_api', __name__)

api = Api(skill_api)


class Skill(Resource):
    """Skill API class"""
    @staticmethod
    def get(skill_id):
        """
        This is the Skill API
        Call this API passing a skill_id and get back skill information
        ---
        tags:
          - Skill API
        parameters:
          - name: "skill_id"
            in: "path"
            description: "ID of skill to return"
            required: true
            type: "integer"
            format: "int64"
        responses:
          404:
            description: Could not find skill
          200:
            description: skill information returned
        """
        skill = CRUDSkill.get_skill(skill_id)
        return make_response(jsonify(skill), 200)

    @staticmethod
    def put(skill_id):
        """
        This is the Skill API
        Call this API passing a skill data and get back updated skill information
        ---
        tags:
          - Skill API
        parameters:
          - name: "skill_id"
            in: "path"
            description: "ID of skill to return"
            required: true
            type: "integer"
            format: "int64"
          - in: "body"
            name: "PUT body"
            description: "Accepts a input dictionary of inputs."
            required: true
            schema:
              type: "object"
              properties:
                name:
                  type: "string"
                  format: "string"
                  example : "Python"
        responses:
          404:
            description: Could not find skill
          204:
            description: Skill information successful update
        """
        skill = CRUDSkill.get_skill(skill_id)

        skill_data = {'name': skill.name}

        skill_json = request.json
        skill_data.update(skill_json)

        try:
            SkillSchema(**skill_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        CRUDSkill.update_skill(skill_id, skill_data)

        return make_response(jsonify(skill), 201)


class SkillList(Resource):
    """Rest class"""
    @staticmethod
    def post():
        """
        This is the Skill API
        Call this api passing a skill data and create new skill
        ---
        tags:
          - Skill API
        parameters:
          - in: "body"
            name: "POST body"
            description: "Accepts a input dictionary of inputs."
            required: true
            schema:
              type: "object"
              properties:
                name:
                  type: "string"
                  format: "string"
                  example : "Python"
        responses:
          201:
            description: The skill was successfully created
        """
        skill_data = {'name': request.json['name']}
        try:
            skill = SkillSchema(**skill_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        CRUDSkill.create_skill()

        return skill.dict(), 201

    @staticmethod
    def get():
        """
        This is the Skill API
        Call this API and get back all skills list
        ---
        tags:
          - Skill API
        responses:
          200:
            description: All skill returned
        """
        skills = CRUDSkill.get_all_skill()
        return make_response(jsonify(skills), 200)


api.add_resource(SkillList, '/api/skill')
api.add_resource(Skill, '/api/skill/<string:skill_id>')
