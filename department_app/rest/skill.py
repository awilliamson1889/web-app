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
        skill = CRUDSkill.get(skill_id)
        if not skill:
            return abort(404, message=f"No such skill with ID={skill_id}")
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
        skill_json = request.json

        try:
            valid_skill_json = SkillSchema(**skill_json).dict(exclude_unset=True)
            result = CRUDSkill.update(skill_id, **valid_skill_json)
        except IntegrityError as exception:
            return abort(404, message=f"Skill {exception}")
        except ValidationError as exception:
            return abort(404, message=f"Skill {exception}")
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
        skill_json = request.json

        try:
            valid_skill_json = SkillSchema(**skill_json).dict(exclude_unset=True)
            skill = CRUDSkill.create(**valid_skill_json)
        except IntegrityError as exception:
            return abort(404, message=f"Skill {exception}")
        except ValidationError as exception:
            return abort(404, message=f"Skill {exception}")
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
