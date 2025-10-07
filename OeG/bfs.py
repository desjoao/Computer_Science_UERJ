def BFS(adj: dict, v: int):
    global pre, cpre
    fila = [v]
    while len(fila) > 0:
        v = fila.pop(0)
        if pre[v-1] == 0:
            cpre += 1
            pre[v-1] = cpre
            for w in adj[v]:
                if pre[w-1] == 0:
                    fila.append(w)

if __name__ == "__main__":
    adj = {1: [2, 3], 2: [1, 3], 3:[1, 2, 5, 6], 4: [6], 5: [3, 6], 6: [3, 4, 5]}
    print(adj, "\nEscolha o vértice de partida")
    v = int(input())
    n = len(adj)
    pre = [0]*n
    cpre = 0

    BFS(adj, v)
    for i in range(0, n):
        print(f'v = {i+1}, pre = {pre[i]}')

