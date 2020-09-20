import networkx as nx
import matplotlib.pyplot as plt
 


#utility fucntion used by DFS which does recursive depth first search 
def DFSUtil(G, v, visited, sl): 
	visited[v] = True
	sl.append(v) 
	for i in G[v]:
		if visited[i] == False:
			DFSUtil(G, i, visited, sl)
	return sl
 


#DFS traversal 
def DFS(G, source): 
    visited = [False]*(len(G.nodes()))
    sl = []		#a list that stores dfs forest starting with source node
    dfs_stk = [] #A nested list that stores all the DFS Forest's
    dfs_stk.append(DFSUtil(G, source, visited, sl))
    for i in range(len(G.nodes())):
        if visited[i] == False:
            sl = []
            dfs_stk.append(DFSUtil(G, i, visited, sl))
        return dfs_stk

#takes input from the file and creates a weighted graph
def CreateGraph():
    G = nx.Graph()
    source = 0
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 3)
    G.add_edge(3, 4)
    G.add_edge(3, 5)
    G.add_edge(2, 5)
    return G, source


#marks all edges traversed through DFS with red
def DrawDFSPath(G, dfs_stk):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True)  #with_labels=true is to show the node number in the output graph
	for i in dfs_stk:
		#if there is more than one node in the dfs-forest, then print the corresponding edges
		if len(i) > 1:
			for j in i[ :(len(i)-1)]:
				if i[i.index(j)+1] in G[j]:
					nx.draw_networkx_edges(G, pos, edgelist = [(j,i[i.index(j)+1])], width = 2.5, alpha = 0.6, edge_color = 'r')
				else:
					#if in case the path was reversed because all the possible neighbours were visited, we need to find the adj node to it.
					for k in i[1::-1]: 
						if k in G[j]:
							nx.draw_networkx_edges(G, pos, edgelist = [(j,k)], width = 2.5, alpha = 0.6, edge_color = 'r')
							break



#main function
if __name__ == "__main__":
	G, source = CreateGraph()
	dfs_stk = DFS(G, source)
	DrawDFSPath(G, dfs_stk)
	plt.show()