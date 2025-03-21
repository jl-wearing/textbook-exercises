/**
 * A bank account has a balance that can be changed by
 * deposits and withdrawals.
 */

public class BankAccount {
    private double balance;

    /**
     * Sets the balance to zero.
     */
    public BankAccount() {}

    /**
     * Sets the balance to the value supplied.
     * @param initialBalance The starting balance of the new bank account.
     */
    public BankAccount(double initialBalance) { balance = initialBalance; }

    /**
     * Deposits money into the bank account.
     * @param amount the amount to deposit.
     */
    public void deposit(double amount) { balance+=amount; }

    /**
     * Withdraws money from a bank account.
     * @param amount the amount to withdraw.
     */
    public void withdraw(double amount) { balance-=amount; }

    /**
     * Returns the current balance.
     * @return the current balance.
     */
    public double getBalance() { return balance; }

    /**
     * Withdraws a monthly account fee from a bank account.
     */
    public void monthlyFee() { withdraw(10.00); }

    /**
     * Returns a String representation of a bank account.
     * @return the string describing the state of a bank account.
     */
    public String toString() {
        return this.getClass().getName() + "[" + this.balance + "]";
    }

    /**
     * Returns true if 2 bank accounts have the same balance.
     * @return true if 2 bank accounts have the same balance, false otherwise.
     */
    public boolean equals(Object other) {
        if(this == other){ return true; }
        if(other == null) { return false; }
        if(this.getClass() != other.getClass()) { return false; }

        BankAccount o = (BankAccount)other;

        return balance == o.balance;
    }
}