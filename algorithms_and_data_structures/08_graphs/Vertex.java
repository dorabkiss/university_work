import java.util.ArrayList;

public class Vertex {
    public String name;
    public ArrayList<Edge> adjlist;

    public Vertex(String _name) {
        name = _name;
        adjlist = new ArrayList<Edge>();
    }
}

