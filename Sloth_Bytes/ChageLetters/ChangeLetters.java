package Sloth_Bytes.ChageLetters;

import java.util.Arrays;

/***
 * Author: Daniel Rodriguez
 * Date: June 21, 2024
 * 
 * given a string change the letters to the next letter in the alphabet
 * i.e. a -> b, b->c... and so on
 * 
 */

public class ChangeLetters {
    public static void main(String[] args) {
        System.out.println("================= Starting Strings =================");
        String[] s = { "hello", "bye", "welcome", "Zebra", "zelda" };
        System.out.println(Arrays.toString(s));

        System.out.println("================= Changed Strings =================");
        for (int i = 0; i < s.length; i++) {
            s[i] = move(s[i]);
        }
        System.out.println(Arrays.toString(s));

    }

    public static String move(String s) {
        String temp = "";

        for (char c : s.toCharArray()) {
            if (c == 'z') {
                temp += 'a';
            } else if (c == 'Z') {
                temp += 'A';
            } else {
                temp += (char) (1 + c); // this takes the ASCII value of c and adds 1 value to it
            }
        }
        return temp;
    }

}
