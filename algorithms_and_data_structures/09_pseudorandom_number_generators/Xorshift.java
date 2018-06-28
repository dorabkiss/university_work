public class Xorshift {
    long a;
    long b;
    long c;
    long x;

    public Xorshift(long _a, long _b, long _c, long seed) {
        a = _a;
        b = _b;
        c = _c;
        x = seed;
    }

    public long next() {
        x ^= (x << a) % 4294967296L;
        x ^= (x >> b) % 4294967296L;
        x ^= (x << c) % 4294967296L;

        return x;
    }

    public void seed(long seed) {
        x = seed;
    }
}
