capitales_paises = {}

for _ in range(5):
    capital = input("Ingrese el nombre de una capital: ")
    pais = input("Ingrese el nombre del país asociado a " + capital + ": ")
    capitales_paises[capital] = pais

print("_______________________________________________________________________________")
nombre_turista = input("Ingrese el nombre del turista: ")
capital_procedencia = input("Ingrese la capital del turista: ")

print("El turista con el nombre " + nombre_turista + " viene de la capital " + capital_procedencia + " y su país es " + capitales_paises.get(capital_procedencia, 'desconocido') + ".")
