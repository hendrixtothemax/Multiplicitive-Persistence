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

Main()
per(277777788888899,0)
