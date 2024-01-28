import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Barrows {
    public static int counter = 0; // holds the counter for how many uniques a player has
    public static int place = 1; // just a placeholder for the places for later

    public static void main(String[] args) throws Exception {

        System.out.println("============== BARROWS DROPS ======================");

        // These AL hold the data from the text file, winners holds the actual places
        // and sorts them by unique amounts
        ArrayList<String[]> arrayList = new ArrayList<String[]>();
        ArrayList<String[]> winner = new ArrayList<String[]>();
        ArrayList<Integer> winners = new ArrayList<Integer>();

        // File that we use for this progra,
        File f = new File("BarrowsText.txt");

        Scanner s = new Scanner(f);

        // reads the file
        while (s.hasNext()) {
            // splits the lines by the regex: " " (meaning spaces)
            String[] arr = s.nextLine().split(" ");
            arrayList.add(arr);
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

                    if (place != 5) {
                        System.out.println("Place: " + place + ": " + winner.get(j)[0]);

                        place++;
                    }

                }
            }
        }

        s.close();

    }
}
