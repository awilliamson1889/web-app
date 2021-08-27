"""Rest location Api"""
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, abort
from pydantic import ValidationError

from department_app.service import CRUDLocation
from department_app.schemas import LocationSchema

location_api = Blueprint('location_api', __name__)

api = Api(location_api)


class Location(Resource):
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
        location = CRUDLocation.get(location_id)
        if not location:
            return abort(404, message=f"No such location with ID={location_id}")
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
        location_json = request.json

        try:
            valid_location_json = LocationSchema(**location_json).dict(exclude_unset=True)
            result = CRUDLocation.update(location_id, **valid_location_json)
        except IntegrityError as exception:
            return abort(404, message=f"{exception}")
        except ValidationError as exception:
            return abort(404, message=f"{exception}")
        if not result:
            return abort(404, message="Location not updated.")
        return make_response(jsonify({'message': 'Data successful updated.'}), 201)


class LocationList(Resource):
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
        location_json = request.json

        try:
            valid_location_json = LocationSchema(**location_json).dict(exclude_unset=True)
            location = CRUDLocation.create(**valid_location_json)
        except IntegrityError as exception:
            return abort(404, message=f"{exception}")
        except ValidationError as exception:
            return abort(404, message=f"{exception}")
        return make_response(jsonify(location), 201)

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
        locations = CRUDLocation.get_location_list()
        return make_response(jsonify(locations), 200)


api.add_resource(LocationList, '/api/location')
api.add_resource(Location, '/api/location/<string:location_id>')
