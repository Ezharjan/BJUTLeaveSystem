# coding: utf-8

from sqlalchemy.exc import IntegrityError
from db import db


class BaseModel(object):

    @classmethod
    def add(cls, **kwargs):
        for key, value in kwargs.items():
            if hasattr(cls, '_' + key):
                kwargs[key] = value.value

        obj = cls(**kwargs)
        db.session.add(obj)
        try:
            db.session.commit()
            return obj
        except IntegrityError:
            db.session.rollback()
            raise IntegrityError

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, '_' + key):
                setattr(self, '_' + key, value.value)
                kwargs[key] = value.value
            else:
                setattr(self, key, value)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    @classmethod
    def save(cls, **kwargs):
        if kwargs.get('id') and kwargs['id']:
            obj = cls.get(kwargs['id'])
            if obj:
                obj.update(**kwargs)
        else:
            obj = cls.add(**kwargs)
        return obj

    @classmethod
    def get(cls, id):
        return cls.query.filter(cls.id == id).first()

    @classmethod
    def count(cls):
        return cls.query.count()

    @classmethod
    def delete(cls, id):
        obj = cls.query.filter(cls.id == id).first()
        if not obj:
            return True
        db.session.delete(obj)
        try:
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
        return False

    @classmethod
    def paginate(cls, condition, **kwargs):
        return cls.query.filter(condition).paginate(error_out=False, **kwargs)

    @classmethod
    def all(cls):
        return cls.query.filter().all()
