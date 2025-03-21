/**
 * A Counter class to model a Counter.
 */

public class Counter {
    private int value;

    /**
     * Default constructor to initialize a counter to zero.
     */
    public Counter() { }

    /**
     * Constructor to set the Counter to an initial tally.
     * @param initial The initial starting value.
     */
    public Counter(int initial) { value = initial; }

    /**
     * Method to increment the counter by 1.
     */
    public void click() { value++; }

    /**
     * Method to decrement the counter by 1.
     */
    public void undo() { value = Math.max(value - 1, 0); }

    /**
     * Method to return the current value of the counter.
     * @return The current value of the counter.
     */
    public int getCount() { return value; }

    /**
     * Method to set the maximum tally limit.
     * @param maximum The maximum tally a counter can have.
     */
    public void setLimit(int maximum) { value = Math.min(value, maximum); }

    /**
     * Method to reset the Counter to zero.
     */
    public void reset() { value = 0; }
}