"""
Suponha que você queira armazenar um mapa em um computador, de modo que as
informações mantidas sejam os nomes das cidades e quais cidades estão diretamente
ligadas por meio de uma estrada (ou seja, sem cidades intermediárias) e o nome da estrada
que conecta as cidades (por exemplo, BR-040 conectando Rio de Janeiro a Brasília).
Após o armazenamento do mapa no computador, suponha que você queira ser capaz de
consultar quais cidades estão ligadas diretamente a uma cidade dada que esteja no mapa e
quais pares de cidades estão diretamente ligadas por meio de uma estrada dada que
também esteja no mapa.
Neste contexto, qual a estrutura de dados poderia ser utilizada para armazenar o mapa em
questão. Considere essa estrutura de dados e escreva, em pseudocódigo, um algoritmo
para realizar as consultas descritas no parágrafo anterior.
"""

"""
Uma estrutura de dados que poderia ser utilizada para o armazenamento do mapa é
é uma matriz de adjacências. Nessa matriz, Os rótulos das colunas seriam as cidades de
origem e os rótulos das linhas as cidades de destino. Dada a interseção de uma coluna
e de uma linha, se houver uma ligação entre as cidades, a matriz guarda o nome da estrada.
"""

class Mapa:
    def __init__(self):
        self.mapa = [[None,'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Vitória'],
                     ['Rio de Janeiro', None, 'BR-116', 'BR-040', 'BR-101'],
                     ['São Paulo', 'BR-116', None, 'BR-381', None],
                     ['Belo Horizonte', 'BR-040', 'BR-381', None, 'BR-262'],
                     ['Vitória', 'BR-101', None, 'BR-262', None]]


    def consulta_cidades(self, cidade: str) -> list:
        cidades = []
        indice = None
        for vertice in self.mapa[0]:
            if vertice == cidade:
                indice = self.mapa[0].index(vertice)
                break
        if not indice:
            msg = "Cidade não consta no mapa."
            return msg
        for linha in self.mapa:
            if linha[0] == None:
                continue
            if linha[indice]:
                cidades.append(linha[0])
                continue
        return cidades
    
    def consulta_estrada(self, estrada: str) -> tuple:
        cidade = (None,None)
        cont = 0
        for linha in self.mapa:
            if cont == 0:
                cont+=1
                continue
            for vertice in linha:
                if vertice == estrada:
                    indice = linha.index(vertice)
                    cidade = (self.mapa[0][indice], self.mapa[0][cont])
                    return cidade
            cont+=1
        return cidade

if __name__ == "__main__":
    mapa = Mapa()
    cidades = mapa.consulta_cidades(input("Insira uma cidade [Belo Horizonte, Rio de Janeiro, São Paulo, Vitória]:\n"))
    print(cidades)
    estrada = mapa.consulta_estrada(input("Insira uma estrada:\n"))
    print(estrada)