from interface.interface import *
from solve import *

def start_game():
    initial_node = getStartingNode()
    interface = Interface(initial_node)
    interface.main()

start_game()