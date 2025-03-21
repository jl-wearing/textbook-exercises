//Testing the implementation of the BankAccount class.

public class BankAccountTester {
    public static void main(String[] args) {
        BankAccount a = new BankAccount();
        BankAccount b = new BankAccount(500);

        System.out.println(a.getBalance());
        System.out.println(b.getBalance());
        System.out.println();

        a.deposit(255.95);
        b.withdraw(10.50);
        System.out.println(a.getBalance());
        System.out.println(b.getBalance());
        System.out.println();

        System.out.println(a.toString());
        System.out.println(b.toString());
        System.out.println();

        BankAccount c = new BankAccount(500.00);
        BankAccount d = new BankAccount(500.00);
        if(c.equals(d)) {
            System.out.println("These 2 bank accounts have the same balance.");
        }
        else {
            System.out.println("The account sizes are not the same.");
        }
    }
}