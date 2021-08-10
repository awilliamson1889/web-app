"""Rest addresses Api"""
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api, abort
from pydantic import ValidationError
from department_app.models import AddressModel, db
from department_app.schemas import AddressSchema
from department_app.service import CRUDAddress

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
        address = CRUDAddress.get_address(address_id)
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
        if not str(address_id).isdigit():
            abort(404, message="ID must be a number.")
        address = AddressModel.query.filter_by(id=address_id).first()
        if not address:
            abort(404, message=f"Could not find address with ID: {address_id}.")

        address_data = {'name': address.name}

        address_json = request.json
        address_data.update(address_json)

        try:
            AddressSchema(**address_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        address.name = address_data['name']

        db.session.commit()
        return make_response(jsonify(address), 201)


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
        address_data = {'name': request.json['name']}
        try:
            address = AddressSchema(**address_data)
        except ValidationError as exception:
            abort(404, message=f"Exception: {exception}")

        result = AddressModel(**address_data)

        db.session.add(result)
        db.session.commit()
        return address.dict(), 201

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
        addresses = AddressModel.query.all()
        return make_response(jsonify(addresses), 200)


api.add_resource(AddressList, '/api/address')
api.add_resource(Address, '/api/address/<string:address_id>')
