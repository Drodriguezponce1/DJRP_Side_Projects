import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Barrows {
    public static int counter = 0; // holds the counter for how many uniques a player has
    public static int place = 1; // just a placeholder for the places for later
    public static int sumAllDrops = 0;
    public static void main(String[] args) throws Exception {

        System.out.println("============== BARROWS DROPS ======================");

        // These AL hold the data from the text file, winners holds the actual places
        // and sorts them by unique amounts
        ArrayList<String[]> arrayList = new ArrayList<String[]>();
        ArrayList<String[]> winner = new ArrayList<String[]>();
        ArrayList<Integer> winners = new ArrayList<Integer>();
        ArrayList<String> drops = new ArrayList<String>();

        // File that we use for this program
        File f = new File("BarrowsText.txt");

        Scanner s = new Scanner(f);

        // reads the file
        while (s.hasNext()) {
            // splits the lines by the regex: " " (meaning spaces)
            String[] arr = s.nextLine().split(",");
            arrayList.add(arr);
            drops.add(arr[1].trim());
        }

        // double checking it reads the file correctly
        for (String[] arr : arrayList) {
            System.out.println(Arrays.toString(arr));
        }

        System.out.println("================ BARROWS CHECK FOR UNIQUENESS ====================");

        // Seen is used for uniqueness as we check each unique players name ( which is
        // held in the arrayList AL)
        ArrayList<String> seen = new ArrayList<String>();
        for (int i = 0; i < arrayList.size(); i++) {
            // grab the current player name and check to see if its in the seen AL
            String current = arrayList.get(i)[0];
            if (!seen.contains(current)) {
                // once we have a unique player name we want to check how many uniques that have
                for (int j = 0; j < arrayList.size(); j++) {
                    if (current.equals(arrayList.get(j)[0])) {
                        counter++;
                    }
                }

                // made this object to have a player and their amount of uniques
                String[] temp = { current, "" + counter };

                System.out.println(current + " has " + counter + "  Uniques");
                winner.add(temp);
                winners.add(counter);

                counter = 0;
                seen.add(current);

            }
        }

        // saw this online its a sorting thing
        winners.sort(Comparator.reverseOrder());

        System.out.println("================ BARROWS WINNERS ====================");

        // this simply prints the barrows winners based on the AL
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < winner.size(); j++) {

                if (Integer.parseInt(winner.get(j)[1]) == winners.get(i)) {

                    if (place != 6) {
                        System.out.println("Place: " + place + ", " + winner.get(j)[0]);

                        place++;
                    }

                }
            }
        }

        System.out.println("================ DROP CALCULATIONS ====================");
        calculateGear(drops);
        s.close();

    }

    public static void calculateGear(ArrayList<String> drops) throws FileNotFoundException
    {
        File f = new File("BarrowsCalculator.txt");
        Scanner s = new Scanner(f);

        ArrayList<String[]> GeDrops = new ArrayList<String[]>();
        while(s.hasNext())
        {
            String[] current = s.nextLine().split(",");
            GeDrops.add(new String[]{current[0].trim(),current[1]});
            
        }

        
        int[] amountUnique = new int[GeDrops.size()];
        for(String d: drops)
        {
            //System.out.println(d);
            for(int i = 0; i < GeDrops.size(); i++)
            {
                if(d.equalsIgnoreCase(GeDrops.get(i)[0]))
                {
                    amountUnique[GeDrops.indexOf(GeDrops.get(i))] += Integer.parseInt(GeDrops.get(i)[1]);
                    sumAllDrops += Integer.parseInt(GeDrops.get(i)[1]);
                    //System.out.println(sumAllDrops);
                }
            }
        }

        System.out.printf("Total Clan Drops: $%,d\n",sumAllDrops);

        int counterUnique = 0;
        for(int amountUni: amountUnique)
        {
            if(amountUni != 0)
            {
                System.out.printf("Darn Kids received a drop: %d x %s ($%,d)\n",(amountUni/Integer.parseInt(GeDrops.get(counterUnique)[1])),GeDrops.get(counterUnique)[0],amountUni);
            }
            counterUnique++;
        }

        s.close();
        
    }
}
