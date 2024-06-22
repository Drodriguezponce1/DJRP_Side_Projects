package Java.RandomExamples;

import java.util.Arrays;

public class Sorting_Searching {
    
    public static void main(String[] args) {
        int[] a = {3,5,0,1,2,4};

        System.out.println(Arrays.toString(selection_sort(a)));
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
}
