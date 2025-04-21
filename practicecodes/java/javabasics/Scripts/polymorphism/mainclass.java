package Scripts.polymorphism;

public class mainclass 
{   
    /*
     * this is suitable example of inheritance in which subclasstwo is 
     * derived from subclass and instant of objects ae being passed
     */
    public static void main(String[] args)
    {
        // subclass objone = new subclass();
        // subclasstwo objonetwo = new subclasstwo();

        // clothing[] items = {new subclass(), new subclasstwo()};
        // arrlist[] items = {objone, objonetwo};
        subclass[] sbc = {new subclass(), new subclasstwo()};

        System.out.println(sbc[1].getPrise());
    }

}
