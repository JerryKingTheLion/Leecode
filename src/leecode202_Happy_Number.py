def isHappy( n):
    # the most important tip: how to judge the appearence of cycle
    sums = 0
    ifCycle = []
    flag = 0

    while True:
        while n >= 10:
            sums += (n % 10) ** 2
            n = n // 10


        sums += n**2

        if flag == 0:
            flag = 1
        elif sums == 1:
            return True
        elif(sums in ifCycle):
            return False

        ifCycle.append(sums)
        n = sums
        sums = 0

n =3
print(isHappy(n))