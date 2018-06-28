public class StackQueue {
    private static Stack s;
    private static Queue q;
    public static void main(String[] args) {
	prepare();
	System.out.print(q.dequeue());
	System.out.print(s.pop());
	System.out.print(s.pop());
	System.out.print(q.dequeue());
	s.pop();
	q.dequeue();
	System.out.print(s.pop());
	System.out.print(q.dequeue());
	System.out.print(s.pop());
	System.out.println(q.dequeue());
	s.pop();
	q.dequeue();
    }
    private static void prepare() {
        q = new Queue();
        s = new Stack();
        q.enqueue(3);
        s.push(0);
        s.push(8);
        q.enqueue(9);
        s.push(7);
        q.enqueue(0);
        s.push(0);
        q.enqueue(2);
        s.push(4);
        q.enqueue(1);
        s.push(3);
        q.enqueue(0);
    }
}
//33497281