import java.util.Scanner;

public class RecursiveFib {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.printf("Enter n: ");
        int n = console.nextInt();
        console.close();

        for(int i = 1; i <= n; i++) {
            long f = fib(i);
            System.out.printf("\nfib %d = %d", i, f);
        }
    }

    public static long fib(int n) {
        if(n <= 2) {
            return 1;
        }
        else {
            return fib(n - 1) + fib(n - 2);
        }
    }
}