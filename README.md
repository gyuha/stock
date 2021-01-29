# 파이썬 설정
## 파이썬 설치 하기
`pyenv`를 설치하고 python을 설치 하자..
이것도 버전 관리가 필요 함..
 * https://pyenv-win.github.io/pyenv-win/

초코로 아래와 같이 설치하는게 가장 간단.

```cmd
choco install pyenv-win
pyenv install --list
pyenv install [version]
```

## 파이썬 가상 환경 만들어 주기

```cmd
python -m pip install virtualenv
python -m virtualenv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

## 사용중인 패키지 저장
activate 상태에서
```cmd
pip freeze > requirements.txt
```

## 장고 버전 확인
```cmd
python -m django --version
```

## 장고 실행하기
```cmd
python manage.py runserver
```

## REF
* django rest api quick start
 * https://www.django-rest-framework.org/tutorial/quickstart/
