public class PersonDriver {
    
    public static void main(String[] args) {
        Person p = new Person();

        System.out.println(p);

        System.out.println(p.equals(p));

        Person d = new Person("Daniel", 26, "Random Address");
        System.out.println(d);
        System.out.println(d.equals(p));
    }
}
