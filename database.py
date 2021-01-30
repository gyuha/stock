from flask.ext.migrate import Migrate
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.mutable import MutableDict

migrate = Migrate()
db = SQLAlchemy()
