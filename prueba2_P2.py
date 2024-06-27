valor_dolar= 950

precios_pesos = []

for i in range(10):
    precio_pesos = float(input("Ingrese el precio {} en pesos chilenos: "))
    precios_pesos.append(precio_pesos)

precios_usd = [precio / valor_dolar for precio in precios_pesos]

print("_________________________________________________________")
print("Precios en dólares (USD):")
for precio in precios_usd:
    print(precio)
