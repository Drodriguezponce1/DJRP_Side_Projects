package Java.RandomExamples;

import java.util.Arrays;

public class Sorting_Searching {
    
    public static void main(String[] args) {
        int[] a = {3,5,0,1,2,4};

        a = selection_sort(a);
        System.out.println(Arrays.toString(a));

        System.out.println(binary_search(a, 5));
    }

    public static int[] selection_sort(int[] a){

        for(int i = 0; i < a.length; i++)
        {
            int min = a[i];

            //find the lowest number and grab its index
            for(int j = i + 1; j< a.length; j++)
            {
                if(a[j] < min)
                {
                    min = j;
                }
            }

            //swap the selection to each index starting at i
            int temp = a[i];
            a[i] = a[min];
            a[min] = temp;



        }

        return a;
    }

    public static int binary_search(int[] a, int n)
    {
        //grab the left most index and right most index
        int left = 0;
        int right = a.length - 1;

        while(left <= right)
        {
            //grab the middle between the left most and right most
            int middle = left + (right - left) / 2;;
            if(n == a[middle])
            {
                return middle;
            }
            else if(n > a[middle])
            {
                left = middle + 1;
            }
            else
            {
                right = middle - 1;
            }
        }

        return -1;
    }
}
