import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;
import java.util.Random;
import org.junit.Test;

public class BigIntRemTest {
    @Test
    public void testRem() {
        BigInt b1 = new BigInt(1);
        b1.data[0] = 9;
        BigInt b2 = new BigInt(1);
        b2.data[0] = 2;
        BigInt b3 = b1.Rem(b2);
        assertEquals("9%2 != 1", 1, b3.get(0));
    }

    @Test
    public void testRem2() {
        BigInt b1 = new BigInt("420");
        BigInt b2 = new BigInt("203");
        BigInt b3 = b1.Rem(b2);
        assertEquals("420%203 != 14", 4, b3.get(0));
        assertEquals("420%203 != 14", 1, b3.get(1));
    }

    @Test
    public void testRem3() {
        BigInt b1 = new BigInt("2223");
        BigInt b2 = new BigInt("1110");
        BigInt b3 = b1.Rem(b2);
        assertEquals("2222%1110 != 3", 3, b3.get(0));
    }
}
