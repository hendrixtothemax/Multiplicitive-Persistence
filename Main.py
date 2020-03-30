#imports
from random import randrange
import time

#Main Class
class Main:
    def __init__(self):
        print('Multiplicitive Persistence Problem -- V0.2 -- Alexander Hendrix -- 2020')

def per(n,t,initnumb):

    if len(str(n))==1:
        if t > 10:
            print("INIT NUMBER:")
            print(initnumb)
            print("")
            print("Number Of Times: " + str(t))
        return "DONE"
    else:
        digits = [int(i) for i in str(n)]

        result = 1
        for j in digits:
            result *= j

        t += 1
        per(result,t,initnumb)

def Process():
    desLength = randrange(5,16,1)
    smrtNumbs = [2,4,6,7,8,9]
    length=len(smrtNumbs)
    FinalNumb=""
    i=0

    while i < desLength:
        FinalNumb = FinalNumb + str(smrtNumbs[randrange(length)])
        i += 1

    result = per(int(FinalNumb),0,FinalNumb)


Main()
while True:
    Process()
