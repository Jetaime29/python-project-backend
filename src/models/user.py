from src import db
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from .allcodes import Allcode


class User(db.Model):

    __tablename__ = "Users"
    # Define column
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullName = Column(String(255), nullable=False)
    genderID = Column(String(255), ForeignKey(Allcode.keyMap))
    address = Column(String(255), nullable=False)
    phonenumber = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    roleID = Column(String(255), ForeignKey(Allcode.keyMap))
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), server_default=func.now())

    # Define relationship
    orders = relationship("Order", backref="orderData")

    # Constuctor
    def __init__(self):
        pass

    def __repr__(self):
        return f"<User {self.fullName}>"
