# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 22:49:39 2019

@author: maari
"""

import matplotlib.pyplot as plt
import networkx as nx

G=nx.DiGraph()

pos={0:(1.75,3),1:(.5,2),2:(3,2),3:(0,1),4:(1,1),5:(2.5,1),6:(3.5,1)}
labels={0:'1',1:'2',2:'3',3:'4',4:'5',5:'6',6:'7'}
Conexion=[(0,1),(0,2),(1,3),(1,4),(2,5),(2,6)]

nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=range(7),node_color='r')
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=Conexion,width=1)
nx.draw_networkx_labels(G,pos,labels,font_size=12)
plt.axis('off')

plt.savefig("Ejemplo4.eps")
plt.show()