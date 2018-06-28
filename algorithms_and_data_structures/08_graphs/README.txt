1 Graphs
This lab requires you to implement undirected graphs, along with algorithms that work on 
those undirected graphs.

1.1 Implementing the class
The first part of the lab is to flesh out implementations of the basic operations on graphs:
• addVertex() and getVertex(), which add and retrieve vertices from a graph by name;
• addEdge() and getEdge(), which respectively create an edge in a graph (with a given weight)
and retrieve an edge from a graph. Your implementations of these two methods must consistently
implement undirected graph semantics;
Implement these methods, and verify that the tests provided for these basic operations pass.

1.2 Minimum spanning trees
You must implement two methods regarding minimum spanning trees; when doing so, you are 
permitted to assume that the graph is connected and that the edge weights are all distinct:
• MSTCost(), which should return the total cost of the minimum spanning tree of the graph;
• MST(), which should return a fresh Graph that represents the minimum spanning tree, but 
shares no structure (vertices or edges) with the original graph.

Implement these and verify that the corresponding tests pass.

1.3 Shortest path
You must implement methods to compute the cost and the edge sequence of the shortest path 
between two vertices:
• SPCost(String from, String to) which should return the total cost of the shortest path 
between from and to;
• SP(String from, String to) which should return a fresh Graph that represents the shortest 
path, but shares no structure (vertices or edges) with the original graph.