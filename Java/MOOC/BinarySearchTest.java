package Java.MOOC;

import org.junit.*;

public class BinarySearchTest {
    
    private BinarySearch b;

    @Before
    public void setup()
    {
        this.b = new BinarySearch();
    }

    @Test
    public void test1()
    {
        b.setArr(new int[]{1,2,3,4,5,6,7,8});
        
        Assert.assertEquals(b.BinarySearch1(2), 1);
    }


}
