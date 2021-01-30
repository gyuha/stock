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

# 코딩 스타일 규칙
## Naming convention
### 변수

* 소문자와 밑줄로 구성한다. - 스네이크케이스([snake_case](https://en.wikipedia.org/wiki/Snake_case))

### 상수

* 대문자와 밑줄로 구성한다. -스크리밍스네이크케이스([SCREAMING_SNAKE_CASE](https://en.wikipedia.org/wiki/SCREAMING_SNAKE_CASE))

### 클래스명

- 파스칼케이스(PascalCase)를 사용한다.
  - 첫자를 대문자, 문자마다 첫 문자를 대문자로 써서 연결한다. 밑줄은 사용하지 않는다.
- 예외(Execption)은 실제로 에러인 경우, `Error`를 붙인다.

#### 메서드명

* 스네이크케이스(snake_case)를 사용한다.
* 인스턴스 메소드의 첫번째 인자는 언제나 `self`이다.
* 클래스 메소드의 첫번째 인자는 언제나 `cls`이다.
* 메소드명은 함수명과 같으나 비공개(private)이면 앞에 _(밑줄)을 붙여준다.
* 서브 클래스(sub-class)의 이름 충돌을 막기 위해서는 밑줄 2개를 앞에 붙인다.

### _(밑줄) 사용 법

* 변수명의 _(밑줄)은 다음과 같은 의미
  * _single_leading_underscore: 내부적으로 사용되는 변수를 일컫습니다.
  * single_trailing_underscore_: 파이썬 기본 키워드와 충돌을 피하려고 사용합니다.
  * \_\_double_leading_underscore: 클래스 속성으로 사용되면 그 이름을 변경합니다.
     (ex. FooBar에 정의된 \_\_boo는 _FooBar\_\_boo로 바뀝니다.)
  * \_\_double_leading_and_trailing_underscore__: 마술(magic)을 부리는 용도로 사용되거나 사용자가 조정할 수 있는 네임스페이스 안의 속성을 뜻합니다. 이런 이름을 새로 만들지 마시고 오직 문서대로만 사용하세요.

### 참고
* [PEP 8 파이썬 코딩 스타일](http://pythonstudy.xyz/python/article/511-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%BD%94%EB%94%A9-%EC%8A%A4%ED%83%80%EC%9D%BC)
* [Python PEP 8](https://b.luavis.kr/python/python-convention)
* [파이썬 코딩 컨벤션](https://spoqa.github.io/2012/08/03/about-python-coding-convention.html)

# 사용 프레임워크
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask-RESTX](https://flask-restx.readthedocs.io/en/latest/index.html)
  * [Flask로 REST API 구현하기 - 2. 파일 분리, 문서화](https://justkode.kr/python/flask-restapi-2)
  * [Flask로 REST API 구현하기 - 3. JWT로 사용자 인증하기](https://justkode.kr/python/flask-restapi-3)

# Database


# 라이브러리
* [arrow](https://arrow.readthedocs.io/en/stable/)
* [numpy](https://numpy.org/)
* [pandas](https://pandas.pydata.org/)
## Blog post
  * [numpy](http://pythonstudy.xyz/python/article/402-numpy-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)
  * [판다스(Pandas) and 넘파이(Numpy) and 맷플롭립(Matplotlib)](https://wikidocs.net/32829)

## 도서
* [파이썬 증권 데이터 분석](http://www.yes24.com/Product/Goods/90578506)
  * [github]()
