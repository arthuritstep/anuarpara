from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index = True) 
    username = Column(String, unique=True, index=True)
    balance = Column(Float, default = 1000.0)
    
class Transaction(Base):
    __tablename__='Transactions'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    type = Column(String)
    amount = Column(Float)
    timestamp = Column(DateTime, default = datetime.utesnow)