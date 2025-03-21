/**
 * A cash register to store currency and
 * dispense change.
 */

public class CashRegister {
    private double payment;
    private double purchase;

    /**
     * Starts a cash register with no cash.
     */
    public CashRegister() {}

    /**
     * Records the price of an item.
     * @param amount The price of the item.
     */
    public void recordPurchase(double amount) { purchase+=amount; }

    /**
     * Records the amount payed by the customer.
     * @param amount the amount payed by the customer.
     */
    public void receivePayment(double amount) { payment = amount; }

    /**
     * Dispenses the change to a customer, if any.
     * @return The change owed to a customer.
     */
    public double dispenseChange() {
        if(payment < purchase) {
            return 0.0;
        }

        return payment - purchase;
    }

    /**
     * Resets the state of the cash register.
     */
    public void reset() {
        payment = 0;
        purchase = 0;
    }
}