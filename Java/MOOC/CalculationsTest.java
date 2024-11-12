package Java.MOOC;

import org.junit.*;
public class CalculationsTest {
    
    @Test
    public void test1()
    {
        Calculations c = new Calculations();

        Assert.assertEquals(25, c.squared(5));
    }
}
