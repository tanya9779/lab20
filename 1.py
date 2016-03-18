import matplotlib.pyplot as plt
import networkx as nx
import codecs

def LoadGraph(f_name): # из файла прочитаем ребра и их вес
    with codecs.open (f_name, 'r', 'utf-8') as f :
        for line in f.read().split('\n'):
            u,v,w = line.split()
            w = float(w)
            labels[u]='$'+u+'$'
            labels[v]='$'+v+'$'
            G.add_edge(u,v,weight=w/100)


#----- main --------
G = nx.Graph()
labels={}
LoadGraph('map.txt')
pos=nx.spring_layout(G,weight='weight') # positions for all nodes

nx.draw_networkx_edges(G,pos,alpha=0.5)
nx.draw_networkx_labels(G,pos,labels,font_size=10)

plt.axis('off')
plt.savefig("labels_and_colors.png") # save as png
plt.show() # display