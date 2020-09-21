#22p21c0253-ณัฐนันท์ 

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np 

def DFSUtil(nextNodes,path,pathNodeList,node,parent):
  path = path + [node]
  pathNodeList.append(path)
  next_nodes = nextNodes.get(node)
  if next_nodes != None:
    for nextNode in nextNodes[node]:
      if nextNode != parent:
        DFSUtil(nextNodes,path,pathNodeList,nextNode,node)

def DFS(Graph,start):
    nextNodes = {node:list(dict(Graph[node]).keys()) for node in Graph}
    pathNodeList = []
    pathList = []
    DFSUtil(nextNodes,[],pathNodeList,start,-1)
    for paths in pathNodeList:
        if len(paths) > 1:
            for node_idx in range(len(paths)-1):
                if (paths[node_idx],paths[node_idx+1]) not in pathList:
                    pathList.append((paths[node_idx],paths[node_idx+1]))
    return pathList
    			
def createGraph(edges):
    G = nx.Graph()
    for e in edges:
        G.add_edge(e[0],e[1])
    return G

edges = [[0,1],[0,2],[0,3],[3,5],[2,6],[6,7],[3,8],[1,9],[2,10]]

fig, ax = plt.subplots(figsize=(6,6))
G = createGraph(edges)
startNode = 0
dfsPathList = DFS(G,startNode)
pos = nx.spring_layout(G)
def update(num):
    np.random.seed(2)
    nx.draw(G, pos, with_labels = True)
    paths = dfsPathList[:num]
    stack = []
    for path in paths:
        for node in path:
            if node not in stack:
                stack.append(node)
    nx.draw_networkx_edges(G, pos, edgelist = paths, edge_color = 'r')
    ax.set_title("Start DFS at node "+str(startNode)+"\n"+str(stack) , fontweight="bold")
    ax.set_xticks([])
    ax.set_yticks([])

ani = matplotlib.animation.FuncAnimation(fig, update, frames=len(dfsPathList)+1, interval=1000, repeat=True)
ani.save('22p21c0253-ณัฐนันท์_HW2.gif', writer='imagemagick', fps=1)
plt.show()
