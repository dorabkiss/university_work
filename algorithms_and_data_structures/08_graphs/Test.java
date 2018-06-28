import static java.util.Arrays.asList;

import java.util.ArrayList;
import java.util.List;
class Test{
    public static void main(String[] args){

        Graph g = new Graph();
        g.addVertex("F");
        g.addVertex("H");
        g.addVertex("I");
        g.addVertex("J");
        g.addVertex("K");


        g.addEdge("F", "H", 1);
        g.addEdge("J", "I", 2);
        g.addEdge("H", "I", 3);
        g.addEdge("J", "J", 4);
        g.addEdge("F", "J", 5);
        g.addEdge("F", "I", 6);
        g.addEdge("H", "H", 7);
       // g.addEdge("K", "H", 8);
       // g.addEdge("K", "I", 9);
        g.addEdge("F", "K", 10);
        g.addEdge("F", "F", 11);
        g.addEdge("I", "I", 12);
        g.addEdge("J", "H", 13);
        g.addEdge("J", "K", 14);
        g.addEdge("K", "K", 15);
        //Graph h = g.MST();
       // for (Vertex v : h.vlist) {
       //    System.out.println(v.name);
       // }
        //Vertex x = g.getLowestDistanceVertex(g.getVertex("J"));

      //  System.out.println(x.name);

        Graph x = g.SP("K", "I");
        for (Vertex v : x.vlist) {
            System.out.println(v.name);
        }

        System.out.println(x.vlist.get(0).adjlist.get(0).weight);
        System.out.println(x.vlist.get(0).adjlist.get(0).from.name);
        System.out.println(x.vlist.get(0).adjlist.get(0).to.name);
        System.out.println(x.vlist.get(1).adjlist.get(0).weight);
        System.out.println(x.vlist.get(1).adjlist.get(0).from.name);
        System.out.println(x.vlist.get(1).adjlist.get(0).to.name);

        System.out.println(x.vlist.get(2).adjlist.get(0).weight);
        System.out.println(x.vlist.get(2).adjlist.get(0).from.name);
        System.out.println(x.vlist.get(2).adjlist.get(0).to.name);

        System.out.println("x elist size: " + x.elist.size());
        for (Edge e : x.elist) {
            System.out.println(e.from.name + e.to.name + e.weight);
        }

        System.out.println("edges: ");
        Edge e1 = x.getEdge("K", "F");
        Edge e2 = x.getEdge("F", "K");
        System.out.println(e1.from.name);
        System.out.println(e1.to.name);
        System.out.println(e2.from.name);
        System.out.println(e2.to.name);

        //System.out.println(g.SPCost("K", "K"));

// 53837 --> 26 33497281 --> 37
        // shortest path between A and B = 26
        // cost of the minimum spanning tree = 37

      /*  g.addVertex("A");
        g.addVertex("B");
        g.addVertex("C");
        g.addVertex("D");

        g.addEdge("A", "B", 30);
        g.addEdge("B", "C", 16);
        g.addEdge("C", "D", 11);
        g.addEdge("A", "D", 40);
        g.addEdge("B", "D", 50);
        g.addEdge("A", "C", 10);
*/

    }
}
