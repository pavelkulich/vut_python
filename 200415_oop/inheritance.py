# vytvoreni tridy Animal
class Animal:
    # definice inicializacni metody
    # metoda je volana pri vytvareni kazdeho objektu jednou
    def __init__(self):
        print("Animal constructed")

    # definice metody move
    def move(self):
        print("moving")


# vytvoreni tridy Dog, ktera dedi z tridy Animal
class Dog(Animal):
    # definici inicializacni metody
    def __init__(self):
        print("Dog constructed")

    # definice metody do_sound
    def do_sound(self):
        print("barking")


# vytvoreni objektu tridy Dog a prirazeni do promenne dog1
dog1 = Dog()

# zavolani metody do_sound na objektu dog1
dog1.do_sound()

# zavolani metody move na objektu dog1
# metodu move objekt dog1 dedi z tridy Animal
dog1.move()

# objektu vytvorenych z predpisu tridy Dog muze byt nekonecne mnoho
# vytvoreni objektu tridy Dog a prirazeni do promenne dog2
dog2 = Dog()

# zavolani metody do_sound na objektu dog2
dog2.do_sound()

# zavolani metody move na objektu dog2
# metodu move objekt dog2 dedi z tridy Animal
dog2.move()

# je mozne vytvaret i objekty primo z tridy Animal
# vytvoreni objektu tridy Animal a prirazeni do promenne animal1
animal1 = Animal()

# zavolani metody move na objektu animal1
animal1.move()

# metodu do_sound na objektu animal1 nemuzeme zavolat, jelikoz ve tride Animal
# neni metoda do_sound definovana
