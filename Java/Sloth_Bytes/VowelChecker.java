package Java.Sloth_Bytes;

import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.HashMap;

/***
 * Author: Daniel Rodriguez
 * Date: June 11, 2024
 * 
 * Just a simple vowel checker which I will implement multiple 
 * to test out Big-O importance in time!
 * 
 * */

public class VowelChecker {
    
    public static void main(String[] args) {

        System.out.println("================= Method 1 =================");
        long start = System.currentTimeMillis();
        System.out.println("Using Method 1:");
        System.out.println("\"Celebration\" vowel count: "+count_vowels1("Celebration"));
        System.out.println("\"Palm\" vowel count: "+count_vowels1("Palm"));
        System.out.println("\"Prediction\" vowel count: "+count_vowels1("Prediction"));
        Long end = System.currentTimeMillis();
        float time = end-start;     
        System.out.printf("Method 1 took : %.4f seconds to execute\n",(time/1000));


        System.out.println("================= Method 2 =================");
        start = System.currentTimeMillis();
        System.out.println("Using Method 2:");
        System.out.println("\"Celebration\" vowel count: "+count_vowels2("Celebration"));
        System.out.println("\"Palm\" vowel count: "+count_vowels2("Palm"));
        System.out.println("\"Prediction\" vowel count: "+count_vowels2("Prediction"));
        end = System.currentTimeMillis();
        time = end-start;     
        System.out.printf("Method 2 took : %.4f seconds to execute\n",(time/1000));


        System.out.println("================= Method 3 =================");
        start = System.currentTimeMillis();
        System.out.println("Using Method 3:");
        System.out.println("\"Celebration\" vowel count: "+count_vowels3("Celebration"));
        System.out.println("\"Palm\" vowel count: "+count_vowels3("Palm"));
        System.out.println("\"Prediction\" vowel count: "+count_vowels3("Prediction"));
        end = System.currentTimeMillis();
        time = end-start;     
        System.out.printf("Method 3 took : %.4f seconds to execute\n",(time/1000));

        System.out.println("================= Method 4 =================");
        start = System.currentTimeMillis();
        System.out.println("Using Method 4:");
        System.out.println("\"Celebration\" vowel count: "+count_vowels4("Celebration"));
        System.out.println("\"Palm\" vowel count: "+count_vowels4("Palm"));
        System.out.println("\"Prediction\" vowel count: "+count_vowels4("Prediction"));
        end = System.currentTimeMillis();
        time = end-start;     
        System.out.printf("Method 4 took : %.4f seconds to execute\n",(time/1000));





    }

    public static int count_vowels1(String s)
    {
        int counter = 0;
        for(char c: s.toLowerCase().toCharArray())
        {
            if( c == 'a' || c == 'e' || c == 'i' || c == 'o')
            {
                counter++;
            }
        }
        return counter;
    }

    public static int count_vowels2(String s)
    {
        ArrayList<Character> vowels = new ArrayList<Character>();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');

        int counter = 0;
        for(char c: s.toLowerCase().toCharArray())
        {
            if(vowels.contains(c))
            {
                counter++;
            }
        }

        return counter;
    }

    public static int count_vowels3(String s)
    {
        char[] vowels = {'a','e', 'i', 'o', 'u'};

        int counter = 0;
        for(int i = 0; i < s.length(); i++)
        {
            for(int j = 0; j < vowels.length; j++)
            {
                if(vowels[j] == s.toLowerCase().charAt(i))
                {
                    counter++;
                }
            }
        }
        return counter;
    }

    public static int count_vowels4(String s)
    {
        HashMap<Character, Integer> vowels = new HashMap< Character, Integer>();
        vowels.put('a', 0);
        vowels.put('e', 0);
        vowels.put('i', 0);
        vowels.put('o',0);
        vowels.put('u',0);

        for(Character c: s.toCharArray())
        {
            if(vowels.containsKey(c))
            {
                vowels.put(c, vowels.get(c) + 1);
            }
        }

        int counter = 0;

        for(int x: vowels.values())
        {
            counter += x;
        }

        return counter;
    }
}
