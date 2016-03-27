# coding: utf-8
# Научиться считывать и отображать граф городов, 
# в том числе с выделением отдельных вершин или некоторого пути (ЭТО В ДРУГИХ ПРИМЕРАХ СДЕЛАНО)

import matplotlib.pyplot as plt
import networkx as nx

def LoadGraph(f_name): # из файла прочитаем ребра и их вес
    with open (f_name, 'r') as f :
        line = f.readline()
        while line:
            u,v,w = line.split()
            w = float(w)
            labels[u]='$'+u+'$'  # значки $ в начале и в конце слов нужны (проверено!)
            labels[v]='$'+v+'$'
            G.add_edge(u,v,weight=w/100) # Опытно проверено, что рисунок лучше, когда weight небольшие
            line = f.readline()


#----- main --------
G = nx.Graph() # граф и названия городов заполнятся в LoadGraph()
labels={} # создаем словарь для всех наименований вершин (города) вида {"Яблочный":"$Яблочный$"}
LoadGraph('map.txt')
pos=nx.spring_layout(G,weight='weight') # positions for all nodes

nx.draw_networkx_edges(G,pos,alpha=0.5)             # нарисуем все дороги черным
nx.draw_networkx_labels(G,pos,labels,font_size=10)  # нанесем все названия городов

plt.axis('off')
plt.savefig("labels_and_colors.png") # save as png
plt.show() # display