import java.util.Scanner;

public class Interest{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);

        //Input
        System.out.print("Enter your starting balance: ");
        double balance = in.nextDouble();
        System.out.printf("\nEnter the interest rate: ");
        double interest = in.nextDouble();
        in.close();

        //Process
        double amount = balance * 2.0;
        int yearsRequired = 0;
        while(balance < amount){
            balance = balance + balance * interest;
            yearsRequired++;
        }

        //Output
        System.out.printf("\nThe number of years required to double your initial investment: %d years.\n",yearsRequired);
    }
}