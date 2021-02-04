
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)


from app import app

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)