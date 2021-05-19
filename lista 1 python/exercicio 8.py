import math

xa=int(input("Digite o ponto A do eixo X: "))
ya=int(input("Digite o ponto A do eixo Y: "))
xb=int(input("Digite o ponto B do eixo X: "))
yb=int(input("Digite o ponto B do eixo Y: "))
xc=int(input("Digite o ponto C do eixo X: "))
yc=int(input("Digite o ponto C do eixo Y: "))
ladoa=int(math.sqrt((xb-xa)^2+(yb-ya)^2))
ladob=int(math.sqrt((xc-xb)^2+(yc-yb)^2))
ladoc=int(math.sqrt((xa-xc)^2+(ya-yc)^2))
if A<B+C and C<A+B and B<A+C:
    per=int(ladoa+ ladob +ladoc)
    sp=per/2
    area=math.sqrt(sp*(sp-ladoa)*(sp-ladob)*(sp-ladoc))
    print("Tamanho lado A: ", ladoa)
    print("Tamanho lado B: ", ladob)
    print("Tamanho lado C: ", ladoc)
    print("Área do triângulo: ", area)
    print("Perímetro do triângulo: ", per)
else:
    print("Não é um triângulo")
