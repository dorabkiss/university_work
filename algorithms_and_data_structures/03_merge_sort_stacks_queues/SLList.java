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

    public SLList sublist(int start, int end) {
        if (start == 0) {
            if (end > 0) {
                return new SLList(first, rest.sublist(0, end - 1));
            }
            else return NIL;
        }
        else {
            return rest.sublist(start-1, end-1);
        }
    }

    public SLList merge(SLList b) {
        if (this.equals(NIL) && b.equals(NIL)) return NIL;
        else if (this.equals(NIL)) return b;
        else if (b.equals(NIL)) return this;
        else {
            int i = (int) this.first();
            int j = (int) b.first();
            if (i <= j) {
                return new SLList(first, rest.merge(b));
            }
            else {
                return new SLList(b.first(), this.merge(b.rest()));
            }
        }
    }


    public SLList mergesort() {
        int sl = this.length();
        if (sl <= 1) return this;
        else {
            int mid = sl/2;
            SLList left = sublist(0, mid).mergesort();
            SLList right = sublist(mid, sl).mergesort();
            return left.merge(right);
        }
    }
}

