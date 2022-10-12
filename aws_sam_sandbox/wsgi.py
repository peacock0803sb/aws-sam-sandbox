import json
import logging
import os
from pathlib import Path

from flask import Flask

from aws_sam_sandbox import app, routers  # noqa


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


def main(is_debug: bool | None = None) -> Flask:
    if is_debug:
        logging.basicConfig(level=logging.DEBUG)
    setting = os.environ.get("SETTING", "local")
    app = init_app(setting)
    return app


def lambda_handler(event, context) -> None:
    main(is_debug=False)


if __name__ == "__main__":
    main(is_debug=True).run(host="127.0.0.1", port=5000)
