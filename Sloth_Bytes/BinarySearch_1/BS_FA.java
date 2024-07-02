package Sloth_Bytes.BinarySearch_1;

import java.util.Arrays;

/***
 * Author: Daniel Rodriguez
 * Date: July 2, 2024
 * 
 * given an integer array, find target x and return its first occurrence
 * using binary search
 * 
 * ex:
 * arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
 * target = 3
 * find_first_occurrence(arr,target) # Return 1
 */

public class BS_FA {

    public static void main(String[] args) {

        System.out.println("==================== Example 1 ====================");
        int[] arr = { 1, 3, 3, 3, 3, 6, 10, 10, 10, 100 };
        int target = 3;
        System.out.println(Arrays.toString(arr) + ", Target: " + target);
        System.out.println("Found at position: " + find_first_occurrence(arr, target));

        System.out.println("==================== Example 2 ====================");
        target = 10;
        System.out.println(Arrays.toString(arr) + ", Target: " + target);
        System.out.println("Found at position: " + find_first_occurrence(arr, target));

        System.out.println("==================== Example 3 ====================");
        int[] arr2 = { 2, 3, 5, 7, 11, 13, 17, 19 };
        target = 6;
        System.out.println(Arrays.toString(arr2) + ", Target: " + target);
        System.out.println("Found at position: " + find_first_occurrence(arr2, target));
    }

    public static int find_first_occurrence(int[] a, int target) {
        int low = 0;
        int high = a.length - 1;

        while (low <= high) {
            int middle = low + (high - low) / 2;

            if (a[middle] == target) {
                while (a[middle] == target) {
                    middle--; 
                }
                return ++middle; // reason for this is because we subtract 1 extra from the while loop
            } else if (target > a[middle]) {
                low = middle + 1;
            } else {
                high = middle - 1;
            }
        }
        return -1;
    }
}
