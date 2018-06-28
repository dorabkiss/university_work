class SLList {
    private Object first; // first item
    private SLList rest;
    private int size; // size of the list

    public SLList(Object f, SLList r) {
        first = f;
        rest = r;
        size = 0;
    } // initialises an empty list

    public static final SLList NIL = new SLList(0, null);

    public Object first() {
        return first;
    }
    public SLList rest() {
        return rest;
    }
    public void setFirst(Object f) {
        first = f;
        size++;
    }
    public void setRest(SLList r) {
        rest = r;
    }

    public Object nth(int i) {
        if (i == 0){
            return first;
        } return rest.nth(i-1);
    }
    public SLList nthRest(int i) {
        if (i == 0) {
            return this;
        }
        return rest.nthRest(i-1);
    }


    public int length() {
        if (rest == null) {
            return 0;
        }
        return 1 + rest.length();
    } // returns the number of items in the list

    public SLList remove(Object o) {
        if (this.equals(NIL)) return NIL;
        if (rest.equals(NIL) && first.equals(o)) return NIL;
        if (rest.equals(NIL) && !first.equals(o)) return new SLList(first, rest);

        if (first.equals(o)) {
            return new SLList(rest.first, rest.rest);
        } else {
            return new SLList(first, rest.remove(o));
        }
    }

    public SLList reverse() {
        if (rest == null) {
            return this;
        } // list is empty

        if (rest == NIL) {
            SLList x = new SLList(first, NIL);
            return x;
        } // list has only one item

        SLList reversed = new SLList(first, NIL);

        for (int i = 1; i < length(); i++) {
            reversed = new SLList(nth(i), reversed);
        }
        return reversed;
    }

    public Integer sum() {
        int sums = 0;

        if (rest == null) {
            sums = 0;
        }

        for (int i = 0; i <= length(); i++){
            sums += (int) nth(i);
        }
        return sums;
    }
}

