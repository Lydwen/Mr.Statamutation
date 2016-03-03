package group01;

import org.junit.Test;
import static junit.framework.Assert.*;

/**
 * Created by user on 12/02/2016.
 */
public class MainTest{

    Main main = new Main();

    @Test
    public void testAddition() {
        assertEquals(4, main.addition(1, 3));
        assertNotSame(4, main.addition(1, 1));
    }

    @Test
    public void testSoustraction(){
        assertEquals(4, main.soustraction(4, 0));
        assertNotSame(4, main.soustraction(4, 1));
    }

    @Test
    public void testSup() {
        assertTrue(main.sup(5, 4));
        assertFalse(main.sup(4, 4));
    }
    @Test
    public void testInf(){
        assertTrue(main.inf(4, 5));
        assertFalse(main.inf(4, 4));
    }
    @Test
    public void testEqual(){
        assertTrue(main.equal(5, 5));
        assertFalse(main.equal(4, 5));
    }

    @Test
    public void testAnd(){
        assertTrue(main.and(true,true));
        assertFalse(main.and(true,false));
        assertFalse(main.and(false,false));

    }

    @Test
    public void testOr(){
        assertTrue(main.or(true,false));
        assertTrue(main.or(true,true));
        assertFalse(main.or(false,false));
    }

    @Test
    public void testSupEq(){
        assertTrue(main.supeq(4,4));
        assertTrue(main.supeq(6,4));
        assertFalse(main.supeq(3,4));
    }

    @Test
    public void testInfEq(){
	    assertTrue(main.infeq(3,4));
        assertTrue(main.infeq(4,4));
        assertFalse(main.infeq(6,4));
    }

    @Test
    public void testInfEq2(){
        assertTrue(main.infeq2(4,4));
        assertFalse(main.infeq2(6,4));
    }
}
