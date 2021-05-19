salario=int(input("Digite o valor do salário:"))
if salario<100:
    print("Isento de pagamento de imposto de renda")
elif salario<500:
    pago=int(salario*0.10)
    print("O valor a ser pago é de ", pago)
elif salario<2000:
    pago=int(salario*0.18)
    print("O valor a ser pago é de ", pago)
else:
    pago=int(salario*0.25)
    print("O valor a ser pago é de ", pago)
