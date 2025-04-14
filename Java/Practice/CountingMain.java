package Java.Practice;

public class CountingMain {

    public static void main(String[] args) {
        int[] c = { 5, 4, 3, 2, 1, 1, 1, 2, 3,4, 5 };

        CountingSort count = new CountingSort(c);

        System.out.println(count);
        count.sort();

        System.out.println(count);
    }
}
