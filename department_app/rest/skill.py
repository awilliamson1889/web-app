"""Rest skill api"""
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, abort
from pydantic import ValidationError

from department_app.service import CRUDSkill
from department_app.schemas import SkillSchema

skill_api = Blueprint('skill_api', __name__)

api = Api(skill_api)


class Skill(Resource):
    """Skill API class"""
    @staticmethod
    def get_json():
        """Get address json, if json have wrong format - return abort """
        try:
            skill_json = {'name': request.json['name']}
        except KeyError:
            return False
        return skill_json

    @staticmethod
    def json_is_valid(json) -> bool:
        """Validate address json data, if json data not valid - return abort"""
        try:
            SkillSchema(**json)
        except ValidationError:
            return False
        return True

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
        if str(skill_id).isdigit() and int(skill_id) > 0:
            skill = CRUDSkill.get(skill_id)
        else:
            abort(404, message="Invalid ID format!")
        if not skill:
            abort(404, message=f"No such skill with ID={skill_id}")
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
        skill_json = Skill.get_json()
        if not skill_json:
            abort(404, message="Wrong JSON fields names.")

        if not Skill.json_is_valid(skill_json):
            abort(404, message="JSON is not valid.")
        try:
            result = CRUDSkill.update(skill_id, name=skill_json['name'])
        except IntegrityError as exception:
            abort(404, message=f"{exception}")
        if not result:
            return abort(404, message="Skill not updated.")
        return make_response(jsonify({'message': 'Data successful updated.'}), 201)


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
        skill_json = Skill.get_json()
        if not skill_json:
            abort(404, message="Wrong JSON fields names.")

        if not Skill.json_is_valid(skill_json):
            abort(404, message="JSON is not valid.")
        try:
            skill = CRUDSkill.create(**skill_json)
        except IntegrityError as exception:
            abort(404, message=f"{exception}")
        return make_response(jsonify(skill), 201)

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
        skills = CRUDSkill.get_skill_list()
        return make_response(jsonify(skills), 200)


api.add_resource(SkillList, '/api/skill')
api.add_resource(Skill, '/api/skill/<string:skill_id>')
