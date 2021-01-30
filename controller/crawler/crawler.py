from flask import request
from flask_restx import Resource, Api, Namespace, fields

import pandas as pd
import numpy as np
import requests

from io import BytesIO

crawler = {}

Crawler = Namespace(
    name="크롤러",
    description="자료를 수집한다."
)


@Crawler.route('/krx/companies')
class Companies(Resource):

  def _get_krx_companies(self):
    '''
    상장 기업 목록 받아 오기
    참고 :
     * https://blog.naver.com/cflab/222141302166
     * https://comdoc.tistory.com/entry/%EC%83%81%EC%9E%A5-%EB%B2%95%EC%9D%B8-%EB%AA%A9%EB%A1%9D-KIND
    '''
    data = pd.read_html(
        'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&pageIndex=1&currentPageSize=5000&orderMode=3&orderStat=D&marketType=stockMkt&searchType=13&fiscalYearEnd=all&&location=all')[0]

    # 숫자를 앞자리가 0인 6자리 문자열로 변환
    # - 방법.1
    # df['종목코드'] = df['종목코드'].astype(np.str)
    # df['종목코드'] = df['종목코드'].str.zfill(6)
    # - 방법.2
    # df['종목코드'] = df['종목코드'].map('{:06d}'.format)
    # - 방법.3
    data['종목코드'] = data['종목코드'].map(lambda x: f'{x:0>6}')

    return data.rename(columns={'회사명': 'company', '종목코드': 'code', '업종': 'industry', '주요제품': 'product', '상장일': 'listing_date', '결산월': 'settlement_month', '대표자명': 'ceo_name', '홈페이지': 'homepage', '지역': 'area'})

  @Crawler.response(201, 'Success')
  def get(self):
    return {
        'result': True
    }

  def put(self):
    return {

    }
