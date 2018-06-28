class SLListTest {
    public static void main(String[] args) {


        SLList d = new SLList(5, new SLList(3, new SLList(8, new SLList(3, new SLList(7, SLList.NIL)))));
        d.mergesort();

        System.out.println(d.counter);

    }
}