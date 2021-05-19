compra=int(input("Digite o valor da compra: "))
pago=int(input("Digite o entregue: "))
if pago>compra:      
    troco=int(pago-compra)
    cem=int(troco/100)
    dez=int(troco%100)/10
    um=int(troco%100)%10
    quant=int(cem+dez+um)
    print("Seu pagamento de", pago,"para a compra de", compra ,
          "receberá troco de", troco, "em ", cem, "notas de cem",
          dez, "notas de dez e", um, "notas de um.")
else:
    print("Sua compra não terá troco")
