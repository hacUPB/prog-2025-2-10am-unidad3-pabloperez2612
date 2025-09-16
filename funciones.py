def suma(a, b):
	resultado = a + b
	return resultado

## resultado resta 

def resta(num1, num2):
	resultado = num1 - num2
	return resultado

## menu
def menu():
	print("1. Entrada\n2. Platos fuertes\n3. Bebidas\n4. Postres\n5. Salida")
	opcion = int(input("elija una opcion :"))
	return opcion

def entradas() :
	print("1. Pan de bono\t\t$3000")
	print("2. empanada\t\t$2500")
def fuertes() :
	print("1. bandeja paisa\t\t$50000")
	print("2. sancocho\t\t$30500")
	print("3. pescado frito \t\t$60000")
def bebidas() :
	print("1. agua natural\t\t$8000")
	print("2. gaseosa\t\t$5000")
def postres() :
	print("1. brownie\t\t$3000")
	print("2. torta de naranja\t\t$2000")

## funcion principal
eleccion = menu()

match(eleccion):
	case 1:
		entradas()
	case 2:
		fuertes()
	case 3:
		bebidas()
	case 4:
		postres()
	case _:
		print("opcion no valida")