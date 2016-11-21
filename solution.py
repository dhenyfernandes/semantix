from __future__ import division
import numpy as np
import csv
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import operator

myarray = np.fromfile('edges.dat',dtype=int,sep=' ')


edge1 = []
edge2 = []
for i in xrange(0,len(myarray),2):
    edge1.append(myarray[i])
    edge2.append(myarray[i+1])
with open('edges.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(zip(edge1,edge2))

df = pd.read_csv('edges.csv',delimiter=',',names=['Node1','Node2'])

G=nx.Graph()
[G.add_node(x) for x in df.Node1.unique()]
[G.add_edge(y,z) for y,z in zip(df.Node1,df.Node2)]
nx.draw(G,with_labels=True)
plt.savefig("edges_problem.png")
print 'Showing the graph'
plt.show()


distancia=[]
centrality = {}
for a in df.Node1.unique():
    for b in df.Node2.unique():
        distancia.append(len(nx.shortest_path(G, a, b)) - 1)
    ct = (len(df.Node1.unique())-1)/sum(distancia)
    centrality[a] = ct
    distancia = []


rank = sorted(centrality.iteritems(), key=operator.itemgetter(1),reverse=True)

for value in rank:
    print 'The node ' + str(value[0]) + ' has the closeness centrality equal to ' + str(value[1])

