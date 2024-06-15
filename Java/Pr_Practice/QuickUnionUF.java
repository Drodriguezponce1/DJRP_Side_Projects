import java.util.Arrays;

public class QuickUnionUF {
    
    private int[] ids;

    public QuickUnionUF(int n)
    {
        this.ids = new int[n];

        for(int i = 0; i < n; i++)
        {
            ids[i] = i;
        }
    }

    public int root(int x)
    {
        while(x != ids[x])
        {
            x = ids[x];
        }

        return x;
    }

    public boolean connection(int x, int y)
    {
        return root(x) == root(y);
    }

    public void union(int x, int y)
    {
        int root_x = root(x);
        int root_y = root(y);
        ids[root_x] = root_y;
    }

    public String toString()
    {
        return Arrays.toString(ids);
    }
}
