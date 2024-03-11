def convertidorG (grad_centi):
    farenheit = (9*(grad_centi-32))/5
    kelvin = grad_centi + 273.15

    return farenheit, kelvin

grad_centi = float(input("Ingrese valor grados centigrados"))

r_farenheit, r_kelvin = convertidorG(grad_centi)

print(" grados farenheit ",  r_farenheit, " grados kelvin ", r_kelvin)
