import os

from dotenv import load_dotenv
from flask import Flask
from flask_restx import Api, Resource

from config.config import ProductionConfig, DevelopmentConfig

import util.response as resp
from route.crawler.crawler import Crawler
from util.database import db
from util.response import response_with

load_dotenv(verbose=True)


def create_app(**config_overrides):
  app = Flask(__name__)
  api = Api(app,
            version="0.1",
            title="Stock - Show me the money",
            description="주식을 해 볼까 해서 제작 중.",
            terms_url="/",
            contact="nicegyuha@gmail.com",
            license="MIT"
            )

  work_env = os.getenv('WORK_ENV')

  if work_env == 'production':
    app_config = ProductionConfig
  elif work_env == 'development':
    app_config = DevelopmentConfig
  else:
    app_config = DevelopmentConfig

  app.config.from_object(app_config)
  api.add_namespace(Crawler, '/crawler')

  db.init_app(app)

  @api.route('/hello')
  class HelloWorld(Resource):
    def get(self):
      return {'hello': os.getenv('DB_NAME')}

  @app.errorhandler(400)
  def bad_request(e):
    return response_with(resp.BAD_REQUEST_400)

  @app.errorhandler(500)
  def server_error(e):
    return response_with(resp.SERVER_ERROR_500)

  @app.errorhandler(404)
  def not_found(e):
    return response_with(resp.SERVER_ERROR_404)

  return app


if __name__ == "__main__":
  debug_mode = os.getenv('WORK_ENV') == 'development'
  app = create_app()
  app.run(port=5000, host="0.0.0.0", use_reloader=True, debug=True)
