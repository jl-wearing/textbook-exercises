//Testing the implementation of the CashRegister class.

public class CashRegisterTester {
    public static void main(String[] args) {
        CashRegister a = new CashRegister();

        a.recordPurchase(50.00);
        a.recordPurchase(25.00);
        a.receivePayment(100.00);
        double change = a.dispenseChange();
        System.out.printf("Change: $%.2f\n", change);
        a.reset();
    }
}