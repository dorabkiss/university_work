import java.util.ArrayList;

public class Graph {
    public ArrayList<Vertex> vlist;
    public ArrayList<Edge> elist;

    public Graph() {
        vlist = new ArrayList<Vertex>();
        elist = new ArrayList<Edge>();
    }

    public void addVertex(String name) {
        Vertex v = new Vertex(name);
        vlist.add(v);
    }

    public Vertex getVertex(String name) {
        if (vlist.size() < 1) {
            return null;
        }
        for (Vertex v : vlist) {
            if (v.name == name) { // find vertex in ArrayList by property(name)
                return v;
            }
        }
        return null;
    }

    public void addEdge(String from, String to, int weight) {
        Vertex vertex1 = getVertex(from);
        Vertex vertex2 = getVertex(to);
        if (vertex1 == null || vertex2 == null || from == to) {
            return;
        }

        Edge e = new Edge(vertex1, vertex2, weight);
        Edge e2 = new Edge(vertex2, vertex1, weight);

        vertex1.adjlist.add(e);
        vertex2.adjlist.add(e2);
    }


    public Edge getEdge(String from, String to) {
        Vertex vertex1 = getVertex(from);
        Vertex vertex2 = getVertex(to);
        if (vertex1 == null || vertex2 == null || vertex1.adjlist.size() < 1 || vertex2.adjlist.size() < 1) {
            return null;
        }
        for (Edge e : vertex1.adjlist) {
            if (e.to.name == vertex2.name && e.from.name == vertex1.name || e.from.name == vertex2.name && e.to.name == vertex1.name) { // find edge in ArrayList by property(name)
                return e;
            }
        }
        return null;

    }


    public int MSTCost() {
        int cost = 0;
        Graph mst = new Graph(); // this will become our final mst
        if (vlist.size() == 0) return cost;

        mst.addVertex(vlist.get(0).name);

        ArrayList<Edge> alledges = new ArrayList<Edge>();
        for (Vertex vert : vlist) {
            for (Edge edg : vert.adjlist) {
                alledges.add(edg);
            }
        }

        while (mst.vlist.size() < vlist.size()) {
            Vertex newV = null;
            Edge newE = null;
            int w = Integer.MAX_VALUE;
            String n = "";
            for (Edge e : alledges) {
                if (mst.getVertex(e.to.name) == null && mst.getVertex(e.from.name) != null) {
                    if (e.weight < w) {
                        w = e.weight;
                        newE = e;
                        newV = e.to;
                        n = newV.name;
                    }
                }
            }
            mst.addVertex(n);
            mst.addEdge(newE.from.name, n, w);
            cost += w;
        }
        return cost;
    }


    public Graph MST() {
        Graph mst = new Graph(); // this will become our final mst
        if (vlist.size() == 0) return mst;

        mst.addVertex(vlist.get(0).name);

        ArrayList<Edge> alledges = new ArrayList<Edge>();
        for (Vertex vert : vlist) {
            for (Edge edg : vert.adjlist) {
                alledges.add(edg);
            }
        }

        while (mst.vlist.size() < vlist.size()) {
            Vertex newV = null;
            Edge newE = null;
            int w = Integer.MAX_VALUE;
            String n = "";
            for (Edge e : alledges) {
                if (mst.getVertex(e.to.name) == null && mst.getVertex(e.from.name) != null) {
                    if (e.weight < w) {
                        w = e.weight;
                        newE = e;
                        newV = e.to;
                        n = newV.name;
                    }
                }
            }
            mst.addVertex(n);
            mst.addEdge(newE.from.name, n, w);
        }
        return mst;
    }


    public int SPCost(String from, String to) {
        PathVertex current = GetRoute(from, to);
        if (current == null)
            return 0;

        return current.g;
    }

    public Graph SP(String from, String to) {
        PathVertex current = GetRoute(from, to);
        if (current == null)
            return new Graph();

        Graph shortestPath = new Graph();

        Edge e = null;
        while (current != null) {
            Vertex map = new Vertex(current.vertex.name);
            if (e != null) {
                map.adjlist.add(e);
            }

            shortestPath.vlist.add(0, map);

            if (current.edge != null) {
                e = new Edge(current.edge.from, current.edge.to, current.edge.weight);
                shortestPath.elist.add(e);
            } else {
                e = null;
            }

            current = current.previous;
        }
        int k = shortestPath.elist.size();
        for (int i = 0; i < k; i++) {
            Edge e1 = new Edge(shortestPath.elist.get(i).to, shortestPath.elist.get(i).from, shortestPath.elist.get(i).weight);
            Vertex v2 = shortestPath.elist.get(i).to;
            shortestPath.getVertex(v2.name).adjlist.add(e1);
        }


        return shortestPath;
    }

    public PathVertex GetRoute(String from, String to) {
        ArrayList<PathVertex> open = new ArrayList<PathVertex>();
        ArrayList<PathVertex> closed = new ArrayList<PathVertex>();

        Vertex firstVertex = getVertex(from);
        PathVertex first = new PathVertex();
        first.vertex = firstVertex;
        open.add(first);

        while (open.size() > 0) {
            PathVertex current = open.remove(0);

            if (current.vertex.name == to) {
                return current;
            }

            boolean alreadyVisited = false;
            for (PathVertex visited : closed) {
                if (visited.vertex.name == current.vertex.name) {
                    alreadyVisited = true;
                    break;
                }
            }

            if (alreadyVisited) {
                continue;
            }

            closed.add(current);

            for (Edge e : current.vertex.adjlist) {
                PathVertex next = new PathVertex();
                next.vertex = e.to;
                next.previous = current;
                next.edge = e;
                next.g = current.g + e.weight;

                boolean found = false;
                for (int i = 0; i < open.size(); ++i) {
                    PathVertex v = open.get(i);
                    if (v.g > next.g) {
                        open.add(i, next);
                        found = true;
                        break;
                    }
                }

                if (!found) {
                    open.add(next);
                }
            }
        }

        return null;
    }

    class PathVertex {
        public PathVertex previous;
        public Vertex vertex;
        public Edge edge;
        public int g;

        public PathVertex() {

        }
    }

}
