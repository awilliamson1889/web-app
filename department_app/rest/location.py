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
    def json_is_valid(json) -> bool:
        """Validate location json data, if json data not valid - return false"""
        try:
            LocationSchema(**json)
        except ValidationError:
            return False
        return True

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
        if str(location_id).isdigit() and int(location_id) > 0:
            location = CRUDLocation.get(location_id)
        else:
            return abort(404, message="Invalid ID format!")
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
        if not location_json:
            return abort(404, message="Wrong JSON fields names.")

        if not Location.json_is_valid(location_json):
            return abort(404, message="JSON is not valid.")
        try:
            result = CRUDLocation.update(location_id, **location_json)
        except IntegrityError as exception:
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
        if not location_json:
            return abort(404, message="Wrong JSON fields names.")

        if not Location.json_is_valid(location_json):
            return abort(404, message="JSON is not valid.")
        try:
            location = CRUDLocation.create(**location_json)
        except IntegrityError as exception:
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
