def Valor_gorjeta(valor ,prc):
    gorjeta = valor *(prc/100)
    return gorjeta
T_valor=100.00
T_prc=15
resu=Valor_gorjeta(T_valor,T_prc)
print(resu)