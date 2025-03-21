package Java.MOOC;

import java.util.HashMap;
import java.util.Scanner;

public class Excercise1 {
    
    //something similar to what MOOC is asking, grabbing user input. 
    // For this I am making a slight change to make the user guess from 1 - 3


    public static void main(String[] args) {
        

        HashMap<Integer, String> hm = new HashMap<Integer, String>();

        Scanner s = new Scanner(System.in);

        System.out.print("Please enter your name: ");
        String name = s.nextLine();

        System.out.print("Please enter a number between 1 and 3: ");

        int num = s.nextInt();

        while(num > 3 || num < 1)
        {
            System.out.print("Please enter a new number between the range 1 - 3: ");
            num = s.nextInt();
        }

        hm.put(1, "Greetings " + name + ", How are you?");
        hm.put(2, "You chose the wrong choice " + name + "! HAHAHAHAHA");
        hm.put(3, "Your chest contained 10 gold, congrats " + name);


        System.out.println(hm.get(num));

        s.close();
    }
}
