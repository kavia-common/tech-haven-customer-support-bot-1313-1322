from flask import Flask
from flask_cors import CORS
from .routes.health import blp as health_blp
from .routes.qa import blp as qa_blp
from flask_smorest import Api


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app, resources={r"/*": {"origins": "*"}})

# OpenAPI/Swagger configuration
app.config["API_TITLE"] = "Tech Haven Q&A API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config['OPENAPI_URL_PREFIX'] = '/docs'
app.config["OPENAPI_SWAGGER_UI_PATH"] = ""
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

# Register blueprints
api.register_blueprint(health_blp)
api.register_blueprint(qa_blp)
