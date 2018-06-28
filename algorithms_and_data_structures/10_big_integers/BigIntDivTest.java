import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;
import java.util.Random;
import org.junit.Test;

public class BigIntDivTest {
    @Test
    public void testDiv() {
        BigInt b1 = new BigInt(1);
        b1.data[0] = 8;
        BigInt b2 = new BigInt(1);
        b2.data[0] = 2;
        BigInt b3 = b1.Div(b2);
        assertEquals("8/2 != 4", 4, b3.get(0));
    }

    @Test
    public void testDiv2() {
        BigInt b1 = new BigInt("420");
        BigInt b2 = new BigInt("210");
        BigInt b3 = b1.Div(b2);
        assertEquals("420/210 != 2", 2, b3.get(0));
    }

    @Test
    public void testDiv3() {
        BigInt b1 = new BigInt(6);
        b1.data[0] = 2;
        b1.data[1] = 7;
        b1.data[2] = 0;
        b1.data[3] = 1;
        b1.data[4] = 3;
        b1.data[5] = 1;
        BigInt b2 = new BigInt(5);
        b2.data[0] = 6;
        b2.data[1] = 3;
        b2.data[2] = 5;
        b2.data[3] = 5;
        b2.data[4] = 6;
        BigInt b3 = b1.Div(b2);
        assertEquals("131072/65536 != 2", 2, b3.get(0));
    }
}
