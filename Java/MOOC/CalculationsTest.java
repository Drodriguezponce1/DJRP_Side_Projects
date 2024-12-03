package Java.MOOC;

import org.junit.*;

public class CalculationsTest {
    private static Calculations c;

    @Before
    public void setup()
    {
        c = new Calculations();
    }
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

    @Test
    public void absolute_test1()
    {
        Assert.assertEquals(4, c.absolute(4));
    }

    @Test
    public void absolute_test2()
    {
        Assert.assertEquals(44, c.absolute(-44));
    }

    @Test
    public void comparision1()
    {
        Assert.assertEquals("8 is greater than 4.", c.comparing(8, 4));
    }

    @Test
    public void comparision2()
    {
        Assert.assertEquals("-3 is smaller than 5.", c.comparing(-3, 5));
    }

    @Test
    public void comparision3()
    {
        Assert.assertEquals("1 is equal to 1." , c.comparing(1, 1));
    }


}
