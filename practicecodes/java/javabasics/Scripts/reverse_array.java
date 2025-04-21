package Scripts;
import java.util.*;

public class reverse_array 
{
    /*
    reverse using creating new array
     */
    static void reverse(int a[], int n)
    {
        int [] b = new int[n];
        int j = n;
        System.out.println("Lenth of array : "+a.length);
        // int j = a.length;
        for (int i=0; i<n;i++)
        {
            b[j-1]=a[i];
            j= j-1;
            System.out.print(i);
        }
        // printing the array
        System.out.println("The reversed array is : \n");
        // System.out.println("Final array is : "+b);
        for (int k = 0; k<n; k++)
        {
            System.out.print(" "+b[k]);
        }
    }

    /*
    reverse array using swapping
     */
    static void reverse_by_swap(int a[])
    {
        int len = a.length, m;

        for(int i=0; i< a.length/2; i++ )
        {
            // {10,20,30,40,50}
            m = a[len - (i+1)];
            a[len - (i+1)] = a[i];
            a[i] = m;

        }
        System.out.print("Final array : ");
        for(int z = 0; z<len; z++)
        {
            System.out.print(" "+a[z]);
        }
    }
    /*
     * reverse array by collection.reverse() 
     */
    static void reverse_by_collections(Integer a[])
    {
        Collections.reverse(Arrays.asList(a));
        System.out.print("Final array : "+Arrays.asList(a));
    }

    // reverse string by StringBuilder.append()
    static void reverse_String_builder_append(String strarray[])
    {
        StringBuilder stb = new StringBuilder();
        for(int i=strarray.length; i>0; i--)
        {
            stb.append(strarray[i-1]).append(" ");
        }
        String[] reversedArray = stb.toString().split(" ");
        System.out.println(reversedArray);
    }

    public static void main(String args[])
    {
        Integer arr[] = {10,20,30,40,50,60,70,80};
        String[] str_array = {"Reverse", "String", "Example"};
            // type one
            // reverse(arr, arr.length);
            // type two
            // reverse_by_swap(arr);
        // reverse_by_collections(arr);
        reverse_String_builder_append(str_array);
    }    
    
}
