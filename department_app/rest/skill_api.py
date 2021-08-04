"""rest api"""
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api, abort
from pydantic import ValidationError
from department_app.models.app_models import Skill
from department_app.schemas.skill_schema import SkillModel
from department_app.models.app_models import db

skill_api = Blueprint('skill_api', __name__)

api = Api(skill_api)


class SkillInfo(Resource):
    """Rest class"""
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
        if not str(skill_id).isdigit():
            abort(404, message="ID must be a number.")
        skill = Skill.query.filter_by(id=skill_id).first()
        if not skill:
            abort(404, message=f"Could not find skill with ID: {skill_id}.")
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
        if not str(skill_id).isdigit():
            abort(404, message="ID must be a number.")
        skill = Skill.query.filter_by(id=skill_id).first()
        if not skill:
            abort(404, message=f"Could not find skill with ID: {skill_id}.")

        skill_data = {'name': skill.name}

        skill_json = request.json
        skill_data.update(skill_json)

        try:
            SkillModel(**skill_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        skill.name = skill_data['name']

        db.session.commit()
        return make_response(jsonify(skill), 201)


class AllSkillInfo(Resource):
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
            skill = SkillModel(**skill_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        result = Skill(**skill_data)

        db.session.add(result)
        db.session.commit()
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
        skills = Skill.query.all()
        return make_response(jsonify(skills), 200)


api.add_resource(AllSkillInfo, '/api/skill')
api.add_resource(SkillInfo, '/api/skill/<string:skill_id>')
