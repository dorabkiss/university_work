class DynamicArray {
    private int[] storage; //array storing the elements (integers)
    private int nitems; //number of items stored, logical size
    int capacity; //how many items can be stored
    public OpCounter counter = new OpCounter();
    public DynamicArray(int size) {
        storage = new int[size];
        capacity = size;
        nitems = 0;
    } //initialises an empty stack
    public int length() {
        return nitems;
    } //returns the number of items in the array
    public int select(int k) {
        return storage[k]; // what if storage is empty or size = 0?
    }
    public void store(int o, int k) {
        storage[k] = o;
    }
    public void push(int o) {
        if (nitems==storage.length){
            extend();
        }
        counter.add(1);
        storage[nitems] = o;
        nitems++;
    }
    public int pop() {
        counter.add(1);
        nitems--;
        return storage[nitems];
    }
    private void extend() {
        //capacity += 5;
        //capacity *= 2;
        capacity *= capacity;
        int[] newstorage = new int[capacity];
        for(int i = 0; i < nitems; i++) {
            newstorage[i] = storage[i];
            counter.add(1);
        }
        storage = newstorage;
    }
}