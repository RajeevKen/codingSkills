package Scripts;

public class trycatch {

    public static void main(String[] main) {
        try {
            int arr[] = { 1, 2, 3 };
            System.out.print(arr[5]);
            int sum = 10 / 0;
            System.out.print(sum);
        } catch (ArithmeticException e) {
            System.out.println("Exception received : " + e);
        } catch (Exception e) {
            System.out.println("Exception received : " + e);
        }

        finally {
            System.out.println("This will get executed always...");
        }
    }
}
