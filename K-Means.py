import random
#multiplica um vetor por um escalar
def scalar_multiply (escalar, vetor):
    return [escalar * i for i in vetor]

#soma n vetores
def vector_sum (vetores):
    resultado = vetores[0]
    for vetor in vetores[1:]:
        resultado = [resultado[i] + vetor[i] for i in range (len(vetor))]   
    return resultado

#calcula a media de n vetores
def vector_mean (vetores):
    return scalar_multiply(1 / len(vetores), vector_sum(vetores))

#calcula o produto escalar
def dot (v, w):
    return sum(v_i * w_i for v_i, w_i in zip (v, w))

#calcular a soma dos quadrados
def sum_of_squares (v):
    return dot (v, v)

#subtração de vetores
def vector_subtract (v, w):
    return [v_i - w_i for v_i, w_i in zip (v, w)]

#distância ao quadrado
def squared_distance (v, w):
    return sum_of_squares(vector_subtract(v, w))

class KMeans:
    def __init__ (self, k, means = None):
        self.k = k
        self.means = means
    #grupos serão representados por valores de 0 a k -1
    def classify (self, ponto):
        return min (range(self.k), key = lambda i: squared_distance(ponto, self.means[i]))

    def train (self, pontos):
        #escolha de k elementos        
        #self.means = random.sample (pontos, self.k)       
        #nenhuma atribuição, para começar
        self.means = random.sample(pontos, self.k)
        assignments = None
        while True:
            #associa cada instância a um inteiro 0 <= i < k
            new_assignments = list(map (self.classify, pontos))
            #se não houver mudança, termina
            if new_assignments == assignments:
                return
            #atribuição atual se torna a nova
            assignments = new_assignments
            #cálculo das novas médias
            for i in range(self.k):
                 #pontos associados ao agrupamento i                
                 #note que pontos e assignments estão na ordem                
                 #por exemplo pontos = [1, 2, 3]  e assignments = [1, 2, 2]                
                 #indicam que a primeira instância está no grupo 1 e as demais                
                 #no grupo 2
                i_points = [p for p, a in zip (pontos, assignments)]
                if i_points:
                    self.means[i] = vector_mean(i_points)

def test_k_means():
    dados = [[1], [3], [6], [7], [10], [11]]
    kmeans = KMeans(3, [[11], [10], [6]])
    kmeans.train(dados)
    print (kmeans.means)
    #Exercício: criando a lista que possuirá todas as outras(lista dentro de outra lista)
    #metodo append
    macro_list = []
    macro_list.append(dados)
    macro_list.append(kmeans)
    print(macro_list)
  


test_k_means()

#[3, 4] - [2, 3], = [1, 1]

#[1, 2]
#[7, 9]
#[2, 2]
#[10, 13]

#calcular o ponto medio
#lista = [1, 2, 3]
#escalar = 2
#for item in scalar_multiply(escalar, lista):
#print (item) 

