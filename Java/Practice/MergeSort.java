import java.util.Arrays;
public class MergeSort{
    public static void main(String[] args) {
        int[] arr = new int[] {10,324,52,13,5,-1,0,99, 1, 1, 1, 1, 10,324,52,13,5,-1,0,99, 1, 1, 1, 1, 10,324,52,13,5,-1,0,99, 1, 1, 1, 1, 10,324,52,13,5,-1,0,99, 1, 1, 1, 1, 10,324,52,13,5,-1,0,99, 1, 1, 1, 1, 10,324,52,13,5,-1,0,99, 1, 1, 1, 1, 10,324,52,13,5,-1,0,99, 1, 1, 1, 1, 10};
        mergeSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    public static void mergeSort(int[] arr){
        if(arr.length > 1){
            int half = arr.length / 2;

            int[] one = Arrays.copyOfRange(arr, 0, half);
            int[] two = Arrays.copyOfRange(arr, half, arr.length);

            mergeSort(one);
            mergeSort(two);

            merge(arr, one, two);

            
        }
    }

    public static void merge(int[] arr, int[] one, int[] two){
        int oneIndex = 0;
        int twoIndex = 0;
        int arrIndex = 0;

        while(oneIndex < one.length && twoIndex < two.length){
            if(one[oneIndex] < two[twoIndex]){
                arr[arrIndex] = one[oneIndex];
                oneIndex++;
            }else{
                arr[arrIndex] = two[twoIndex];
                twoIndex++;
            }

            arrIndex++;
        }

        while(oneIndex < one.length){
            arr[arrIndex] = one[oneIndex];
            oneIndex++;
            arrIndex++;
        }

        while(twoIndex < two.length){
            arr[arrIndex] = two[twoIndex];
            twoIndex++;
            arrIndex++;
        }
    }
}