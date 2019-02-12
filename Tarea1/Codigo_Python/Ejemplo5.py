# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 23:04:57 2019

@author: maari
"""

import matplotlib.pyplot as plt
import networkx as nx

G=nx.DiGraph()

pos={0:(0,1),1:(1,0),2:(2,1),3:(1.6,2),4:(.5,2)}
labels={0:'1',1:'2',2:'3',3:'4',4:'5'}
Conexion=[(0,1),(1,2),(2,3),(2,4),(3,4),(4,0)]

nx.draw_networkx_nodes(G,pos,node_size=300,nodelist=range(5),node_color='r')
nx.draw_networkx_edges(G,pos,alpha=1,edgelist=Conexion,width=1)
nx.draw_networkx_labels(G,pos,labels,font_size=12)
plt.axis('off')

plt.savefig("Ejemplo5.eps")
plt.show()