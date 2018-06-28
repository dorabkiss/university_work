public class BinarySearch {
    int counter = 0;

    public boolean search(int array[], int key, int lo, int hi) {
        //int mid = (lo + hi - 1) / 2; (lo+hi) is evaluated first, and could overflow int, so (lo+hi)/2 would return the wrong value.
        int mid = lo + ((hi - lo - 1) / 2); // to avoid overflow
        if (lo == hi) {
            return false;
        } else if (array[mid] == key) {
            return true;
        } else if (key < array[mid]) {
            return search(array, key, lo, mid);
        } else {
            return search(array, key, mid + 1, hi);
        }
    }

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

}
/* int mid = (lo + hi - 1) / 2 fails for large values of the int variables low and high.
Specifically, it fails if the sum of low and high is greater than the maximum
positive int value (2^31 - 1). The sum overflows to a negative value,
and the value stays negative when divided by two.
In Java, it throws ArrayIndexOutOfBoundsException.
 */