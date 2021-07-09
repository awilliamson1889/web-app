"""rest api"""
from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, Api, abort
from department_app.models.app_models import Address
from department_app.models.address_schema import AddressModel
from department_app.models.app_models import db
from pydantic import ValidationError
from flasgger import Swagger, swag_from

address_api = Blueprint('address_api', __name__)

api = Api(address_api)


class AddressInfo(Resource):
    def get(self, address_id):
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
        if not str(address_id).isdigit():
            abort(404, message=f"ID must be a number.")
        address = Address.query.filter_by(id=address_id).first()
        if not address:
            abort(404, message=f"Could not find address with ID: {address_id}.")
        return make_response(jsonify(address), 200)

    def put(self, address_id):
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
            abort(404, message=f"ID must be a number.")
        address = Address.query.filter_by(id=address_id).first()
        if not address:
            abort(404, message=f"Could not find address with ID: {address_id}.")

        if 'name' in request.json:
            address.name = request.json['name']
        try:
            result = AddressModel(id=address.id, name=address.name)
        except ValidationError as e:
            abort(404, message=f"Exception: {e}")

        db.session.commit()
        return result.dict(), 204


class AllAddressInfo(Resource):
    def post(self):
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
        e = Address.query.all()
        address_data = {'id': len(e)+100, 'name': request.json['name']}
        try:
            address = AddressModel(**address_data)
        except ValidationError as e:
            abort(404, message=f"Exception: {e}")

        result = Address(**address_data)

        db.session.add(result)
        db.session.commit()
        return address.dict(), 201

    def get(self):
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
        d = Address.query.all()
        return make_response(jsonify(d), 200)


api.add_resource(AllAddressInfo, '/api/address')
api.add_resource(AddressInfo, '/api/address/<string:address_id>')
