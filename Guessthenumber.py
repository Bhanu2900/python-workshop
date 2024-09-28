import random

class Guessthenumber:
    def __init__(self):
        self.low = 1
        self.high = 1
        self. live = 3
        self. guesses =0


        def set_range(self, high):
            if(self.low+1)<high:
                self.high = high
            else:
                return "please give a bigger digit"

            def play(self):
                if (self.low +1)> self.high:
                    print("restart the game")

                while self.guesses < 3:
                    self.guesses +=1
                    num = random.randint(self.low, self.high)
                    guess = int(input("please enter the number:"))
                    if guess == num:
                        print("you win")
                        break
                    else:
                        print("you loss")

