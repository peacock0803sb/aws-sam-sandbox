from __future__ import annotations
import logging
import os

from flask import Flask

from main import init_app, root  # noqa


def main(is_debug: bool | None = None) -> Flask:
    if is_debug:
        logging.basicConfig(level=logging.DEBUG)
    setting = os.environ.get("SETTING", "local")
    app = init_app(setting)
    return app


def to_apigateway():
    from asgiref.wsgi import WsgiToAsgi
    from mangum import Mangum

    app = WsgiToAsgi(main())
    return Mangum(app, lifespan="off")


handler = to_apigateway()


if __name__ == "__main__":
    main(is_debug=True).run(host="127.0.0.1", port=5000)
