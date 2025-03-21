package Java.MOOC;

public class BinarySearch {
    
    private int[] arr;

    public BinarySearch()
    {
        
    }

    public BinarySearch(int[] arr)
    {
        this.arr = arr;
    }

    public void setArr(int[] arr)
    {
        this.arr = arr;
    }

    public int BinarySearch1(int goal)
    {   
        int left = 0;
        int right = arr.length - 1;

        while(left <= right)
        {
            int mid = left + (right-left) / 2;

            if(arr[mid] == goal)
            {
                return mid;
            }
            else if(arr[mid] > goal)
            {
                right = mid - 1;
            }
            else
            {
                left = mid + 1;
            }
        }

        return -1;
    }
}
