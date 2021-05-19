import math

a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=int(input("Digite o valor de c: "))
delta=int(b*b-4*a*c)
r1=float((-b + math.sqrt(delta))/(2*a))
if delta<0:
    print("Esta equação não possui solução real")
elif delta == 0:
        print("A primeira raiz é igual a ", r1)
        print("Devido delta ser 0, as duas raízes são ", r1)
else:
    print("A primeira raiz é igual a ", r1)
    r2=float((-b-math.sqrt(delta))/(2*a))
    print("A segunda raiz é igual a ", r2)

