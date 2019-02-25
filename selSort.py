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

#Definir função de Selection Sort
def selSort():
    #Laço do primeiro ao penúltimo elemento do vetor
    for i in range(n-1):
        #Definir o índice a ser testado da rodada
        i_menor = i
        #Laço do elemento a direita do elemento atual até o último elemento do vetor
        for j in range(i+1, n):
            #Se o valor no índice atual for menor que o do i_menor...
            if vetor[j] < vetor[i_menor]:
                #Definir o índice atual como o índice com o menor valor dessa rodada
                i_menor = j
        #Se o índice atual não for o com menor valor do vetor...
        if vetor[i] != vetor[i_menor]:
            #Guardar a posição atual temporariamente
            temp = vetor[i]
            #Definir o valor do índice atual com o valor menor encontrado
            vetor[i] = vetor[i_menor]
            #Definir o valor no ´índice onde estava o valor menor com o valor do índice atual
            vetor[i_menor] = temp

#Chama a função apropriada e nomeia o arquivo de saída de acordo
selSort()
nome_do_arquivo = "SelSorted_" + nome_do_arquivo    

#Cria o arquivo para salvar os dados de saída
arquivo = open(nome_do_arquivo, "a")

#Percorrer os elementos do vetor...
for x in vetor:
    #Escrever cada elemento do vetor em uma linha no arquivo
    arquivo.write(str(x) + "\n")

#Notificar o usuário o nome do arquivo com os dados de saída salvo
print(f"\nOs dados foram salvos no arquivo '{nome_do_arquivo}'.\n") 
    
