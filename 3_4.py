# coding: utf-8
# 3 - построить и отобразить остовное дерево методом обхода в ширину (BFS)
# (4 задание ПОЛУЧИЛОСЬ само:)  Выделить и отобразить компоненты связности


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

#--- ф-ция обхода в ширину (использует очередь, идет от вершины v ко всем достижимым в ширину и помечает как посещенные)
def BFS(v): # ф-ция поиска в ширину от узла v
    queue = [v]
    while queue:
        v = queue.pop(0)
        for i in G.neighbors(v): # по всем соседям пройдемся
            if not Visited[i]:
                edge_list.append( (v,i) ) # добавим пройденное ребро для раскраски
                Visited[i] = True # текущую вершину метим как посещенную
                node_list.append(i) # добавим пройденную вершину для раскраски
                queue.append(i)
# end of BFS()

#----- main --------
G = nx.Graph()
labels={} # граф и названия городов заполнятся в LoadGraph()
LoadGraph('map.txt')
COLORS = ['black','red','green','blue','brown','orange'] # чтобы не превысить кол-во цветов, возьмем
                                                         # индекс так i%len(COLORS)

pos=nx.spring_layout(G,weight='weight') # positions for all nodes
nx.draw_networkx_edges(G,pos,alpha=0.5) # нарисуем все дороги черным
nx.draw_networkx_labels(G,pos,labels,font_size=10) # нанесем все названия городов

Visited = {i:False for i in G.nodes()} # все вершины пока не посещенные - при посещении вершины помечаем как True
count = 0
edge_list = [] # список ребер для очередной раскраски. Каждый элемент - кортеж вершин (u,v)
node_list = [] # список вершин для очередной раскраски
while False in Visited.values(): # пока есть непосещенные вершины
    count += 1 # увеличиваем счетчик кол-ва компонент связности
    edge_list = [] # очищаем списки ребер
    node_list = [] # и вершин для очередной компоненты связности

    for v in G.nodes():
        if not Visited[v]: # найдем первый непосещенный узел и от него построим очередной компонент связности
            BFS(v)
            # раскрасим очередной компонент связности своим цветом
            nx.draw_networkx_edges(G, pos, edgelist=edge_list, alpha=0.5,edge_color=COLORS[count%len(COLORS)] )
            nx.draw_networkx_nodes(G, pos, nodelist=node_list, node_color=COLORS[count%len(COLORS)], node_size=200, alpha=0.8)
            break

print('Количество компонент связности:',count)

plt.axis('off')
plt.savefig("BFS.png") # save as png
plt.show() # display









