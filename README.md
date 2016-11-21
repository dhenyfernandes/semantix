# semantix

This file describes how to execute the solution.py and how the solution of the challange was developed. 

To execute the file just do: python solution.py in a terminal. The file 'edges.dat' must be at the same place of the file solution.py. When executed, it will return each node with it's respective closeness centrality. 

To achieve the solution of the challange, I first read the dat file and added each column in a distinct variable. Then, I zipped these variables and write them in csv file, just for facilitate the process of construct the graph. Later, I read the csv file using pandas, created a graph with the NetworkX package and add every unique node to the graph. After, I added the edges between nodes according to the edges.dat file. Then, I drew the graph just for representing the problem in a graphical way. After, I computed the closeness centrality of each node and then sorted the nodes, from the nodes with the highest closeness centrality to those with lowest. Finally, I printed these nodes. 
