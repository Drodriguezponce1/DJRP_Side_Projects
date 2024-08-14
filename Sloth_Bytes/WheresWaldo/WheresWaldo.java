package Sloth_Bytes.WheresWaldo;

import java.util.Arrays;

public class WheresWaldo {
    
    public static void main(String[] args) {
        
        String[][] s1 = {
            {"A", "A", "A"},
            {"A", "A", "A"},
            {"A", "B", "A"}
        };

        //printArrays method defined below
        printArrays(s1);
        System.out.printf("\nWaldo was found at position: %s\n" ,Arrays.toString(findWaldo(s1)));
        System.out.println("=================================================\n");

        String[][] s2 = {
            {"c", "c", "c", "c"},
            {"c", "c", "c", "d"}
        };

        printArrays(s2);
        System.out.printf("\nWaldo was found at position: %s\n" ,Arrays.toString(findWaldo(s2)));
        System.out.println("=================================================\n");

        String[][] s3 = {
            {"O", "O", "O", "O"},
            {"O", "O", "O", "O"},
            {"O", "O", "O", "O"},
            {"O", "O", "O", "O"},
            {"P", "O", "O", "O"},
            {"O", "O", "O", "O"}
        };

        printArrays(s3);
        System.out.printf("\nWaldo was found at position: %s\n" ,Arrays.toString(findWaldo(s3)));
        System.out.println("=================================================\n");
    }


    public static int[] findWaldo(String[][] c)
    {
        for(int i = 0; i < c.length; i++)
        {
            // grab a copy of our current array, and sort it
            String[] temp = Arrays.copyOf(c[i], c[i].length);

            Arrays.sort(temp);
            
            // once we have our sorted copy, you want to see if there is a difference
            /**  In order to find a diff, we know for sure that when we sort our array
             *   we know that the second value is always going to be the duplicated value
             *   Ex: [2,2,1,2] -- Sorted --> [1,2,2,2]. We know that 2 is the duplicated one
             *   Ex2: [2,1,2,2] -- Sorted --> [1,2,2,2]. Taking a similar array, 2 is still the duplicated one at position 1
             *   By knowing we need to check for a difference from value 2, we have to go back
             *   to our original array and simply get the index where its not 2
            **/
            for(int j = 0; j < c[i].length; j++)
            {
                if(!c[i][j].equals(temp[1])) // the check for whichever is the 2nd value
                {

                    return new int[] {i + 1,j + 1};
                }
            }
        }

        return new int[] {-1,-1};
    }

    public static void printArrays(String[][] s)
    {
        for(String[] st: s)
        {
            System.out.println(Arrays.toString(st));
        }
    }

}
