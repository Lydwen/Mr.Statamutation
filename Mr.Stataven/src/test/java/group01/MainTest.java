package group01;

import junit.framework.TestCase;

/**
 * Created by user on 12/02/2016.
 */
public class MainTest extends TestCase {

    Main main = new Main();

    public void testMain() throws Exception {
        assertEquals(4, main.addition(1,3));
        assertNotSame(4, main.addition(1,1));

        assertEquals(4, main.soustraction(4,0));
        assertNotSame(4, main.soustraction(4,1));

        assertTrue(main.supeq(4,4));
        assertTrue(main.supeq(6,4));
        assertFalse(main.supeq(3,4));

        assertTrue(main.infeq(3,4));
        assertTrue(main.infeq(4,4));
        assertFalse(main.infeq(4,6));

        assertTrue(main.sup(5,4));
        assertFalse(main.sup(4,4));

        assertTrue(main.inf(4,5));
        assertFalse(main.inf(4,5));

        assertTrue(main.equal(5,5));
        assertFalse(main.equal(4,5));
    }
}
