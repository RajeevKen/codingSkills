package Scripts.oops;

public class oppsexample 
{
    String name;
    String size;    
    int[] scores = {1,2,3,4,5,6,7,8};
    // for (int unitscore : scores)
    // {
    //     System.out.println(unitscore);
    // }
    public static void main(String[] args)
    {
        oppsexample ops = new oppsexample();
        for (int unitscore : ops.scores)
        {
            System.out.println(unitscore);
        }
    }
}
