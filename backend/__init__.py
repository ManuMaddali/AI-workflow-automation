from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    CORS(app)
    # Configurations
   
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE_PATH = os.path.join(BASE_DIR, "../instance/db.sqlite3")

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DATABASE_PATH}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    print(f"Database Absolute Path: {DATABASE_PATH}")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)



    # Import models to register with SQLAlchemy
 
    from backend.models.user import User
    from backend.models.workflow import Workflow
    from backend.models.task import Task


    # Register the Blueprint
    from backend.app.routes import routes
    app.register_blueprint(routes)
    
    return app

