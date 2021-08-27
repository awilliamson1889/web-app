"""Rest addresses Api"""
from sqlalchemy.exc import IntegrityError
from flask import Blueprint, jsonify, make_response, request
from flask_restful import Resource, Api, abort
from pydantic import ValidationError

from department_app.service import CRUDAddress
from department_app.schemas import AddressSchema

address_api = Blueprint('address_api', __name__)

api = Api(address_api)


class Address(Resource):
    """Address API class"""
    @staticmethod
    def get(address_id):
        """
        This is the Address API
        Call this API passing a address_id and get back address information
        ---
        tags:
          - Address API
        parameters:
          - name: "address_id"
            in: "path"
            description: "ID of address to return"
            required: true
            type: "integer"
            format: "int64"
        responses:
          404:
            description: Could not find address
          200:
            description: Address information returned
        """
        address = CRUDAddress.get(address_id)
        if not address:
            return abort(404, message=f"No such address with ID={address_id}")
        return make_response(jsonify(address), 200)

    @staticmethod
    def put(address_id):
        """
        This is the Address API
        Call this API passing a address data and get back updated address information
        ---
        tags:
          - Address API
        parameters:
          - name: "address_id"
            in: "path"
            description: "ID of address to return"
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
                  example : "Moskovskaja, 384"
        responses:
          404:
            description: Could not find address
          204:
            description: Address information successful update
        """
        address_json = request.json

        try:
            valid_address_json = AddressSchema(**address_json).dict(exclude_unset=True)
            result = CRUDAddress.update(address_id, **valid_address_json)
        except IntegrityError as exception:
            return abort(404, message=f"{exception}")
        except ValidationError as exception:
            return abort(404, message=f"{exception}")

        if not result:
            return abort(404, message="Address not updated.")
        return make_response(jsonify({'message': 'Data successful updated.'}), 201)


class AddressList(Resource):
    """Address API"""
    @staticmethod
    def post():
        """
        This is the Address API
        Call this api passing a address data and create new address
        ---
        tags:
          - Address API
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
                  example : "Moskovskaja, 384"
        responses:
          201:
            description: The address was successfully created
        """
        address_json = request.json

        try:
            valid_address_json = AddressSchema(**address_json).dict(exclude_unset=True)
            address = CRUDAddress.create(**valid_address_json)
        except IntegrityError as exception:
            return abort(404, message=f"{exception}")
        except ValidationError as exception:
            return abort(404, message=f"{exception}")
        return make_response(jsonify(address), 201)

    @staticmethod
    def get():
        """
        This is the Address API
        Call this API and get back all addresses list
        ---
        tags:
          - Address API
        responses:
          200:
            description: All addresses returned
        """
        addresses = CRUDAddress.get_address_list()
        return make_response(jsonify(addresses), 200)


api.add_resource(AddressList, '/api/address')
api.add_resource(Address, '/api/address/<string:address_id>')
