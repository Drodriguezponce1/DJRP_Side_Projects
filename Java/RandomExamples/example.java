package Java.RandomExamples;

public class example extends example2{

    public int yo2;

    public example(int yo2, int yo){
        super(yo);

        this.yo2 = yo2;

    }


    public String toString()
    {
        return '['+ yo2+ ", " + super.getYo() + "]";
    }
    
}
