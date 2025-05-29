from flask_restx import Api
from flask import Blueprint
from api.items import api as items_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    blueprint,
    version='1.0',
    title='Rest-in-a-Box API',
    description='A simple REST API with OpenAPI support',
    doc='/docs'  # Swagger UI at /api/docs
)

api.add_namespace(items_ns)
