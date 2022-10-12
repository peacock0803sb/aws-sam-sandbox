import json
from pathlib import Path

from flask import Flask

app = Flask(__name__)


def init_app(setting_name: str) -> Flask:
    # app = Flask(__name__)
    app.logger.debug("Init Flask app config: %s", setting_name)

    config_json_path = Path(__file__).parent / "config" / "json-schemas"
    for p in config_json_path.glob("*.json"):
        with open(p) as f:
            json_name = p.stem
            schema = json.load(f)
        app.config[json_name] = schema
        app.logger.debug("Init json-schema config: %s", setting_name)
    return app
