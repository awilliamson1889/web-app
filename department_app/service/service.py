"""Service methods"""
from flask_restful import abort


def check_id_format(input_id):
    """Check ID format"""
    if not str(input_id).isdigit():
        abort(404, message="ID must be a number.")
