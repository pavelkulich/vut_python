# vytvoreni tridy Animal
class Animal:
    # definice inicializacni metody
    # metoda je volana pri vytvareni kazdeho objektu jednou
    def __init__(self):
        print("Animal constructed")

    # definice metody move
    def move(self):
        print("moving")


# vytvoreni objektu tridy Animal a prirazeni do promenne animal1
animal1 = Animal()

# zavolani metody move na objektu animal1
animal1.move()

# objektu vytvorenych z predpisu tridy Animal muze byt nekonecne mnoho
# vytvoreni objektu tridy Animal a prirazeni do promenne animal2
animal2 = Animal()

# zavolani metody move na objektu animal2
animal2.move()
