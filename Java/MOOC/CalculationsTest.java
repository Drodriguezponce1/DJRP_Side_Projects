package Java.MOOC;

import org.junit.*;
public class CalculationsTest {
    public Calculations c = new Calculations();
    @Test
    public void squared_test()
    {
        Assert.assertEquals(25, c.squared(5));
    }

    @Test
    public void square_root_sum_test1()
    {
        Assert.assertEquals(1, c.square_root_sum(1, 0));
    }

    @Test
    public void square_root_sum_test2()
    {
        Assert.assertEquals(3, c.square_root_sum(5, 4));
    }


}
