"""Rest location Api"""
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api, abort
from pydantic import ValidationError
from department_app.models.app_models import Location
from department_app.schemas.location_schema import LocationModel
from department_app.models.app_models import db


location_api = Blueprint('location_api', __name__)

api = Api(location_api)


class LocationInfo(Resource):
    """Location API class"""
    @staticmethod
    def get(location_id):
        """
        This is the location API
        Call this API passing a location_id and get back location information
        ---
        tags:
          - Location API
        parameters:
          - name: "location_id"
            in: "path"
            description: "ID of location to return"
            required: true
            type: "integer"
            format: "int64"
        responses:
          404:
            description: Could not find location
          200:
            description: Location information returned
        """
        if not str(location_id).isdigit():
            abort(404, message="ID must be a number.")
        location = Location.query.filter_by(id=location_id).first()
        if not location:
            abort(404, message=f"Could not find location with ID: {location_id}.")
        return make_response(jsonify(location), 200)

    @staticmethod
    def put(location_id):
        """
        This is the location API
        Call this API passing a location data and get back updated location information
        ---
        tags:
          - Location API
        parameters:
          - name: "location_id"
            in: "path"
            description: "ID of location to return"
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
                  example : "Brest, Belarus"
        responses:
          404:
            description: Could not find location
          204:
            description: Location information successful update
        """
        if not str(location_id).isdigit():
            abort(404, message="ID must be a number.")
        location = Location.query.filter_by(id=location_id).first()
        if not location:
            abort(404, message=f"Could not find location with ID: {location_id}.")

        location_data = {'name': location.name}

        location_json = request.json
        location_data.update(location_json)

        try:
            LocationModel(**location_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        location.name = location_data['name']

        db.session.commit()
        return make_response(jsonify(location), 201)


class AllLocationInfo(Resource):
    """Rest class"""
    @staticmethod
    def post():
        """
        This is the location API
        Call this api passing a location data and create new location
        ---
        tags:
          - Location API
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
                  example : "Minsk, Belarus"
        responses:
          201:
            description: The location was successfully created
        """
        location_data = {'name': request.json['name']}
        try:
            location = LocationModel(**location_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        result = Location(**location_data)

        db.session.add(result)
        db.session.commit()
        return location.dict(), 201

    @staticmethod
    def get():
        """
        This is the location API
        Call this API and get back all locations list
        ---
        tags:
          - Location API
        responses:
          200:
            description: All location returned
        """
        locations = Location.query.all()
        return make_response(jsonify(locations), 200)


api.add_resource(AllLocationInfo, '/api/location')
api.add_resource(LocationInfo, '/api/location/<string:location_id>')
