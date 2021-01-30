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

  def get_krx_companies():
    url = 'http://kind.krx.co.kr/corpgeneral/corpList.do'
    data = {
        'method': 'download',
        'orderMode': '1',           # 정렬컬럼
        'orderStat': 'D',           # 정렬 내림차순
        'searchType': '13',         # 검색유형: 상장법인
        'fiscalYearEnd': 'all',     # 결산월: 전체
        'location': 'all',          # 지역: 전체
    }

    res = requests.post(url, data=data)
    content = BytesIO(res.content)
    dfs = pd.read_html(content, header=0, parse_dates=['상장일'])
    df = dfs[0].copy()

    # 숫자를 앞자리가 0인 6자리 문자열로 변환
    # - 방법.1
    # df['종목코드'] = df['종목코드'].astype(np.str)
    # df['종목코드'] = df['종목코드'].str.zfill(6)
    # - 방법.2
    # df['종목코드'] = df['종목코드'].map('{:06d}'.format)
    # - 방법.3
    df['종목코드'] = df['종목코드'].map(lambda x: f'{x:0>6}')
    return df

  @Crawler.response(201, 'Success')
  def get(self):
    return {
        'result': True
    }

  def put(self):
