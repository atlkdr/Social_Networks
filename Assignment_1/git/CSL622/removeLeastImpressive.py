'''
Question: Find the number of fake edges required to add to the least Impressive to remove him from that position.

Group members:
Piyush Pilaniya(2016csb1049)
Prinshu Kumar(2016csb1051)
Vaibhav Chopra(2016eeb1104)
'''
import networkx as nx
#import matplotlib.pyplot as plt
G = nx.read_edgelist(r"/home/prinshu/Downloads/pagerank.txt",create_using=nx.DiGraph(), nodetype = int)
G.remove_node(35)
G.remove_node(40)
#nx.draw(G,with_labels=1)
y = []
for i in range(33):
      if i == 17:
         continue
      p = G.in_edges(i+1)
      x = len(p)
      y.append(x)
p = G.in_edges(100)
y.append(len(p))

print (y)
y.sort()
print (y)
print ("Required edges : ")
print (y[1]-y[0])