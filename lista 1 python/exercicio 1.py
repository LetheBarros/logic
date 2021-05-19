gasolina=float(input("Qual o preço da gasolina?"))
alcool=float(input("Qual o preço do alcool?"))

calc=alcool/gasolina

if calc <= 0.7:
    print("usar álcool!")
else:
    print("usar gasolina!")
