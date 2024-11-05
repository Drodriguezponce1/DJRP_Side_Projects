package Sloth_Bytes.CheckTitleString;
/***
 * Author: Daniel Rodriguez
 * Date: July 23, 2024
 * 
 * given a string check to see if it is formatted as a Title String:
 * 
 * ex: 
 * - "A Mind Boggling Achievement" ➞ true
 * - "Water is transparent" ➞ false
 */
public class CheckTitleString {
    
    public static void main(String[] args) {
        String one = "A Mind Boggling Achievement";
        String two = "Water is transparent";

        System.out.println(one + " -> " + checkTitle(one));
        System.out.println(two+ " -> "+ checkTitle(two));

    }

    public static boolean checkTitle(String s)
    {
        String[] str = s.split(" ");

        for(String s1: str)
        {
            if(!Character.isUpperCase(s1.charAt(0)))
            {
                return false;
            }
        }

        return true;
    }
}
