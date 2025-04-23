# The Meiosis internals package
# It contains basic stuff to make using meiosis in some regards
import os
def get_bindings() -> list[tuple]:

    return [
        ('cls',lambda _: os.system('cls' if os.name == 'nt' else 'clear') ),# SCARY! look into other ways of clearing the STDOUT
        ('exit',lambda _: 1001),
        ('panic',lambda _: 1002)
        ]