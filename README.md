# 파이썬 설정
## 파이썬 설치 하기
`pyenv`를 설치하고 python을 설치 하자..
이것도 버전 관리가 필요 함..
 * https://pyenv-win.github.io/pyenv-win/

초코로 아래와 같이 설치하는게 가장 간단.

```
choco install pyenv-win
pyenv install --list
pyenv install [version]
```

## 파이썬 가상 환경 만들어 주기

```
python -m pip install virtualenv
python -m virtualenv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## 사용중인 패키지 저장
activate 상태에서
```
pip freeze > requirements.txt
```

## 데이터베이스 설정
`.env` 파일을 만들고 아래와 같이 입력 해 준다.
```
DB_HOST=localhost
DB_NAME=stock
DB_USER=[USER_ID]
DB_PASS=[USER_PASSWORD]
```


## REF
* [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/index.html)
* [Flask로 REST API 구현하기](https://justkode.kr/python/flask-restapi-1)