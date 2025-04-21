package Scripts.collection;

import java.util.*;


public class arlist {
    

    String description;
    String Name;
    Integer size;
    public static void main(String[] args)
    {
        ArrayList<String> lst = new ArrayList<String>();
        // Vector<String> lst=new Vector<String>();  

        lst.add("Anil");
        lst.add("sunil");
        lst.add("junil");
        lst.add("pranil");
    
        // transversing thru array creating iterator
        Iterator<String> itr = lst.iterator();

        while(itr.hasNext())
        {
            System.out.println(itr.next());
        }
    }

}
