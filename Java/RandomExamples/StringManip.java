package Java.RandomExamples;
import java.util.HashMap;

public class StringManip{
    public static void main(String[] args) {
    
        String s = "10011011001;0110,1001,1001,0,10,11";
        System.out.printf("%.4f\n", 123.2342342);

        String[] m = s.split(";");
        // ['10011011001','0110,1001,1001,0,10,11']

        String toBeChanged = m[0];

        String[] changes = m[1].split(",");
        // ['0110','1001','1001','0','10','11']

        toBeChanged = makeChanges(toBeChanged, changes);

        System.out.println(toBeChanged);
    }

    public static String makeChanges(String str, String[] changes)
    {
        int placeholder = 2;

        HashMap<Integer, String> m = new HashMap<Integer, String>();

        for(int i = 0; i < changes.length; i+=2)
        {
            m.put(placeholder, changes[i+1]);
            System.out.print(str + " changed too: ");
            str = str.replaceFirst(changes[i], "" + placeholder);
            str = str.replaceFirst(changes[i], "" + placeholder);
            System.out.println(str + " using " + changes[i] + " ====> " + changes[i+1] + " AKA: "+ placeholder);

            placeholder++;
        }

        for(int values: m.keySet())
        {
            str = str.replaceFirst("" + values,m.get(values));
        }

        return str;
    }
}
