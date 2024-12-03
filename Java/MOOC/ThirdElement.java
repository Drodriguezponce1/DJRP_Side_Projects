package Java.MOOC;

import java.util.ArrayList;
import java.util.Scanner;

public class ThirdElement {
    
    private ArrayList<String> a;


    public ThirdElement()
    {
        this.a = new ArrayList<String>();
    }

    public void getInput()
    {
        Scanner scan = new Scanner(System.in);

        System.out.println("Please enter at-most 3 names: ");
        String in = scan.nextLine();
        
        do{

            a.add(in);

            in = scan.nextLine();

        }while(in != "" || a.size() < 3);
        

        scan.close();

    }

    public void printArray()
    {
        int start = 1;

        for(String s: a)
        {
            System.out.println(start + ": " + s);
            start++;
        }
    }
    
}
