import random

class Dice(object):
    def getTwo(self, dice1, dice2):
        if dice1 == 1 and dice2 == 1: 
            return True
        
        return False

    def getThree(self, dice1, dice2):
        if dice1 == 1 and dice2 == 2 or dice1 == 2 and dice2 == 1: 
            return True
        
        return False

    def getFour(self, dice1, dice2):
        if dice1 == 2 and dice2 == 2: 
            return True
        
        if dice1 == 1 and dice2 == 3 or dice1 == 3 and dice2 == 1:
            return True
        
        return False

    def getFive(self, dice1, dice2):
        if dice1 == 1 and dice2 == 4 or dice1 == 4 and dice2 == 1: 
            return True

        if dice1 == 2 and dice2 == 3 or dice1 == 3 and dice2 == 2: 
            return True

        return False
    
    def getSix(self, dice1, dice2):
        if dice1 == 1 and dice2 == 5 or dice1 == 5 and dice2 == 1: 
            return True

        if dice1 == 4 and dice2 == 2 or dice1 == 2 and dice2 == 4: 
            return True
        
        if dice1 == 3 and dice2 == 3:
            return True

        return False

    def getSeven(self, dice1, dice2):
        if dice1 == 1 and dice2 == 6 or dice1 == 6 and dice2 == 1: 
            return True

        if dice1 == 2 and dice2 == 5 or dice1 == 5 and dice2 == 2: 
            return True

        if dice1 == 3 and dice2 == 4 or dice1 == 4 and dice2 == 3: 
            return True

        return False

    def getEight(self, dice1, dice2):
        if dice1 == 2 and dice2 == 6 or dice1 == 6 and dice2 == 2: 
            return True

        if dice1 == 3 and dice2 == 5 or dice1 == 5 and dice2 == 3: 
            return True

        if dice1 == 4 and dice2 == 4: 
            return True

        return False

    def getNine(self, dice1, dice2):
        if dice1 == 3 and dice2 == 6 or dice1 == 6 and dice2 == 3: 
            return True

        if dice1 == 4 and dice2 == 5 or dice1 == 5 and dice2 == 4: 
            return True

        return False

    def getTen(self, dice1, dice2):
        if dice1 == 4 and dice2 == 6 or dice1 == 6 and dice2 == 4: 
            return True

        if dice1 == 5 and dice2 == 5 or dice1 == 5 and dice2 == 5: 
            return True

        return False

    def getEleven(self, dice1, dice2):
        if dice1 == 5 and dice2 == 6 or dice1 == 6 and dice2 == 5: 
            return True

        return False

    def getTwelve(self, dice1, dice2):
        if dice1 == 6 and dice2 == 6: 
            return True

        return False

class Solutions(object):
    def __init__(self) -> None:
        # Wins
        self.comeOutPoint = 0 
        self.point = 0

        # Losses 
        self.craps = 0
        self.sevensOut = 0

        # Auxilaries 
        self.firstRoll = True
        self.dice = Dice()

    def rollingAPoint(self, func, num):


        if self.firstRoll is False and func:
            foundSecond = False 

            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            numToFunc = {
                2: self.dice.getTwo(dice1, dice2),
                3: self.dice.getThree(dice1, dice2),
                4: self.dice.getFour(dice1, dice2),
                5: self.dice.getFive(dice1, dice2),
                6: self.dice.getSix(dice1, dice2),
                7: self.dice.getSeven(dice1, dice2),
                8: self.dice.getEight(dice1, dice2),
                9: self.dice.getNine(dice1, dice2),
                10: self.dice.getTen(dice1, dice2),
                11: self.dice.getEleven(dice1, dice2),
                12: self.dice.getTwelve(dice1, dice2)
            }

            while 1 == 1:
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)

                if numToFunc[num]:
                    foundSecond = True

                if foundSecond is False and self.dice.getSeven(dice1, dice2):
                    self.sevensOut += 1
                    print("Sevens Out: You tried to get {} twice, but got a 7 before that".format(num))
                    break

                if foundSecond and self.dice.getSeven(dice1, dice2):
                    self.point += 1
                    print("Scored Point: You got {} twice before getting a 7".format(num))
                    break
            
            return True
        
        return False

    def simCraps(self, times): 
        # Wins
        self.comeOutPoint = 0 
        self.point = 0

        # Losses 
        self.craps = 0
        self.sevensOut = 0

        # Auxilaries 
        self.firstRoll = True
        firstRoll = self.firstRoll

        self.dice = Dice()
        dice = self.dice

        for i in range(times):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            if firstRoll and (dice.getSeven(dice1, dice2) or dice.getEleven(dice1, dice2)): 
                self.comeOutPoint += 1
                print("Scored ComOutPoint: You hit a 7 or 11 on 1st roll\n")
                self.firstRoll = False
                # self.printResults()
                continue

            if firstRoll and dice.getTwo(dice1, dice2) or dice.getThree(dice1, dice2) or dice.getTwelve(dice1, dice2):
                self.craps += 1
                print("Scored Craps: You hit either a 2, 3, 12 on 1st roll\n")
                # self.printResults()
                continue

            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            if self.rollingAPoint(dice.getFour(dice1, dice2), 4):
                # self.printResults()
                continue

            if self.rollingAPoint(dice.getFive(dice1, dice2), 5):
                # self.printResults()
                continue

            if self.rollingAPoint(dice.getSix(dice1, dice2), 6):
                # self.printResults()
                continue

            if self.rollingAPoint(dice.getEight(dice1, dice2), 8):
                # self.printResults()
                continue

            if self.rollingAPoint(dice.getNine(dice1, dice2), 9):
                # self.printResults()
                continue

            if self.rollingAPoint(dice.getTen(dice1, dice2), 10):
                # self.printResults()
                continue

            print("You scored nothing\n")

        self.printResults(times)
    
    def printResults(self, times):
        print()
        print("----------- Final Results ----------\n")
        print("You played this game {} times, and these are your wins and losses".format(times))
        print()
        print("--------------------------------")
        print("Wins: ")
        print("Come Out Point: ", self.comeOutPoint)
        print("Point: ", self.point)
        print()

        print("Losses: ")
        print("Craps: ", self.craps)
        print("Sevens Out: ", self.sevensOut)
        print("--------------------------------\n\n")

        wins = self.comeOutPoint + self.point
        losses = self.craps + self.sevensOut
        print("You won {} times, and loss {} times. Your winning probability is {}%\n".format(wins, losses, (wins/(wins + losses))*100))

        if self.comeOutPoint > self.point:
            print("You are more likely to win scoring ComeOutPoint than Point")
        else:
            print("You are more likely to win scoring Point than ComeOutPoint")

        print()

s = Solutions()
dice = Dice()

times = 1000000
s.simCraps(times)