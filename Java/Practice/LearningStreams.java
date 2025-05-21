import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class LearningStreams {
    public static void main(String[] args) {

        List<Integer> numbers = new ArrayList<>();

        for (int i = 0; i < 100; i++) {
            numbers.add(i);
        }

        System.out.print("First 10 even numbers: ");
        numbers.stream()
                .filter(number -> number % 2 == 0).limit(10L)
                .forEach(number -> System.out.print(number + " "));

        System.out.println("\n\n+++++++++++++++++++++++++++++++++++++++++++++++\n");

        System.out.print("Sum of all numbers: ");
        System.out.println(numbers.stream().reduce(0, (start, number) -> start + number));

        System.out.println("\n+++++++++++++++++++++++++++++++++++++++++++++++\n");
        System.out.print("Sum of even numbers: ");
        System.out.println(numbers.stream()
                .filter(number -> number % 2 == 0)
                .reduce(0, (start, number) -> start + number));

        System.out.println("\n+++++++++++++++++++++++++++++++++++++++++++++++\n");
        // here i want to show that we can switch from a string notation to integer or
        // double
        List<String> nums = new ArrayList<>();

        for (int i = 0; i < 100; i++) {
            nums.add("" + i);
        }

        nums.stream()
                .map(number -> Integer.parseInt(number))
                .filter(number -> number % 2 == 0).limit(10L)
                .forEach(number -> System.out.print(number + " "));

        System.out.println("\n+++++++++++++++++++++++++++++++++++++++++++++++\n");
        new ArrayList<String>(Arrays.asList("Hello", "World", "Daniel")).stream()
                .forEach(word -> {
                    System.out.println("All letters of the word \"" + word + "\" added together is: " + calcWord(word));
                });

        System.out.println("\n+++++++++++++ SAME AS ABOVE ++++++++++++++++++++++++++++++++++\n");
        new ArrayList<String>(Arrays.asList("Hello", "World", "Daniel")).stream()
                .forEach(word -> {

                    int calc = 0;
                    for (char c : word.toCharArray()) {
                        calc += c;
                    }

                    System.out.println("All letters of the word \"" + word + "\" added together is: " + calc);
                });
    }

    public static int calcWord(String number) {
        int calc = 0;
        for (char c : number.toCharArray()) {
            calc += c;
        }

        return calc;
    }
}