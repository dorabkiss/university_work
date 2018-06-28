import java.util.ArrayList;
import java.util.List;

class Heap {
    // public for JUnit testing purposes
    public ArrayList<Integer> array;
    public int heap_size;
    public int countDirect = 0;
    public int countIncremental = 0;

    public Heap(int size) {
        array = new ArrayList<Integer>(size);
        heap_size = 0;
    }

    public Heap(List<Integer> source) {
        this(source, false);
    }

    public Heap(List<Integer> source, boolean incremental) {
        array = new ArrayList<Integer>(source.size());

        if (incremental) {
            heap_size = 0;
            for (int i = 0; i < source.size(); i++) {
                this.insert(source.get(i));
                countIncremental++;
            }
        }
        if (!incremental) {
            for (int i = 0; i < source.size(); i++) {
                array.add(source.get(i));
                heap_size++;
                countDirect++;
            }
            for (int i = source.size() / 2; i >= 0; i--) {
                this.maxHeapify(i);
            }
        }
    }

    public static int parent(int index) {
        // if (index < 1){return 0};
        return (index - 1) / 2;
    }

    public static int left(int index) {
        return (2 * index) + 1;
    }

    public static int right(int index) {
        return (2 * index) + 2;
    }

    public void maxHeapify(int i) {
        int largest = i;
        int leftIndex = left(i);
        int rightIndex = right(i);

        if (leftIndex < heap_size && array.get(largest) < array.get(leftIndex)) {
            largest = leftIndex;
        }
        if (rightIndex < heap_size && array.get(largest) < array.get(rightIndex)) {
            largest = rightIndex;
        }

        if (largest != i) {
            Integer temp = array.get(i);
            array.set(i, array.get(largest));
            array.set(largest, temp);
            maxHeapify(largest);
            countDirect+=2;
        }
    }

    public void buildMaxHeap() {
        for (int j = heap_size/2-1; j >= 0; j--) {
            maxHeapify(j);
        }
    }

    public void insert(Integer k) {
        array.add(k);
        heap_size++;
        int i = array.indexOf(k);
        int p = parent(i);
        while (i > 0 && array.get(i) > array.get(p)) {
            Integer temp = array.get(p);
            array.set(p, array.get(i));
            array.set(i, temp);
            i = p;
            p = parent(i);
            countIncremental++;
        }
    }

    public Integer maximum() {
        return array.get(0);
    }

    public Integer extractMax() {
        // if (array.size()<1) return null;
        if (array.size() == 1) {
            Integer max = array.get(0);
            array.remove(0);
            heap_size--;
            return max;
        } else {
            Integer max = array.get(0);
            array.remove(0);
            heap_size--;
            buildMaxHeap();
            return max;
        }
    }
    public ArrayList<Integer> sort(){
        buildMaxHeap();
        for (int i = heap_size-1; i>0; i--){
            Integer temp = array.get(0);
            array.set(0, array.get(i));
            array.set(i, temp);
            heap_size--;
            maxHeapify(0);
        }
        return array;
    }
}
