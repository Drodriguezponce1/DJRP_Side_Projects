package Java.Testing;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class Testing {
    
    public static void main(String[] args) throws FileNotFoundException {
        ArrayList<String[]> arr = new ArrayList<String[]>();


        File f = new File("file.txt");

        Scanner s = new Scanner(f);

        while(s.hasNext())
        {
            arr.add(s.nextLine().split(","));
        }

        for(String[] sr: arr)
        {
            System.out.println(sr[Integer.parseInt(args[0])]);
        }
    }
    



    
}
