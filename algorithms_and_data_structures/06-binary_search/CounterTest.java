public class CounterTest {
    private int counter = 0;

    public void resetCounter() {
        counter = 0;
    }

    int count(int array[], int key, int lo, int hi) {
        resetCounter();
        if (lo == hi) {
            return counter;
        }
        while (lo!=hi) {
            counter++;
            int mid = lo + (hi - lo - 1) / 2;
            if (array[mid] == key) {
                return counter;
            } else if (key < array[mid]) {
                hi = mid;
            } else {
                lo = mid+1;
            }
        } return counter;
    }

    public static void main(String args[]) {
        CounterTest c = new CounterTest();
        int[] array = new int[11342];
        for (int i = 0; i < array.length-1; i++) {
            array[i] = i;
        }
        System.out.println(c.count(array, 53961, 0, 33468101));
        System.out.println(c.counter);
    }
}

        // 33497281 53837