package Scripts;
import java.util.ArrayList;
import java.util.Scanner;

public class primeNumber 
{
 
    
    static void pm(int n)
    {
        if (n==0||n==1)
        {
            System.out.print(n+ " Number is not prime");
        }
        else
        {
        // provide prime numbers in range
            int m=0,flag=0;
            m=n/2;
            for (int i=2; i<m;i++)
            {
                if(n%i==0)
                {
                    System.out.println(n + " Number is not prime number");
                    flag=1;
                    break;
                }
            }
            if(flag==0)
            {
                System.out.println(n+ " Number is prime number");
    
            }
        }
    }
    // using sq root
    public static boolean sqroot(int n)
    {
        if (n<=1)
        {
            return false;
        }
        else 
        {
            for(int i =2; i<Math.sqrt(n); i++)
            {
                if(n%i==0)
                {
                    return false;
                }
            }
            return true;
        }
    }
    public static void main(String[] args)
    {
        // Integer[] inarray = {1,2,3,4};
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number : ");
        Integer num = sc.nextInt();
        ArrayList<Integer> arrlst = new ArrayList<Integer>();
        arrlst.add(num);
        System.out.println(arrlst);
        // System.out.println(inarray);
        pm(num);
        System.out.println("*******************************************");
        if(sqroot(num))
        {
            System.out.println(num+ "  number is prime");
        }
        else
        {
            System.out.println(num+ "  number is not prime");
        }

    }
}
