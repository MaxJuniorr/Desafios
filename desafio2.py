y = [int(x) for x in input().split()]
contador = 0
if len(y) == 2:
    n, q = y
    if (1 <= n <= 100000) and (1<= q <= n):
        moradores = [int(x) for x in input().split()]
        if len(moradores) == n:
            for i in range(q):
                x = [int(x) for x in input().split()]
                if (len(x) != 2) and (i == q-1) and contador == 0:
                    print('Erro! Seria necessário ter, pelo menos, um evento tipo bombeiro.')
                else:
                    if len(x) == 3:
                        moradores[x[1]-1] = x[2]
                    elif len(x) == 2:
                        print(sum(moradores[:x[1]]))
                        contador += 1
                    else:
                        print('Erro! Seus eventos foram definidos incorretamente.')
        else:
            print('Erro! O número de andares não está batendo com o informado.')
else:
    print('Erro! Por favor, verifique se você digitou as informações corretamente.')