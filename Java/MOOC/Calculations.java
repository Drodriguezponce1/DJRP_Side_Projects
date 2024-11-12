package Java.MOOC;

//import java.util.Scanner;
public class Calculations {
    
    //These excercies come from Part 2 of Java Programming 1

/*   public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.println("Currently testing: squared(int x)");
        System.out.print("Please enter a number to be squared: ");
        int x = s.nextInt();
        System.out.println(x + " squared is: " + squared(x));

        System.out.println("==================================================================");

        System.out.println("Currently testing: squared(int x)");
        System.out.print("Please enter a number to be squared: ");
        int x = s.nextInt();
        System.out.println(x + " squared is: " + squared(x));



        s.close();
        
    }*/ 

    // simply returning the square of a number
    public int squared(int x)
    {
        return x * x;
    }

    public int square_root_sum(int x, int y)
    {
        return (int)Math.sqrt(x + y);
    }


}
