from flask import request
from flask_restx import Resource, Api, Namespace, fields

crawler = {}

Crawler = Namespace(
    name="크롤러",
    description="자료를 수집한다."
)


@Crawler.route('/companies')
class Companies(Resource):
  @Crawler.response(201, 'Success')
  def get(self):
    return {
        'result': True
    }

  def put(self):
