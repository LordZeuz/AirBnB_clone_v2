#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        '''returns the list of City instances with state_id==State.id'''
        from models.city import City
        all_city = storage.all(City)
        rel_cit = [city for city in models.storage.all(City).values()
                   if self.id == city.state_id]
        return rel_cit
