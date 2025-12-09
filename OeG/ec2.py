class Digrafo:
    def __init__(self, numVertices: int):
        self.numVertices = numVertices
        self.digrafo = [[0] * numVertices for _ in range(numVertices)]
    
    def adicionar_aresta(self, origem, destino, peso):
        if 0 <= origem < self.numVertices and 0 <= destino < self.numVertices:
            self.digrafo[origem][destino] = peso
        else:
            print('Vértices inválidos.')
    
    def transpor(self, grafo: list) -> list:
        n = len(grafo)
        grafo_transposto = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                grafo_transposto[i][j] = grafo[j][i]
        return grafo_transposto

    def imprimir_matriz(self, digrafo:list):
        print("   ", end="")
        for i in range(self.numVertices):
            print(f"{i:3}", end="")
        print("\n" + "-" * (self.numVertices * 4 + 4))

        for i, linha in enumerate(digrafo):
            print(f"{i}| ", end="")
            for val in linha:
                print(f"{val:3}", end="")
            print()
        print("\n" + "-" * (self.numVertices * 4 + 4))
    
    def imprimir_arvoreGeradoraMinima(self, pai:list, caminho:list):
        print(' --- Árvore Geradora Mínima ---')
        print('Aresta \tPeso')
        peso_total = 0
        for i in range(1, len(caminho)):
            peso = caminho[i]
            print(f'{pai[i]}->{i} \t{peso}')
            peso_total+=peso
        print(f'Custo total da AGM: {peso_total}')
    
    def imprimir_caminho(self, vetor:list):
        print("   ", end="")
        for i in range(len(vetor)):
            print(f"{i:3}", end="")
        print("\n" + "-" * (len(vetor) * 4 + 4))
        
        print("   ", end="")
        for i in range(len(vetor)):
            print(f"{vetor[i]:3}", end="")
        print()

class Algoritmos:
    def __init__(self, numVertices: int):
        self.digrafoController = Digrafo(numVertices=numVertices)

    def Warshall(self):
        digrafo = self.digrafoController.digrafo
        n = len(digrafo)
        for i in range(0, n):
            digrafo[i][i] = 1
        for k in range(0, n):
            for i in range(0, n):
                if digrafo[i][k] == 1:
                    for j in range (0, n):
                        if digrafo[k][j] == 1:
                            digrafo[i][j] = 1
        return digrafo
    
    def Tarjan(self, vertice: int, stack: list, pre: list, low: list, vis: list):
        global cpre, cont
        digrafo = self.digrafoController.digrafo
        n = len(digrafo)
        cpre +=1
        pre[vertice] = cpre
        low[vertice] = cpre
        vis[vertice] = 1
        stack.insert(0, vertice)
        for j in range(n):
            if digrafo[vertice][j] == 1 and vertice!=j:
                if pre[j] == 0:
                    self.Tarjan(j, stack, pre, low, vis)
                if vis[j] == 1:
                    low[vertice] = min(low[vertice], low[j])
        if pre[vertice] == low[vertice]:
            cont+=1
            print(f'Componente {cont}')
            while(True):
                p = stack.pop(0)
                print(p)
                vis[vertice] = 0
                if p == vertice:
                    break

    def Kosaraju(self, vis: list, ot: list, os: int, comp: int):
        digrafo = self.digrafoController.digrafo
        n = len(digrafo)
        for i in range(n):
            if vis[i] == 0:
                self.OT(i, i, vis, ot, os, n, digrafo)
        for i in range(n):
            if ot[i] != 0:
                comp+=1
                print('Componente', comp)
                self.BPT(i, i, vis, n, digrafo)

    def OT(self, u: int, v:int, vis:list, ot:list, os:int, n:int, digrafo:list):
        vis[v] = 1
        for i in range(n):
            if digrafo[v][i] == 1:
                if vis[i] == 0:
                    self.OT(v, i, vis, ot, os, n)
        ot[os] = v
        os -=1

    def BPT(self, u: int, v:int, vis:list, n:int, digrafo: list):
        vis[v] = 0
        print(v)
        digrafo_transposto = self.digrafoController.transpor(digrafo)
        for i in range(n):
            if digrafo_transposto[v][i] == 1 and vis[i] == 1:
                self.BPT(v, i, vis, n, digrafo)

    def Prim(self, vertice:int):
        digrafo = self.digrafoController.digrafo
        n = len(digrafo)
        caminho = [float('inf')]*n
        pai = [None]*n
        visitados = [False]*n

        pai[vertice] = -1
        caminho[vertice] = 0

        for _ in range(n):
            min = float('inf')
            menor_indice = -1
            
            for i in range(n):
                if caminho[i] < min and visitados[i] is False:
                    min = caminho[i]
                    menor_indice = i
            
            if menor_indice == -1:
                break # Grafo desconexo
            
            w = menor_indice
            visitados[w] = True

            for v in range(n):
                peso = digrafo[w][v]
                if (peso > 0 and 
                    visitados[v] == False and 
                    peso < caminho[v]):
                    
                    caminho[v] = peso
                    pai[v] = w
        return pai, caminho

    def Floyd(self):
        digrafo = self.digrafoController.digrafo
        n = len(digrafo)
        caminhos_minimos = [[None for _ in range (n)] for _ in range (n)]

        for i in range(n):
            for j in range(n):
                if digrafo[i][j] == 0 and i!= j:
                    caminhos_minimos[i][j] = float('inf')
                else:
                    caminhos_minimos[i][j] = digrafo[i][j]
        for k in range (n):
            for i in range(n):
                for j in range(n):
                    caminhos_minimos[i][j] = min(caminhos_minimos[i][j],
                                                 caminhos_minimos[i][k] + caminhos_minimos[k][j])
        return caminhos_minimos

    def Bellman_Ford(self, vertice: int):
        digrafo = self.digrafoController.digrafo
        n = len(digrafo)
        if vertice >= n:
            print('Vértice inexistente no grafo.')
            exit()
        caminhos_minimos = [float('inf')]*n
        ordem = [-1]*n
        caminhos_minimos[vertice] = 0
        
        for k in range(n-1):
            for i in range(n):
                for j in range(n):
                    if (digrafo[i][j] != 0 and 
                        caminhos_minimos[j] > caminhos_minimos[i] + digrafo[i][j]):
                        caminhos_minimos[j] = caminhos_minimos[i] + digrafo[i][j]
                        ordem[j] = i
        for i in range(n):
            for j in range(n):
                if (digrafo[i][j] != 0 and 
                caminhos_minimos[j] > caminhos_minimos[i] + digrafo[i][j]):
                    print('Exite ciclo negativo')
                    return None, None
        print('Não existe ciclo negativo')
        return caminhos_minimos, ordem

def warshal(alg:Algoritmos):
    alg.digrafoController.adicionar_aresta(0, 1, 1)
    alg.digrafoController.adicionar_aresta(0, 7, 1)
    alg.digrafoController.adicionar_aresta(1, 2, 1)
    alg.digrafoController.adicionar_aresta(1, 7, 1)
    alg.digrafoController.adicionar_aresta(2, 3, 1)
    alg.digrafoController.adicionar_aresta(2, 5, 1)
    alg.digrafoController.adicionar_aresta(2, 8, 1)
    alg.digrafoController.adicionar_aresta(3, 4, 1)
    alg.digrafoController.adicionar_aresta(3, 5, 1)
    alg.digrafoController.adicionar_aresta(4, 5, 1)
    alg.digrafoController.adicionar_aresta(5, 6, 1)
    alg.digrafoController.adicionar_aresta(6, 7, 1)
    alg.digrafoController.adicionar_aresta(6, 8, 1)
    alg.digrafoController.adicionar_aresta(7, 8, 1)
    print("\n*** Matriz sem fechamento transitivo ***")
    alg.digrafoController.imprimir_matriz(alg.digrafoController.digrafo)
    warshalGraph = alg.Warshall()
    print("\n*** Matriz com fechamento transitivo ***")
    alg.digrafoController.imprimir_matriz(warshalGraph)

def tarjan(alg:Algoritmos):
    global cpre, cont
    n = len(alg.digrafoController.digrafo)
    pre = [0]*n
    low = [None]*n
    vis = [0]*n
    cpre, cont = 0, 0
    stack = []
    alg.digrafoController.adicionar_aresta(0, 1, 1)
    alg.digrafoController.adicionar_aresta(0, 2, 1)
    alg.digrafoController.adicionar_aresta(1, 2, 1)
    alg.digrafoController.adicionar_aresta(1, 7, 1)
    alg.digrafoController.adicionar_aresta(2, 0, 1)
    alg.digrafoController.adicionar_aresta(2, 3, 1)
    alg.digrafoController.adicionar_aresta(2, 5, 1)
    alg.digrafoController.adicionar_aresta(2, 8, 1)
    alg.digrafoController.adicionar_aresta(3, 4, 1)
    alg.digrafoController.adicionar_aresta(4, 5, 1)
    alg.digrafoController.adicionar_aresta(5, 3, 1)
    alg.digrafoController.adicionar_aresta(6, 7, 1)
    alg.digrafoController.adicionar_aresta(6, 8, 1)
    alg.digrafoController.adicionar_aresta(7, 8, 1)
    print("\n*** Matriz de adjacências ***")
    alg.digrafoController.imprimir_matriz(alg.digrafoController.digrafo)
    for i in range(n):
        if pre[i] == 0:
            alg.Tarjan(i, stack, pre, low, vis)
    print(f'Número de componentes fortemente conexos: {cont}')

def prim(alg:Algoritmos):
    alg.digrafoController.adicionar_aresta(0, 1, 4)
    alg.digrafoController.adicionar_aresta(0, 7, 6)
    alg.digrafoController.adicionar_aresta(1, 2, 2)
    alg.digrafoController.adicionar_aresta(1, 7, 10)
    alg.digrafoController.adicionar_aresta(2, 3, 6)
    alg.digrafoController.adicionar_aresta(2, 5, 8)
    alg.digrafoController.adicionar_aresta(2, 8, 13)
    alg.digrafoController.adicionar_aresta(3, 4, 4)
    alg.digrafoController.adicionar_aresta(3, 5, 7)
    alg.digrafoController.adicionar_aresta(4, 5, 2)
    alg.digrafoController.adicionar_aresta(5, 6, 3)
    alg.digrafoController.adicionar_aresta(6, 7, 9)
    alg.digrafoController.adicionar_aresta(6, 8, 10)
    alg.digrafoController.adicionar_aresta(7, 8, 5)
    print('\n*** Matriz de adjacência ***')
    alg.digrafoController.imprimir_matriz(alg.digrafoController.digrafo)
    pai, caminho = alg.Prim(0)
    alg.digrafoController.imprimir_arvoreGeradoraMinima(pai, caminho)

def floyd(alg:Algoritmos):
    alg.digrafoController.adicionar_aresta(0, 1, 4)
    alg.digrafoController.adicionar_aresta(0, 7, 6)
    alg.digrafoController.adicionar_aresta(1, 2, 2)
    alg.digrafoController.adicionar_aresta(1, 7, 10)
    alg.digrafoController.adicionar_aresta(2, 3, 6)
    alg.digrafoController.adicionar_aresta(2, 5, 8)
    alg.digrafoController.adicionar_aresta(2, 8, 13)
    alg.digrafoController.adicionar_aresta(3, 4, 4)
    alg.digrafoController.adicionar_aresta(3, 5, 7)
    alg.digrafoController.adicionar_aresta(4, 5, 2)
    alg.digrafoController.adicionar_aresta(5, 6, 3)
    alg.digrafoController.adicionar_aresta(6, 7, 9)
    alg.digrafoController.adicionar_aresta(6, 4, 10)
    alg.digrafoController.adicionar_aresta(7, 8, 5)
    print('\n*** Matriz de adjacência ***')
    alg.digrafoController.imprimir_matriz(alg.digrafoController.digrafo)
    caminhos_minimos = alg.Floyd()
    print('\n*** Matriz de adjacência com caminhos mínimos ***')
    alg.digrafoController.imprimir_matriz(caminhos_minimos)

def bellman_ford(alg:Algoritmos, v: int):
    alg.digrafoController.adicionar_aresta(0, 1, 4)
    alg.digrafoController.adicionar_aresta(0, 7, 6)
    alg.digrafoController.adicionar_aresta(1, 2, 2)
    alg.digrafoController.adicionar_aresta(1, 7, 10)
    alg.digrafoController.adicionar_aresta(2, 3, 6)
    alg.digrafoController.adicionar_aresta(2, 4, 8)
    alg.digrafoController.adicionar_aresta(2, 8, 13)
    alg.digrafoController.adicionar_aresta(3, 0, -10)
    alg.digrafoController.adicionar_aresta(3, 5, -7)
    alg.digrafoController.adicionar_aresta(4, 5, 2)
    alg.digrafoController.adicionar_aresta(5, 6, -3)
    alg.digrafoController.adicionar_aresta(6, 7, 9)
    alg.digrafoController.adicionar_aresta(6, 8, 10)
    alg.digrafoController.adicionar_aresta(7, 8, 5)
    alg.digrafoController.adicionar_aresta(8, 3, 2)
    print('\n*** Matriz de adjacência ***')
    alg.digrafoController.imprimir_matriz(alg.digrafoController.digrafo)
    caminhos_minimos, ordem = alg.Bellman_Ford(v)
    if caminhos_minimos is None:
        return
    print(f'\n*** Distâncias mínimas partindo de {v} ***')
    alg.digrafoController.imprimir_caminho(caminhos_minimos)
    print(f'\n*** Vértices precedentes partindo de {v} ***')
    alg.digrafoController.imprimir_caminho(ordem)
    
if __name__ == '__main__':
    n = 9
    alg = Algoritmos(n)
    msg = '[1] - Warshal \n[2] - Tarjan \n[3] - Prim \n[4] - Floyd \n[5] - Bellman-Ford \nElse - exit\n'
    opcao = int(input(msg))
    if opcao == 1: 
        warshal(alg)
    elif opcao == 2:
        tarjan(alg)
    elif opcao == 3: 
        prim(alg)
    elif opcao == 4:
        floyd(alg)
    elif opcao == 5:
        bellman_ford(alg, int(input('Insira o índice do vetor inicial: ')))
    else: 
        exit()
