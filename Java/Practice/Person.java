public class Person{

    static 
    {
        main_id = 0;
    }
    private static int main_id;
    private int id,age;
    private String name, address;

    public Person()
    {
       this.id = main_id; 
       this.age = 0;
       this.name = "N/A";
       this.address = "N/A";
        
       main_id++;
    }

    public Person(String name, int age, String address)
    {
        this.id = main_id;
        this.name = name;
        this.age = age;
        this.address = address;

        main_id++;
    }

    public int getId()
    {
        return this.id;
    }

    public int getAge()
    {
        return this.age;
    }

    public String getName()
    {
        return this.name;
    }

    public String getAddress()
    {
        return this.address;
    }

    public void setName(String name)
    {
        System.out.println("Changing name....");

        this.name = name;
    }

    public void setAge(int age)
    {
        if(age < 0){
            System.out.println("Sorry unable to change the age");
        }
        else{
            System.out.println("Changing age....");
            this.age = age;
        }
    }

    public void setAddress(String address)
    {
        System.out.println("Changing Address....");
        this.address = address;
    }

    @Override
    public String toString()
    {
        return "[ID: " + this.id + ", Name: " + this.name + ", Age: " + this.age + ", Address: " + this.address + "]";

    }

    public boolean equals(Person o)
    {
        return (this.id == o.getId()) && (this.age == o.getAge()) && (this.name.equals(o.getName())) && (this.address.equals(o.getAddress()));
    }

    public int compare(Person o)
    {
        return 0;
    }



}