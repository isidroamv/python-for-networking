def pedir():
	n_1 = int(raw_input('Ingresa el primer numero: '))
	n_2 = int(raw_input('Ingresa el segundo numero: '))
	return [n_1, n_2]

def suma(numeros):
	resultado = numeros[0] + numeros[1]
	return resultado

def main():
	numeros = pedir()
	resultado = suma(numeros)
	print 'Resultado: ' + str(resultado)

if __name__ == '__main__':
	main()
