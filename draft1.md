Draft:
In this tutorial we will be studying the abstract graph data structure. Graphs can be used to solve many real world problems. In our modern world that relies on connections and networks, graphs are used to represent systems of roads, internet connections, and even the list of classes required to graduate.

Objectives:
Learn the about the components of a graph and how they form the graph data structure.
Learn to represent graphs through adjacency matrix and adjacency linkedList
Implement graph and apply graph algorithm to a real interview problem.

Graph component and definitions:

Vertex:
A graph's vertex(a node) is a fundamental part of the graph it can have a name which is called the "key" a vertex might also have additional information which is called the "payload".

Edge:
The edge connects two vertices and represents information about the relationship between them. There are two types of edges one-way(directed) or two-way(undirected).

Weight:
Edges may sometimes have weight showing that there is a cost to go from a vertex to the connected vertex. A weighted graph might represent a road map.

Path:
A path is a sequence of vertices and edges from one vertex to another. A weighted path is the sum of all weighted edges covered between two vertices.

Cycle:
A cycle exists in a Directed graph, it is a path that starts and ends from the same vertex.

![file directory and pom image](./img/digraph.png)
