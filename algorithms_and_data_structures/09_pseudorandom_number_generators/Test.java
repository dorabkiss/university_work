import java.math.BigInteger;
public class Test {
    public static void main(String[] args) {
        /*long a = 1664525L;
        long c = 1013904223L;
        long m = 4294967296L;
        LCG g = new LCG(a, c, m, 11);
        g.seed(3626130726L);
        System.out.println(g.next());

        long x ^= (x << a) % 4294967296L;
        x ^= (x >> b) % 4294967296L;
        x ^= (x << c) % 4294967296L;
*/
        /*BigInteger a = BigInteger.valueOf(13);
        BigInteger b = BigInteger.valueOf(17);
        BigInteger c = BigInteger.valueOf(5);
        BigInteger m = BigInteger.valueOf(4294967296L);
        BigInteger aInv = a.modInverse(m);
        BigInteger x = BigInteger.valueOf(53837);
*/
        //Xorshift g = new Xorshift(13, 17, 5, 4140);

        // x = x.subtract(b).multiply(aInv).mod(m);

      //  long xo = g.next();
        //System.out.println(aInv);
        //System.out.println(xo);

        Xorshift g = new Xorshift(13, 17, 5, 3289548223L);
        g.seed(3289548223L);
        System.out.println(g.next());






    }
}