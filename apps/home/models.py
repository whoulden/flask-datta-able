# -*- encoding: utf-8 -*-
from email.errors import BoundaryError
import uuid 

from sqlalchemy.orm import relationship 
from sqlalchemy import exc, select

from apps import db
from apps.authentication.models import Users


class Dashboard ():

    experiments = None
    cycles = 8
    exs = '12'

    def __init__(self, **kwargs):
        cycles = 0

    def calc(self):
        experiments = Experiment.query.all()

class Experiment (db.Model):

    __tablename__ = 'experiment'

    key            = db.Column(db.String(), primary_key=True)
    goal           = db.Column(db.String(), unique=False)
    last_run       = db.Column(db.DateTime, unique=False)
    last_completed = db.Column(db.DateTime, unique=False)
    models         = db.Column(db.String(), unique=False)
    recover_from   = db.Column(db.String(), unique=False)
    check_rows     = db.Column(db.Float, unique=False)
    train_rows     = db.Column(db.Float, unique=False)
    boundary       = db.Column(db.Float, unique=False)
    predict_query  = db.Column(db.String(), unique=False)
    predict_source = db.Column(db.String(), unique=False)
    train_query    = db.Column(db.String(), unique=False)
    train_source   = db.Column(db.String(), unique=False)

    @classmethod
    def find_by_key(cls, _id) -> "Experiment":
        return cls.query.filter_by(id=_id).first()
   
    def save(self) -> None:
        #try:
            db.session.add(self)
            db.session.commit()
          
        #except exc.SQLAlchemyError as e:
        #    db.session.rollback()
        #    db.session.close()
        #    error = str(e.__dict__['orig'])
        #    raise InvalidUsage(error, 422)
    
class Question (db.Model):

    __tablename__ = 'question'

    key            = db.Column(db.String(), primary_key=True)
    type           = db.Column(db.String(), unique=False)
    domain         = db.Column(db.String(), unique=False)
    description    = db.Column(db.String(), unique=False)

    @classmethod
    def find_by_key(cls, _key) -> "Question":
        return cls.query.filter_by(id=_key).first()
   
    def save(self) -> None:
        db.session.add(self)
        db.session.commit()
          
    
    
