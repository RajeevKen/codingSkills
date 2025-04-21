package Scripts;

public class dot {
    
/*
 * This method is used to reverse the string argument
 */
static void reverse_p(String str_org)
{
   String r_srt = "";

   for (int i=0; i <str_org.length(); i++)
    
   {
        char chr = str_org.charAt(i);
        r_srt = chr + r_srt;
   }
   System.out.println("The reversed string is : "+r_srt);
}
public static void main(String[] args)
{
    String ss = "miltiple";
    reverse_p(ss);
}
}
