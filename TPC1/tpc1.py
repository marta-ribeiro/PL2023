
def ler_ficheiro(idade, sexo, tensao, colesterol, batimento, tem_doenca):
	file = open("myheart.csv", "r")
	file.readline()  # ignorar a primeira linha
	for x in file:

		param = x.split(",")
		idade.append(int(param[0]))
		sexo.append(param[1])
		tensao.append(int(param[2]))
		colesterol.append(int(param[3]))
		batimento.append(int(param[4]))
		tem_doenca.append(int(param[5]))

	file.close()
	return 0


def doenca_sexo(sexo, tem_doenca):
	mulheres = 0
	homens = 0
	for i in range(len(tem_doenca)):
		if tem_doenca[i] == 1:
			if sexo[i] == "F":
				mulheres += 1
			else:
				homens += 1

	print(f"Existem {str(mulheres)} pessoas do sexo feminino e {str(homens)} pessoas do sexo masculino com doenca.")


def doenca_por_idade(idade, tem_doenca):
	faixa_etaria = {}

	for i in range(len(tem_doenca)):
		if tem_doenca[i] == 1:
			escolha = (idade[i] // 5) * 5
			if escolha in faixa_etaria:
				faixa_etaria[escolha] += 1
			else:
				faixa_etaria.update({escolha: 1})

	ordenado = dict(sorted(faixa_etaria.items()))
	print("Distribuição da doença pela faixa etária: ")
	for key, valor in ordenado.items():
		print(f"[{key},{key+4}] - {valor}")


def doenca_por_colesterol(colesterol, tem_doenca):
	nivel_colesterol = {}

	for i in range(len(tem_doenca)):
		if tem_doenca[i] == 1:
			escolha = (colesterol[i] // 10) * 10
			if escolha in nivel_colesterol:
				nivel_colesterol[escolha] += 1
			else:
				nivel_colesterol.update({escolha: 1})

	ordenado = dict(sorted(nivel_colesterol.items()))
	print("Distribuição da doença pelos níveis de colesterol: ")
	for key, valor in ordenado.items():
		print(f"[{key},{key+9}] - {valor}")


def main():

	idade = []
	sexo = []
	tensao = []
	colesterol = []
	batimento = []
	tem_doenca = []
	ler_ficheiro(idade, sexo, tensao, colesterol, batimento, tem_doenca)
	doenca_sexo(sexo, tem_doenca)
	doenca_por_idade(idade, tem_doenca)
	doenca_por_colesterol(colesterol, tem_doenca)


if __name__ == "__main__":
	main()
