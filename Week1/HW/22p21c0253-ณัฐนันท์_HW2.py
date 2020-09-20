#22p21c0253-ณัฐนันท์ 

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation

def DFSUtil(G, v, visited, sl): 
	visited[v] = True
	sl.append(v) 
	for i in G[v]:
		if visited[i] == False:
			DFSUtil(G, i, visited, sl)
	return sl
 
def DFS(G, source): 
    visited = [False]*(len(G.nodes()))
    sl = []
    dfs_stack = []
    dfs_stack.append(DFSUtil(G, source, visited, sl))
    for i in range(len(G.nodes())):
        if visited[i] == False:
            sl = []
            dfs_stk.append(DFSUtil(G, i, visited, sl))
    return dfs_stack
			
def createGraph():
    G = nx.Graph()
    source = 1
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 3)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(2, 5)
    return G, source

fig, ax = plt.subplots(figsize=(6,6))
G, source = createGraph()
dfs_stk = DFS(G, source)

def createEdgeList(dfs_stk,G):
    edgelist = []
    for i in dfs_stk:
        for j in i[ :(len(i)-1)]:
            edge = ()
            if i[i.index(j)+1] in G[j]:
                edge = (j,i[i.index(j)+1])
                edgelist.append(edge)
            else:
                for k in i[1::-1]:
                    if k in G[j]:
                        edge = (j,k)
                        edgelist.append(edge)
                        break
            
    return edgelist

edgelist = createEdgeList(dfs_stk,G)
pos = nx.spring_layout(G)
print(dfs_stk)
print(edgelist)
def update(num):
    nx.draw(G, pos, with_labels = True)
    counter = num % len(edgelist) + 1
    paths = edgelist[:counter]
    stack = []
    for path in paths:
        for node in path:
            if node not in stack:
                stack.append(node)
    print(stack)
    nx.draw_networkx_edges(G, pos, edgelist = paths, edge_color = 'r')
    ax.set_title("Start DFS at node 1" , fontweight="bold")
    ax.set_title(str(stack), fontweight="bold")
    ax.set_xticks([])
    ax.set_yticks([])

ani = matplotlib.animation.FuncAnimation(fig, update, frames=6, interval=1000, repeat=True)
ani.save('animation.gif', writer='imagemagick', fps=1)
plt.show()


