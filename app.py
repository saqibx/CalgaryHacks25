from flask import Flask, sessions
from config import Config
from extensions import db  # Import database setup

app = Flask(__name__)
app.config.from_object(Config)  # Load config settings
app.secret_key = Config.SECRET_KEY

# Import Blueprints (after app is created)
from routes.login import login_bp
from routes.home import home_bp
from routes.renters import renters_bp

# Register Blueprints
app.register_blueprint(login_bp)
app.register_blueprint(home_bp)
app.register_blueprint(renters_bp)

if __name__ == "__main__":
    app.run(debug=True)
