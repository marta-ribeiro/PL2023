def main():
	ligado = True
	soma_parcial = 0
	soma_total = 0
	texto = input("> ")
	param = texto.split(" ")
	for i in param:
		if i.upper() == "ON":
			ligado = True
		elif i.upper() == "OFF":
			ligado = False
		elif i == '=':
			print(f"A soma de todos os valores até agora é {soma_total}.")
			print(f"A soma dos valores desde o último '=' é {soma_parcial}.")
			soma_parcial = 0
		elif i.isnumeric() and ligado:
			soma_parcial += int(i)
			soma_total += int(i)

	
if __name__ == "__main__":
	main()
