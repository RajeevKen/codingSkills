package Scripts;

public class string_reverse 
{
    // reversed string by 
    static void srting_reverse(String strng)
    {
        String nmstr="";
        char ch;
        for(int i =0; i<strng.length(); i++)
        {
            ch = strng.charAt(i);
            nmstr = ch + nmstr;
        }
        System.out.println("Original String : " + strng + " reversed string : "+nmstr);
    }
    public static void main(String[] args)
    {
        srting_reverse("arrags");
    }

    /*
     * reverse string using byte array
     */
    static void reverse_byte_array()
    {
        
    }
}
