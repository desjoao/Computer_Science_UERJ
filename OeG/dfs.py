def DFS(p: int, v: int):
    global pre, cpre
    cpre +=1
    pre[v-1] = cpre
    for w in adj[v]:
        if pre[w-1] == 0:
            DFS(v, w)

if __name__ == "__main__":
    adj = {
            1: [2, 3],
            2: [1, 4],
            3: [1],
            4: [2, 5],
            5: [4]
            }
    cpre = 0
    n = len(adj)
    pre = [0]*n
    for i in range (0, n):
        if pre[i] == 0:
            DFS(i+1, i+1)
    for i in range(0, n):
        print(f"v: {i+1} | pre: {pre[i]}")

