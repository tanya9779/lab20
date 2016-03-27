# coding: utf-8
# найти длины кратчайших путей от заданной вершины ко всем остальным (Алгоритм Дейкстры)

# Для красоты картинки при загрузке сделано weight=int(w/100)
#                   С большими значениями граф некрасивый (уродливый)
#                   с десятичной точкой нагромождений много


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
            G.add_edge(u,v,weight=int(w/100)) # Опытно проверено, что рисунок лучше, когда weight небольшие
            line = f.readline()


# реализация алгоритма Дейкстры из указанной вершины во все остальные
def dejkstra (start):
    shortest_path={vertex:float('+inf') for vertex in G.nodes()} # первоначально (+бесконечность)
    shortest_path[start]=0
    queue=[start]
    p = {} # словарь вида {текущая вершина:предыдущая вершина}  
    while queue:
        current=queue.pop(0)
        for neighbour in G.neighbors(current): # обход всех соседей
            Visited[neighbour] = True
            offering_shortest_path=shortest_path[current]+G.get_edge_data(current, neighbour)['weight']
            if offering_shortest_path < shortest_path[neighbour]:
                # найден путь короче - запоминаем 
                shortest_path[neighbour]=offering_shortest_path
                queue.append(neighbour)
                p[neighbour] = current
    # построим кратч. маршрут до всех доступных из старт
    for i in p.keys():
            edge_list.append( (i, p[i]) ) # путь в обратную сторону, но сейчас это не важно
            if i not in node_list:
                node_list.append(i)  # пройденные вершины тоже покрасим
            if p[i] not in node_list:
                node_list.append(p[i])

#----- main --------
G = nx.Graph()
labels={} # граф и названия городов заполнятся в LoadGraph()
LoadGraph('map.txt')
COLORS = ['black','red','green','blue','brown','orange'] # чтобы не превысить кол-во цветов, возьмем
                                                         # индекс так i%len(COLORS)

# список длин дорог для нанесения на ребра
edge_labels=dict([((u,v,),d['weight'])         # ключем является кортеж из вершин (u,v) а значением длина
             for u,v,d in G.edges(data=True)]) # просим G вернуть ребра со всеми свойствами (data=True)
                                               # возвращается d как список свойств, а нам нужно только длины

Visited = {i:False for i in G.nodes()} # все вершины пока не посещенные - при посещении вершины помечаем как True

# Выведем на экран список всех городов и попросим ввести начальный (словами)
# FIXME проверку на неверный ввод
cityes = ','.join(G.node) 
print ('доступные: '+cityes)
start = input('Начальный город: ')

edge_list = [] # список ребер для раскраски
node_list = [] # список вершин для раскраски

pos=nx.spring_layout(G,weight='weight') # positions for all nodes
nx.draw_networkx_edges(G,pos,alpha=0.5) # нарисуем все дороги черным
nx.draw_networkx_labels(G,pos,labels,font_size=10) # нанесем все названия городов
# нанесем длины ребер
nx.draw_networkx_edge_labels(G,pos,edge_labels,font_size=8)


count = 1 # просто поменяем начальный цвет
dejkstra(start)
# раскрасим каждый посещенный компонент
nx.draw_networkx_edges(G, pos, edgelist=edge_list, alpha=0.5,edge_color=COLORS[count%len(COLORS)] )
nx.draw_networkx_nodes(G, pos, nodelist=node_list, node_color=COLORS[count%len(COLORS)], node_size=200, alpha=0.5)
# start-вершину выделим цветом
nx.draw_networkx_nodes(G, pos, nodelist=[start], node_color=COLORS[len(COLORS)-1], node_size=200, alpha=0.5)



plt.axis('off')
plt.savefig("dejkstra1.png") # save as png
plt.show() # display
