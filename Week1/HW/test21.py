import networkx as nx
import random
import matplotlib.animation as animation
import matplotlib.pyplot as plt

# Graph Initialization
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5])
G.add_edges_from([(1,2), (2,3), (2,5), (1,5), (2,5)])
nx.draw(G)

# animation function for having node labelled 1 to move to random positions
# If you are moving nodes it's labels and the corresponding edges will also 
# move to their new positions

def animate_one(i):
    nx_animation.set_node_position(G, node=1, position=(random.uniform(0,1), random.uniform(0,1)))

# calling Matplotlib's FuncAnimation
anim = animation.FuncAnimation(plt.gcf(), animate)