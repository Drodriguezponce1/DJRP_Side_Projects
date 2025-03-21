package Java.Practice;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class HangMan {
    
    private String message;

    private char[] msg;

    private HashMap<Character, Boolean> h;

    public HangMan()
    {
        System.out.print("Please enter a Message: ");

        Scanner scan = new Scanner(System.in);

        String s = scan.nextLine();

        scan.close();
        this.message = s;
        msg = s.toCharArray();

        for(int i = 0; i < msg.length; i++)
        {
            if(msg[i] != ' ')
            {
                msg[i] = 'x';
            }
        }

        this.h = new HashMap<Character, Boolean>();
        setupHM();
    }

    public HangMan(String message)
    {
        this.message = message;
        this.msg = message.toCharArray();
        for(int i = 0; i < msg.length; i++)
        {
            if(msg[i] != ' ')
            {
                msg[i] = 'x';
            }
        }
        this.h = new HashMap<Character, Boolean>();
        setupHM();
    }

    public String getMsg()
    {
        String temp = "";
        for(char c: msg)
        {
            temp += c;
        }

        return temp;
    }
    
    public String getMessage()
    {
        return message;
    }

    public void setupHM()
    {
        for(int i = 97; i <= 122; i++)
        {
            h.put((char) i, true);
        }
    }

    public void game()
    {
        String player = "";

        Scanner scan = new Scanner(System.in);
        System.out.print("Please enter your player name: ");
        player = scan.nextLine();

        System.out.println("Hello " + player + " you have 3 tries to get the message. Good Luck! ");

        int tries = 3;
        String temp = "";

        ArrayList<Character> used = new ArrayList<Character>();

        while(tries != 0 && !temp.equals(message))
        {  
            
            if(used.size() > 0)
            {
                System.out.println("Letters used: " + used);
            }

            System.out.println();
            System.out.println("Current state of message: " + getMsg());
           
            System.out.println();

            char choice = printAvailable();
            used.add(choice);
            if(message.contains("" + choice))
            {
                System.out.println("Great guess! ");
                updateMessage(msg, choice);
                temp = getMsg();
                
            }
            else
            {
                System.out.println("Oof. Wrong choice! You now have " + (tries - 1) + " tries");
                tries--;
            }

            System.out.println();
            temp = getMsg();

            
        }

        if(temp.equals(message))
        {
            System.out.println("CONGRATS YOU FIGURED OUT THE MESSAGE: " + "[" + message + "]");
        }
        else
        {
            System.out.println("AWW YOU FAILED TO FIGURED OUT THE MESSAGE: " + "[" + message + "]");
        }
    }

    public void updateMessage(char[] msg, char choice)
    {
        for(int i = 0; i < message.length(); i++)
        {
            if(message.charAt(i) == choice)
            {
                msg[i] = choice;
            }
        }
    }

    public char printAvailable()
    {
        Scanner scan = new Scanner(System.in);

        System.out.println("Please select from the current letters available: ");

        for(char c: h.keySet())
        {
            if(h.get(c) == true)
            {
                 System.out.print(c + " ");
            }
           
        }

        System.out.println();
        
        System.out.print("Choice: ");
        String ch = scan.nextLine();

        char choice = ch.charAt(0);

        while(h.get(choice) != true)
        {
            System.out.println("Please select a character that is available please: ");
            ch = scan.nextLine();
            choice = ch.charAt(0);
        }

        h.put(choice, false);
        
        return choice;
    }

}
