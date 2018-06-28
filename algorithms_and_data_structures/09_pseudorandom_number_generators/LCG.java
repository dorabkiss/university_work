public class LCG {
    public long a; // multiplier
    public long c; // increment
    public long m; // modulus
    public long x; // start value
    public long shift;

    public LCG(long _a, long _c, long _m, long seed) {
        a = _a;
        c = _c;
        m = _m;
       // if (seed == 0) seed +=m;
        x = seed;
        shift = 0;
    }

    public LCG(long _a, long _c, long _m, long seed, long _shift) {
        a = _a;
        c = _c;
        m = _m;
        // if (seed == 0) seed +=m;
        x = seed;
        shift = _shift;
    }

    // Advances the state by one iteration, returns the next random number from the generator
    public long next() {
        if (this.x == 0) {
            this.x += m;
        }
        //x = (x * a + c) & m-1; // x = (a*x + c) mod m
        if (shift != 0) {
            //x = (x >>> shift);
            x = (x * 0x5DEECE66DL + 0xBL) & ((1L << 48) - 1);
            return x >>> shift;
        }
        x = (x * a + c) & m-1; // x = (a*x + c) mod m
        return x;
    }

    public void seed(long seed) {
        x = seed;
    }




}
// seed to get moodle ID 3626130726 (question 3)
// Q4: 3289548223