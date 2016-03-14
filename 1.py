import matplotlib.pyplot as plt

import networkx as nx

G = nx.Graph()

# some math labels
labels={}

G.add_node(0, x=0, y=0)
labels[0]=r'$Москва$'
G.add_node(1, x=-5, y=2)
labels[1]=r'$Санкт-Петербург$'
G.add_node(2, x=5, y=0)
labels[2]=r'$Казань$'
G.add_node(3, x=10, y=-2)
labels[3]=r'$Уфа$'
G.add_node(4, x=6, y=-5)
labels[4]=r'$Пермь$'

G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,2)
G.add_edge(4,3)
G.add_edge(0,4)

pos=nx.spring_layout(G) # positions for all nodes

nx.draw_networkx_edges(G,pos,width=1.0,alpha=0.5)

nx.draw_networkx_labels(G,pos,labels,font_size=16)

plt.axis('off')
plt.savefig("labels_and_colors.png") # save as png
plt.show() # display