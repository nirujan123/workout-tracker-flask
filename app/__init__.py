import os
from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    os.makedirs(app.instance_path, exist_ok=True)

    app.config["DATABASE"] = os.path.join(app.instance_path, "workout_tracker.sqlite")

    from .db import close_db
    app.teardown_appcontext(close_db)

    from .routes import bp
    app.register_blueprint(bp)

    return app
