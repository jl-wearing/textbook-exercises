import java.util.Scanner;

public class LoopFib {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.printf("Enter n: ");
        int n = console.nextInt();
        console.close();

        for(int i = 1; i <= n; i++) {
            long f = fib(i);
            System.out.printf("fib %d: %d\n", i, f);
        }
    }

    public static long fib(int n) {
        if(n<=2) {
            return 1;
        }
        else {
            long olderValue = 1;
            long oldValue = 1;
            long newValue = 1;

            for(int i = 3; i <= n; i++) {
                newValue = olderValue + oldValue;
                olderValue = oldValue;
                oldValue = newValue;
            }
            return newValue;
        }
    }
}