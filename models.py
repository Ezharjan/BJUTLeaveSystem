import datetime

from sqlalchemy.dialects.mysql import TEXT

from base_model import BaseModel
from db import db

class LeaveBeijing(db.Model, BaseModel):
    # 定义表名
    __tablename__ = 'leave_beijing'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64))
    student_id = db.Column(db.String(64))
    colleage = db.Column(db.String(64))
    id_card = db.Column(db.String(64))
    leave_time = db.Column(db.String(64))
    back_time = db.Column(db.String(64))
    counselor = db.Column(db.String(64))
    transportation = db.Column(db.String(64))
    telephone = db.Column(db.String(64))
    healthy = db.Column(db.String(64))
    reason = db.Column(TEXT)
    destination = db.Column(db.String(64))
    is_del = db.Column(db.Boolean, nullable=False, server_default='0')
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)


    @classmethod
    def leave_beijing_list(cls, where, paginate=False):
        cond = cls.id == cls.id
        if where.get('activity_id'):
            cond = (cls.activity_id == where.get('activity_id'))
        if where.get('jurisdiction'):
            cond &= (cls.jurisdiction == where.get('jurisdiction'))
        if where.get('group_id'):
            cond &= (cls.group_id == where.get('group_id'))
        if where.get('group_ids'):
            cond &= (cls.group_id.in_(where.get('group_ids')))
        if where.get('is_del'):
            cond &= (cls.is_del == where.get('is_del'))
        if paginate:
            return cls.query.filter(cond).paginate(error_out=False)
        else:
            return cls.query.filter(cond).all()





class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User',backref='role') # 反推与role关联的多个User模型对象



class User(db.Model):
    # 定义表名
    __tablename__ = 'users'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64),unique=True)
    pswd = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 设置外键

if __name__ == '__main__':

    # 删除所有表
    db.drop_all()

    # 创建所有表
    db.create_all()