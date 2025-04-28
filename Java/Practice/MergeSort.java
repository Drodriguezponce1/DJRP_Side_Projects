import java.util.Arrays;
public class MergeSort{
    public static void main(String[] args) {
        int[] arr = new int[]{6,5,4,3,2,1};
        mergeSort(arr);
        System.out.println(Arrays.toString(arr));
    }

    public static void mergeSort(int[] arr){
        if(arr.length > 1){
            int half = arr.length / 2;

            int[] one = new int[half];
            int[] two = new int[arr.length - half];

            for(int i = 0; i < arr.length; i++){
                if(i < one.length){
                    one[i] = arr[i];
                }else{
                    two[i - one.length] = arr[i];
                }

                
            }

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