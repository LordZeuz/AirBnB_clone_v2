#!/usr/bin/python3

from models import storage
from models.state import State
from models.city import City



print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print("Find the city {} in the state {}".format(city, state))
