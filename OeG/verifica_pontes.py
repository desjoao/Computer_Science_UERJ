"""
cpre: contador
pre: vetor com índice de visita
low: vetor com menor índice de um vizinho não pai
"""

def Pontes(p: int, v: int):
    global pre, low, cpre
    cpre +=1
    pre[v] = cpre
    low[v] = pre[v]
    for w in adj[v]:
        if pre[w] == 0:
            Pontes(v, w)
            if low[w] == pre[w]:
                print(v, w, " é ponte")
            low[v] = min(low[v], low[w])
        else:
            if w != p:
                low[v] = min(low[v], pre[w])

if __name__ == "__main__":
    adj = {0: [1, 2], 1: [0, 3, 4], 2: [0, 4], 3:[1, 4, 5], 4:[1, 2, 3, 5], 5:[3, 4]}
    n = len(adj)
    pre = [0]*n
    low = [0]*n
    cpre = 0

    for i in range(0, n):
        if pre[0] == 0:
            Pontes(i, i)
    for i in range(0, n):
        print(f'{i}: pre = {pre[i]}; low = {low[i]}')
