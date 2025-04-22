# app.py

import os
import sys
import connexion
from flask import Flask, send_from_directory
from flask_cors import CORS
from config import OPENAPI_STUB_DIR

# 1) Sanity checks
if not os.path.exists("config.py"):
    print("Missing config.py. Copy config.py.example and fill it in.")
    sys.exit(1)

if not os.path.exists(OPENAPI_STUB_DIR):
    print(f"Folder '{OPENAPI_STUB_DIR}' not found. Run the OpenAPI generator first.")
    sys.exit(1)

# 2) Create a Connexion App (which under the hood makes a Flask app for us)
app = connexion.App(
    __name__,
    specification_dir="./openapi/",
    options={
        "swagger_ui": True,
        "swagger_url": "/Pikha/v1/ui"
    }
)

# 3) Get at the underlying Flask instance
flask_app = app.app

# 4) Enable CORS for your API routes
CORS(flask_app, resources={r"/Pikha/v1/*": {"origins": "*"}})

# 5) Import the JSON encoder from your generated stub code
sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import encoder
flask_app.json_encoder = encoder.JSONEncoder

# 6) Mount your API under /Pikha/v1
app.add_api(
    "Pikha.yaml",
    arguments={"title": "Pikha Dust & Temp API"},
    pythonic_params=True
)

# 7) Serve your static HTML from the `static/` folder
#    so that GET / → static/index.html, GET /Dustall.html → static/Dustall.html, etc.

@flask_app.route("/", defaults={"path": "index.html"})
@flask_app.route("/<path:path>")
def static_serve(path):
    # static files are in ./static/<path>
    return send_from_directory("static", path)

# 8) Run!
if __name__ == "__main__":
    flask_app.run(port=8080, debug=True)
