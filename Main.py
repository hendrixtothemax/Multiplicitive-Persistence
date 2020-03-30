#imports
from random import randrange

#Main Class
class Main:
    def __init__(self):
        print('Multiplicitive Persistence Problem -- V0.1 -- Alexander Hendrix -- 2020')

def per(n,t):
    times = t

    if len(str(n))==1:
        print("Number Of Times: " + str(times))
        return "DONE"
    else:
        digits = [int(i) for i in str(n)]

        result = 1
        for j in digits:
            result *= j

        times += 1
        print(result)
        per(result,times)

def Process():
    desLength = randrange(5,30,1)
    smrtNumbs = [2,4,6,7,8,9]
    length=len(smrtNumbs)
    FinalNumb=""
    i=0

    while i < desLength:
        FinalNumb = FinalNumb + str(smrtNumbs[randrange(length)])
        i += 1

    print("INIT NUMBER:")
    print(FinalNumb)
    print("")
    per(int(FinalNumb),0)


Main()
#per(277777788888899,0)
Process()
