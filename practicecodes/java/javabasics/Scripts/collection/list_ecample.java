package Scripts.collection;

import java.util.*;

public class list_ecample 
{
    public static void main(String[] args)
    {   

        // new code
        arlist arl = new arlist();
        arlist arl1 = new arlist();
        // arl.Name = "";
        arlist[] items = {arl, arl1, new arlist(), new arlist()};

        arl.Name = "NameOne";
        arl1.Name = "NameTne";

        arl.description = "customer one name";
        arl1.description = "customer two name";

        arl.size = 48;
        arl1.size = 47;

        items[3].Name = "customer two name";
        items[3].description = "customer two name";
        // new code
        List<String> lst = new ArrayList<String>();
        
        lst.add("sallium");
        lst.add("pallium");
        lst.add("guallium");
        lst.add("lithium");

        System.out.println(lst.toString());
        for (arlist ar : items)
        {
            System.out.println(ar.toString());
        }
    }

}
