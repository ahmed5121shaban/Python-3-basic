class game:
    def __init__(self):
            while True:
                print('''  '''Welcome in our game.
                         1- calculate game
                         2- destance word game
                         3- press X to exit''' ''')
                choice = input('inter your game number : ')
                if choice=='X' or choice=='x':
                    break
                if int(choice) == 1:
                    num1 = int(input('enter start : '))
                    num2 = int(input('enter end : '))
                    num3 = int(input('enter start : '))
                    num4 = int(input('enter end : '))
                    self.calculate(num1,num2,num3,num4)
                elif int(choice) == 2:
                    txt = input('enter your text : ')
                    self.destance(txt)
            
                choice1=input('press any key to play again or N to exit : ')
                if choice1=='N' or choice1=='n':
                    break
    def calculate(self,num1,num2,num3,num4):
                for x in range(num1,num2 + 1):
                    for y in range(num3,num4 + 1):
                        print(f'{x} X {y} = {x*y}')
                    print('-------------------')
                    
    def destance(self,txt):
                 print(len(txt.split()))
            

a = game()
