#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.city import City
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    @property
    def cities(self):
        '''returns the list of City instances with state_id==State.id'''
        from models.__init__ import storage
        all_city = storage.all(City)
        rel_city = {k: v for k, v in all_city.items()
                    if v.state_id == self.id}
        return rel_city
