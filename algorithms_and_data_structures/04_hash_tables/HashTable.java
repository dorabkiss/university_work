public class HashTable {
    // public for testing purposes
    public int buckets[];
    public long a;
    public long c;
    public long m;
    int size;
    private static final int removed = -9999999;   // special value used on removal
    private static final double maxLoad = 0.75;   // load factor on which to rehash


    public int hash(int x) { return (int)((a*x +c) % m); }

    public HashTable(long _a, long _c, long _m) {
        this.a = _a;
        this.c = _c;
        this.m = _m;
        buckets = new int[(int)_m];
        size = 0;
    }

    public void insert(int key) {
        // resize if necessary
        if (loadFactor() > maxLoad) {
            rehash();
        }
        int i = hash(key);
        while (buckets[i] != 0 && buckets[i] != key) {
            i = (i + 1) % buckets.length;
        }
        if (buckets[i] != key) {
            buckets[i] = key;
            size++;
        }
    }

    public boolean find(int key) {
        int j = hash(key);
        while (buckets[j] != 0 && buckets[j] != key) {
            j = (j + 1) % buckets.length;
        }
        return buckets[j] == key;
    }

    public double loadFactor() {
        return (double) size/buckets.length;
    }

    public void remove(int key) {
        // linear probing to find proper index
        int h = hash(key);
        while (buckets[h] != 0 && buckets[h] != key) {
            h = (h + 1) % buckets.length;
        }

        // remove the element
        if (buckets[h] == key) {
            buckets[h] = removed;
            size--;
        }
    }

    // Resizes the hash table to twice its original capacity.
    private void rehash() {
        int[] newBuckets = new int[2 * buckets.length];
        int[] old = buckets;
        buckets = newBuckets;
        size = 0;
        for (int n : old) {
            if (n != 0 && n != removed) {
                insert(n);
            }
        }
    }
}
