import random
class Chance:
        
    'A class that consists of games of random chance such as dice rolls and types of random number generation'

    @staticmethod
    def diceRoll(diceSides: int):
        'Creates a random roll using a inputed amount of sides. Returns the resulted roll and if an error occurs a -1 will be returned'

        result = -1
        if diceSides <= 1:
            print("diceSides is {0} and thus cannot be rolled without error".format(diceSides))
        else:
            result = random.randint(1,diceSides)
        return result

    @staticmethod
    def diceRollModified(diceSides: int, modifier: int):
        'Creates a random roll using a inputed amount of sides with a modifier added. Returns the resulted roll with the modifier added and if an error occurs a -1 will be returned'

        result = -1
        if diceSides <= 1:
            print("diceSides is {0} and thus cannot be rolled without error".format(diceSides))
        else:
            result = random.randint(1,diceSides) + modifier
        return result

    @staticmethod
    def randomSelect(group: list):
        selectedIndex = random.randint(0, (len(group)))
        return selectedIndex
#a = [1,41,42,145,12,3,1,44]
#b = Chance.randomSelect(a)
#print("{0}:{1}".format(b, a[b]))
