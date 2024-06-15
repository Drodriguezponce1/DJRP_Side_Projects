import java.util.Arrays;

/**
 * QuickFindUF
 */
public class QuickFindUF {

    private int[] ids;

    public QuickFindUF(int n)
    {
        this.ids = new int[n];

        for(int i = 0; i < n; i++)
        {
            ids[i] = i;
        }
    }

    public boolean connection(int x, int y)
    {
        return ids[x] == ids[y];
    }

    public void union(int x, int y)
    {
        int point1 = ids[x];
        int point2 = ids[y];

        for(int i = 0; i < ids.length; i++)
        {
            if(ids[i] == point1)
            {
                ids[i] = point2;
            }
        }
    }

    public String toString()
    {
        return Arrays.toString(ids);
    }
}