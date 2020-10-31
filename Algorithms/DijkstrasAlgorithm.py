import timeit
import networkx as nx
import random
import matplotlib.pyplot as plt


def dijkstra(graph, source, target):
    try:
        return [p for p in nx.all_shortest_paths(graph, source, target)]
    except:
        return []


# g1 = nx.gnp_random_graph(random.randint(15, 50), 0.6)
# g2 = nx.gnp_random_graph(random.randint(15, 50), 0.6)
# g3 = nx.gnp_random_graph(random.randint(15, 50), 0.6)
# g4 = nx.gnp_random_graph(random.randint(15, 50), 0.6)
# g5 = nx.gnp_random_graph(random.randint(15, 50), 0.6)
# g6 = nx.gnp_random_graph(random.randint(15, 50), 0.6)
# g7 = nx.gnp_random_graph(random.randint(15, 50), 0.6)
# g8 = nx.gnp_random_graph(random.randint(15, 50), 0.6)
# g9 = nx.gnp_random_graph(random.randint(15, 50), 0.6)
# g10 = nx.gnp_random_graph(random.randint(15, 50), 0.6)

g1 = nx.gnm_random_graph(15, 8)
g2 = nx.gnm_random_graph(20, 10)
g3 = nx.gnm_random_graph(25, 12)
g4 = nx.gnm_random_graph(30, 14)
g5 = nx.gnm_random_graph(35, 16)
g6 = nx.gnm_random_graph(40, 18)
g7 = nx.gnm_random_graph(45, 20)
g8 = nx.gnm_random_graph(50, 22)
g9 = nx.gnm_random_graph(55, 24)
g10 = nx.gnm_random_graph(60, 26)


graphs = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]
g_timer = []

for i in graphs:
    start = timeit.default_timer()
    dijkstra(g1, 0, 10)
    stop = timeit.default_timer()
    g_timer.append(stop - start)

graphLables = ['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 'g10']
plt.plot(graphLables, g_timer)
plt.ylabel('Time')
plt.xlabel('Graphs')
plt.show()
# ran on Jupyter notebook because matplotlib wouldn't work
