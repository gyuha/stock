from controller.crawler.crawler import Crawler
import os
from flask import Flask
from flask_restx import Resource, Api
from dotenv import load_dotenv

load_dotenv(verbose=True)

app = Flask(__name__)
api = Api(app,
          version="0.1",
          title="Stock - Show me the money",
          description="주식을 해 볼까 해서 제작 중.",
          terms_url="/",
          contact="nicegyuha@gmail.com",
          license="MIT"
          )


@api.route('/hello')
class HelloWorld(Resource):
  def get(self):
    return {'hello': os.getenv('DB_NAME')}


api.add_namespace(Crawler, '/crawler')


if __name__ == '__main__':
  app.run(debug=True)
