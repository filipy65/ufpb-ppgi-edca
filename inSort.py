#Solicitar nome do arquivo para leitura dos dados
nome_do_arquivo = input("\nDigite o nome do arquivo com os valores para ordenar (que esteja no mesmo diretório deste script): ")

#Ler o valores de um arquivo
arquivo = open(nome_do_arquivo)

#Inicializar o vetor
vetor = []

#Atribuir aos índices do vetor os valores do arquivo
for x in arquivo:
    #Converter o valor em inteiro
    x = int(x)
    #Inserir valor ao vetor
    vetor.append(int(x))

#Contar a quantidade de elementos do vetor
n = len(vetor)

#Definir função de Insertion Sort
def inSort():
    #Laço do segundo ao último elemento do vetor
    for i in range(1, n):
        #Definir o valor do pivô
        pivo = vetor[i]
        #Definir índice a esquerda para testar
        j = i-1
        #Laço enquanto o índice a esquerda do pivô for válido e seu valor maior que o pivô
        while j >= 0 and vetor[j] > pivo:
            #Definir o valor do índice do pivo com o valor do índice a sua esquerda
            vetor[j+1] = vetor[j]
            #Decrementar o índice atual para ir a esquerda
            j -= 1
        #Inserir valor do pivô em sua posição adequada no momento
        vetor[j+1] = pivo

#Chama a função apropriada e nomeia o arquivo de saída de acordo
inSort()
nome_do_arquivo = "InSorted_" + nome_do_arquivo

#Cria o arquivo para salvar os dados de saída
arquivo = open(nome_do_arquivo, "a")

#Percorrer os elementos do vetor...
for x in vetor:
    #Escrever cada elemento do vetor em uma linha no arquivo
    arquivo.write(str(x) + "\n")

#Notificar o usuário o nome do arquivo com os dados de saída salvo
print(f"\nOs dados foram salvos no arquivo '{nome_do_arquivo}'.\n") 
    
