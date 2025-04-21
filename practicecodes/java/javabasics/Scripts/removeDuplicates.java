package Scripts;

import java.util.Arrays;

public class removeDuplicates {
    
    static void dupli(String str)
    {
        char [] chr = str.toCharArray();
        for (int i = 0; i<str.length(); i++)
        {
            if(chr[i]==chr[i+1])
            {
                str.charAt(i);
            }
        }
    }
    // remove duplicates type 2 method
    static String r_emove(char[] str)
        {
            int index=0;
            for(int i = 0; i<str.length; i++)
            {   int j;
                for(j=0; j<i; j++)
                {
                    if(str[i] == str[j])
                    {
                        break;
                    }
                }
                if (i==j)
                {
                    str[index++]=str[i];
                }
            }

            return String.valueOf(Arrays.copyOf(str, index));
        }
    
    public static void main(String[] args)
    {
        String str = "rrraaajjjeeevvv";
        char[] chr = str.toCharArray();
        // dupli(str);
        System.out.println(r_emove(chr));
    }
}
