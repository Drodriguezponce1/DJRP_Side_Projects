package Java.Practice;

public class CountingSort{

    private int[] a;

    public CountingSort(int[] a){
        this.a = a;
    }

    public void sort(){
        int max = 0;
        int min = 0;

        for(int n: this.a){
            max = Math.max(max, n);

            min = Math.min(min, n);
        }

        int[] count = new int[max - min + 1]; // since we consider zeroes we need max - min + 1;

        // we have to update each index at n + m; this just means that we need to update the placeholder for 5 for example
        for(int n: this.a){
            count[n - min]++;
        }

        for(int i = 0; i < count.length; i++){
            System.out.println(i + " is counted: " + count[i] + " times!");
        }

        // once we have our count array
        int index = 0;

        for(int i = 0; i < count.length; i++){
            while(count[i] > 0){
                this.a[index] = i + min;
                index++;
                count[i]--;
            }

        }
    }

    public String toString(){

        String temp = "";

        for(int n: this.a){
            temp += n + " ";
        }
        return "[ " + temp + "]";
    }


}