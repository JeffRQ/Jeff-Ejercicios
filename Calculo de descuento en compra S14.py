
def calc_desc(total_mnt, porc_desc=10):
    descuento = (total_mnt * porc_desc) /100
    return descuento

valor_compra1 = calc_desc(87500)
desc1 = calc_desc(valor_compra1)
total_final = valor_compra1 - desc1

print("\n ***Resultado:1*** ")

print(f"total de compra es: $ {valor_compra1} \n ")
print(f"valor del descuento: {desc1} % \n ")
print(f"total a pagar: $ {total_final: .2f} \n ")

valor_compra2 = calc_desc(250000)
porc_desc2 = 12
desc2 = calc_desc(valor_compra2, porc_desc2)
total_final2 = valor_compra2 - desc2

print("\n ***Resultado:2*** ")

print(f"total de compra es: $ {valor_compra2} \n ")
print(f"descuento del: {porc_desc2} % \n ")
print(f"valor del descuento: $ {desc2} \n ")
print(f"total a pagar: $ {total_final2} \n")

print("\n ***")
