# app.py

import sys
import os
from flask_cors import CORS
import connexion

# 1) Ensure config.py exists
if not os.path.exists("config.py"):
    print("Missing config.py. Copy config.py.example and fill it in.")
    sys.exit(1)

# 2) Load and validate OPENAPI_STUB_DIR
from config import OPENAPI_STUB_DIR
if not os.path.exists(OPENAPI_STUB_DIR):
    print(f"Folder '{OPENAPI_STUB_DIR}' not found. Run the OpenAPI generator first.")
    sys.exit(1)

# 3) Make the generated stub importable
sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import encoder

def main():
    # Create a Connexion app and enable the built‐in Swagger UI at /Pikha/v1/ui
    app = connexion.App(
        __name__,
        specification_dir="./openapi/",
        options={
            "swagger_ui": True,
            # Mount the UI under your API’s base‐path
            "swagger_url": "/Pikha/v1/ui"
        }
    )

    # Use the JSON encoder from the generated stub code
    app.app.json_encoder = encoder.JSONEncoder

    # 4) Enable CORS on your API routes
    CORS(app.app, resources={r"/Pikha/v1/*": {"origins": "*"}})

    # 5) Mount your API (this reads Pikha.yaml & hooks up controller.*)
    app.add_api(
        "Pikha.yaml",
        arguments={"title": "Pikha Dust & Temp API"},
        pythonic_params=True
    )

    # 6) Run
    app.run(port=8080, debug=True)

if __name__ == "__main__":
    main()
