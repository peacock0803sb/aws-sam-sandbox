from __future__ import annotations
import logging
import os

from flask import Flask

from aws_sam_sandbox import routers  # noqa
from aws_sam_sandbox.initilizer import init_app


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
