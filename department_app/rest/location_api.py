"""rest api"""
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api, abort
from department_app.models.app_models import Location
from department_app.models.location_schema import LocationModel
from department_app.models.app_models import db
from pydantic import ValidationError

location_api = Blueprint('location_api', __name__)

api = Api(location_api)


class LocationInfo(Resource):
    def get(self, location_id):
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
            abort(404, message=f"ID must be a number.")
        location = Location.query.filter_by(id=location_id).first()
        if not location:
            abort(404, message=f"Could not find location with ID: {location_id}.")
        return make_response(jsonify(location), 200)

    def put(self, location_id):
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
            abort(404, message=f"ID must be a number.")
        location = Location.query.filter_by(id=location_id).first()
        if not location:
            abort(404, message=f"Could not find location with ID: {location_id}.")

        if 'name' in request.json:
            location.name = request.json['name']
        try:
            result = LocationModel(id=location.id, name=location.name)
        except ValidationError as e:
            abort(404, message=f"Exception: {e}")

        db.session.commit()
        return result.dict(), 204


class AllLocationInfo(Resource):
    def post(self):
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
        e = Location.query.all()
        location_data = {'id': len(e)+100, 'name': request.json['name']}
        try:
            location = LocationModel(**location_data)
        except ValidationError as e:
            abort(404, message=f"Exception: {e}")

        result = Location(**location_data)

        db.session.add(result)
        db.session.commit()
        return location.dict(), 201

    def get(self):
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
        d = Location.query.all()
        return make_response(jsonify(d), 200)


api.add_resource(AllLocationInfo, '/api/location')
api.add_resource(LocationInfo, '/api/location/<string:location_id>')
