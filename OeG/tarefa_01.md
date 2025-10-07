Questão 3:

Algoritmo:
Ciclo Euleriano(G): #dados grafo G, pilha P, inteiro V:
	Esvazia(P)
	Push(P,v )
	enquanto topo != 0:
		v <- P[topo]
		w <- ProxV(v)
		Push(P, w)
		Eliminar(v, w)
		enquanto topo != 0 e d[P[topo]] = 0:
			w <- Pop(P)
			Imprimir w

Aplicação:
Grafo = [(1, (1, 2), (1, 6)), (2, (2, 3), (2, 1)),
	(3, (3, 4), (3, 2)), (4, (4, 5), (4, 3)),
	(5, (5, 6), (5, 4)), (6, (6, 1), (6, 5))] #3-upla com vértice e suas arestas
v = 1
P = []
Push(P, 1): P = [1]
enquanto topo != 0:
	1ª iteração
	v = P[topo] = 1
	w = ProxV(v) = 2
	Push(P, w): P [1, 2]
	Eliminar (v, w)
	# Grafo = [(1,(None, None), (1, 6)), (2, (2, 3), (None, None)),
        # (3, (3, 4), (3, 2)), (4, (4, 5), (4, 3)),
        # (5, (5, 6), (5, 4)), (6, (6, 1), (6, 5))]
	topo !=0? sim; d[P[topo]] == 0? não
	
	2ª iteração
	v = P[topo] = 2
	w = ProxV(v) = 3
	Push(P, w): P = [1, 2, 3]
	Eliminar (v, w)
	# Grafo = [(1,(None, None), (1, 6)), (2, (None, None), (None, None)),
	# (3, (3, 4), (None, None)), (4, (4, 5), (4, 3)),
	# (5, (5, 6), (5, 4)), (6, (6, 1), (6, 5))]
	topo != 0? sim; d[P[topo]] == 0? não

	3ª iteração
	v = P[topo] = 3
	w = ProxV(v) = 4
	Push(P, w): P = [1, 2, 3, 4]
	Eliminar (v, w)
	# Grafo = [(1,(None, None), (1, 6)), (2, (None, None), (None, None)),
	# (3, (None, None), (None, None)), (4, (4, 5), (None, None)),
	# (5, (5, 6), (5, 4)), (6, (6, 1), (6, 5))]
	topo != 0? sim; d[P[topo]] == 0? não

	4ª iteração
	v = P[topo] = 4
	w = ProxV(v) = 5
	Push (P, w): P = [1, 2, 3, 4, 5]
	Eliminar (v, w)
	# Grafo = [(1,(None, None), (1, 6)), (2, (None, None), (None, None)),
	# (3, (None, None), (None, None)), (4, (None, None), (None, None)),
	# (5, (5, 6), (None, None)), (6, (6, 1), (6, 5))]
	topo != 0? sim; d[P[topo]] == 0? não

	5ª iteração
	v = P[topo] = 5
	w = ProxV(v) = 6
	Push (P, w): P = [1, 2, 3, 4, 5, 6]
	Eliminar(v, w)
	# Grafo = [(1,(None, None), (1, 6)), (2, (None, None), (None, None)),                                                                                          
        # (3, (None, None), (None, None)), (4, (None, None), (None, None)),
        # (5, (None, None), (None, None)), (6, (6, 1), (None, None))]
	topo != 0? sim; d[P[topo]] == 0? não

	6ª iteração
	v = P[topo] = 6
	w = ProxV[topo] = 1
	Push(P, w): P = [1, 2, 3, 4, 5, 6, 1]
	Eliminar(v, w)
	# Grafo = [(1,(None, None), (None, None)), (2, (None, None), (None, None)),
	# (3, (None, None), (None, None)), (4, (None, None), (None, None)),
	# (5, (None, None), (None, None)), (6, (None, None), (None, None))]
	topo != 0? sim; d[P[topo]] == 0? sim

	enquanto topo != 0 e d[P[topo]] == 0
	1ª iteração
	w = Pop(P): P = [1, 2, 3, 4, 5, 6]
	print w -> 1
	topo == 6; d[P[topo]] == 0

	2ª iteração
	w = Pop(P): P = [1, 2, 3, 4, 5]
	print w -> 6
	topo == 5; d[P[topo]] == 0

	3ª iteração
	w = Pop(P): P = [1, 2, 3, 4]
	print w -> 5
	topo == 4; d[P[topo]] == 0

	4ª iteração
	w = Pop(P): P [1, 2, 3]
	print w -> 4
	topo == 3; d[P[topo]] == 0

	5ª iteração
	w = Pop(P): P = [1, 2]
	print w -> 3
	topo == 2; d[P[topo]] == 0

	6ª iteração
	w = Pop(P): P = [1]
	print w -> 2
	topo == 1; d[P[topo]] == 0

	7ª iteração
	w = Pop(P): P = []
	print w -> 1
	topo == None; d[P[topo]] == None

	FIM


Questão 4:

Algoritmo de Busca em Profundidade:
BP(p,v):
	cpre = cpre+1
	pre[v] = cpre
	w = A[v]
	enquanto w != nulo:
		se pre[w.v] == 0:
			BP(v, w.v)
		w = w.prox

para i no intervalo de 1 até 6:
	pre[i] = 0

cpre = 0
para i no intervalor de 1 até 6:
	se pre[i] = 0:
		BP(i, i)
	

Aplicação:
Grafo = [(1, [2, 6]), (2, [3, 1]), (3, [4, 2]),
	(4, [5, 3]), (5, [6, 4]), (6, [1, 5])] #2-upla composto por vértice e suas adjacências
para i no intervalo de 1 até 6:
	pre[i] = 0
pre = [0, 0, 0, 0, 0, 0]
cpre = 0
para i no intervalo de 1 até 6:
	1ª iteração:
	pre[1] == 0? sim
	vá para BP(1, 1)

	BP(1,1):
		cpre = 1
		pre[1] = 1: pre = [1, 0, 0, 0, 0, 0]
		w = A[1] = [2, 6]
		pre[2] == 0? sim
		vá para BP(1, 2)
		
		BP(1, 2):
			cpre = 2
			pre[2] = 2: pre = [1, 2, 0, 0, 0, 0] 
			w = A[2] = [3, 1]
			pre[3] == 0? sim
			vá para BP(2, 3)

			BP(2, 3):
				cpre = 3
				pre[3] = 3: pre = [1, 2, 3, 0, 0, 0]
				w = A[3] = [4, 2]
				pre[4] == 0? sim
				vá para BP(3, 4)

				BP(3, 4):
					cpre = 4
					pre[4] = 4: pre = [1, 2, 3, 4, 0, 0]
					w = A[4] = [5, 3]
					pre[5] == 0? sim
					vá para BP(4, 5)

					BP(4, 5):
						cpre = 5
						pre[5] = 5: pre = [1, 2, 3, 4, 5, 0]
						w = A[5] = [6, 4]
						pre[6] == 0? sim
						vá pára BP(5, 6)

						BP(5, 6):
							cpre = 6
							pre[6] = 6: pre = [1, 2, 3, 4, 5, 6]
							w = A[6] = [1, 5]
							pre[1] == 0? não
							pre[5] == 0? não
							w.prox == nulo
							retorna para BP(4, 5)
						
						pre[4] == 0? não
						retorna para BP(3, 5)
					
					pre[3] == 0? não
					retorna para BP(2, 3)
				
				pre[2] == 0? não
				retorna para BP(1, 2)
			
			pre[1] == 0? não
			retorna para BP(1, 1)

		pre[6] == 0? não
		
	pre[2] == 0? não
	pre[3] == 0? não
	pre[4] == 0? não
	pre[5] == 0? não
	pre[6] == 0? não

	FIM (pre = [1, 2, 3, 4, 5, 6])


Questão 5:
Algoritmo:

Criação(n):
	para i de 1 até n:
		pai[i] = i

Busca(p):
	se pai[p] != p:
		pai[p] = Busca(pai[p])
	retornar pai[p]

Uniao(p, q):
	Pp = Busca(p)
	Pq = Busca(q)
	se (Pp < Pq):
		pai[Pq] = Pp
	senao:
		pai[Pp] = Pq

Componentes():
	ler(n, m)
	Criação(n)
	para i de 1 até m:
		ler(u, v)
		Uniao(u, v)
	c = 0
	para i de 1 até n
		se pai[i] = i:
			c = c+1
	se c = 1:
		escrever("Conexo")
	senao:
		escrever("Desconexo")


Aplicação

Componentes():
	ler (n, m)
	-> n = [1, 2, 3, 4, 5, 6, 7, 8]; m = [(1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (5, 7), (5, 8), (6, 8), (7, 8)]

	Criação(n)
	pai = [1, 2, 3, 4, 5, 6, 7, 8]

	para i de 1 até 9:
		1ª iteração
		ler (u, v) -> u = 1; v = 3
		Uniao(1, 3):
			P1 = Busca(1) = 1
			P3 = Busca(2) = 3
			P1 < P2? sim
			pai[P2] = P1 -> pai = [1, 2, 1, 4, 5, 6, 7, 8]

		2ª iteração
		ler (u, v) -> u = 1; v = 4
		Uniao(1, 4):
			P1 = Busca(1) = 1
			P4 = Busca(4) = 4
			P1 < P4? sim
			pai[P4] = P1 -> pai = [1, 2, 1, 1, 5, 6, 7, 8]
		
		3ª iteração
		ler (u, v) -> u = 2; v = 3
		Uniao(2, 3):
			P2 = Busca(2) = 2
			P3 = Busca(3) = 1
			P2 < P3? nao
			pai[P2] = P3 -> pai = [1, 1, 1, 1, 5, 6, 7, 8]

		4ª iteração
		ler (u, v) -> u = 2; v = 4
		Uniao(2, 4):
			P2 = Busca(P2) = 1
			P4 = Busca(P4) = 1
			P2 < P4? nao
			pai[P2] = P4 -> pai [1, 1, 1, 1, 5, 6, 7, 8]
		
		5ª iteração
		ler (u, v) -> u = 3; v = 4
		Uniao(3, 4):
			P3 = Busca(P3) = 1
			P4 = Busca(P4) = 1
			P3 < P4? nao
			pai[P3] = P4 -> pai[1, 1, 1, 1, 5, 6, 7, 8]

		6ª iteração
		ler (u, v) -> u = 5; v = 7
		Uniao(5, 7):
			P5 = Busca(P5) = 5
			P7 = Busca(P7) = 7
			P5 < P7? sim
			pai[P7] = P5 -> pai = [1, 1, 1, 1, 5, 6, 5, 8]

		7ª iteração
		ler(u, v) -> u = 5; v = 8
		Uniao(5, 8)
			P5 = Busca(P5) = 5
			P8 = Busca(P8) = 8
			P5 < P8? sim
			pai[P8] = P5 -> pai = [1, 1, 1, 1, 5, 6, 5, 5]
		
		8ª iteração
		ler(u, v) -> u = 6; v = 8
		Uniao(6, 8):
			P6 = Busca(P6) = 6
			P8 = Busca(P8) = 5
			P6 < P8? nao
			pai[P6] = P8 -> pai = [1, 1, 1, 1, 5, 5, 5, 5]

		9ª iteração
		ler(u, v) -> u = 7; v = 8
		Uniao(7, 8):
			P7 = Busca(P7) = 5
			P8 = Busca(P8) = 5
			P7 < P8? nao
			pai[P7] = P8 -> pai = [1, 1, 1, 1, 5, 5, 5, 5]
		
	c = 0
	para i de 1 até 8:
		1ª iteração
		pai[1] = 1? sim
			c = 0 + 1 = 1
		
		2ª iteração
		pai[2] = 2? nao

		3ª iteração
		pai[3] = 3? nao

		4ª iteração
		pai[4] = 4? nao

		5ª iteração
		pai[5] = 5? sim
			c = 1 + 1 = 2
		
		6ª iteração
		pai[6] = 6? nao

		7ª iteração
		pai[7] = 7? nao

		8ª iteração
		pai[8] = 8? nao

	c = 1? nao
	
	impressão: "Desconexo"
	FIM
