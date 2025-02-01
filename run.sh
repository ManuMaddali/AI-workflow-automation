export PYTHONPATH=$PYTHONPATH:$(pwd)


# Set the FLASK_APP environment variable to point to the create_app function
export FLASK_APP=backend.__init__:create_app

# Optionally set Flask environment to development (this enables debug mode)
export FLASK_ENV=development

# Run the Flask application
flask run
