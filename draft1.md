
In this tutorial we will be studying the abstract graph data structure. Graphs can be used to solve many real world problems. In our modern world that relies on connections and networks, graphs are used to represent systems of roads, internet connections, and even the list of classes required to graduate.

What are we aiming to cover?
Learn the about the components of a graph and how they form the graph data structure.
Learn to represent graphs through adjacency matrix and adjacency linkedList
Implement graph and apply two popular graph algorithms Breadth First Search and Depth First Search. And the Stack and Queue data structures associated with each.


What are the parts that comprise a graph?

Vertex:
A graph's vertex(a node) is a fundamental part of the graph it can have a name which is called the "key" a vertex might also have additional information which is called the "payload".

Edge:
The edge connects two vertices and represents information about the relationship between them. There are two types of edges one-way(directed) or two-way(undirected). A graph with one-way edges is a directed graph, and a graph with two-way edges is an undirected graph.

Weight:
Edges may sometimes have weight showing that there is a cost to go from a vertex to the connected vertex. A weighted graph might represent a road map.

Path:
A path is a sequence of vertices and edges from one vertex to another. A weighted path is the sum of all weighted edges covered between two vertices.

Cycle:
A cycle exists in a Directed graph, it is a path that starts and ends from the same vertex.

Below is an example of a weighted directed graph with 6 vertices you can imagine this portraying the flight distances between major cities.

![file directory and pom image](./img/digraph.png)

One way to implement a graph is to use a 2D matrix. The rows and columns represents a vertex in the graph. And values correspond to the weighted edge connecting the two vertices. The simple grid layout makes it easy to see which vertices are associated with which, but a constraint for using the adjacency matrix is that it is cumbersome when applied to large graph structures with many vertices.

![file directory and pom image](./img/adjacencymatx.png)

Real world graphs often times are "loosely connected" meaning their associated adjacency matrix is sparsely populated because the number of edges per vertex is nowhere near every other vertex.
A more space efficient way to implement a loosely connected graph data structure is by using an adjacency List.

![file directory and pom image](./img/adjlist.png)

In an adjacency list a master list of all vertices in the graph is kept and each vertex maintains a list of vertices it's edges are connecting it to. Easy to represent a sparse graph as well as find all links to a particular vertex. 