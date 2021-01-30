import os
from flask import Flask
from flask_restx import Resource, Api
from dotenv import load_dotenv

load_dotenv(verbose=True)

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
  def get(self):
    return {'hello': os.getenv('DB_NAME')}


if __name__ == '__main__':
  app.run(debug=True)
