import math

A=int(input("Digite o lado A:"));
B=int(input("Digite o lado B:"));
C=int(input("Digite o lado C:"));

if A<B+C and B<A+C and C<A+B:
    print("É um triângulo");
    if A==B==C:
        print("equilátero!");
    elif A==B or B==C or A==C:
        print("isósceles!");
    else:
        print("escaleno!");
else:
    print("não é um triângulo");

peri=int(A+B+C);
sp=peri/2;
area=int(math.sqrt(sp*(sp-A)*(sp-B)*(sp-C)));

print("O perímetro deste triângulo é: ", peri, " e a área é: ", area)
