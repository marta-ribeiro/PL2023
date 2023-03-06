import re

def ler_ficheiro(pasta, data, nome, pai, mae, obs):
	file = open("processos.txt", "r")
	x = 1

	while(x):
		x = file.readline()
		param = x.split("::")
		if x == '' or x == '\n':
			continue
		if param[0] == '':
			continue
		if param[1] == '':
			continue
		if param[2] == '':
			continue

		pasta.append(param[0])
		data.append(param[1])
		nome.append(param[2])
		pai.append(param[3])
		mae.append(param[4])
		obs.append(param[5])

	file.close()
	return 0

def processosPorAno(data):
	anos_dict = {}

	for x in data:
		ano = x.split("-")
		if ano[0] in anos_dict:
			anos_dict[ano[0]] += 1
		else:
			anos_dict.update({ano[0]: 1})

	return anos_dict

def tiposRelacao(obs):
	relacao = {}

	for x in obs:

		result = re.findall(r'\,([A-Za-z]+[\s]*[A-Za-z]*)\.', x)

		if not result:
			continue

		for y in result:
			if y in relacao:
				relacao[y] += 1
			else:
				relacao.update({y: 1})

	return relacao


def main():
	pasta = []
	data = []
	nome = []
	pai = []
	mae = []
	obs = []
	ler_ficheiro(pasta, data, nome, pai, mae, obs)

	print("O que pretende calcular? ")
	print("1. Frequência de processos por ano.\n"
		  "2. Frequência de nomes próprios e apelidos.\n"
		  "3. Frequência dos vários tipos de relação.\n"
		  "0. Sair.")


	opcao = int(input("Escolha: "))

	while opcao != 0:
		if opcao == 1:
			resposta1 = processosPorAno(data)
			print("Número de processos por ano:")
			print(resposta1)
		elif opcao == 2:
			break
		elif opcao == 3:
			resposta3 = tiposRelacao(obs)
			print("Tipos de relação:")
			print(resposta3)
		elif opcao == 4:
			break
		else:
			print("Valor não é aceite. Tente outra vez.")
		opcao = int(input("Escolha: "))

	print("Obrigado!")


if __name__ == "__main__":
	main()