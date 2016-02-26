package group01;

import junit.framework.TestCase;

/**
 * Created by user on 12/02/2016.
 */
public class MainTest extends TestCase {

    public void testMain() throws Exception {
        Main main = new Main();
        assertEquals(4, main.addition(1,3));
        assertEquals(4, main.addition(1,3));
    }
}
