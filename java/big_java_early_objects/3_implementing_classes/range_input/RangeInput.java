/**
 * A class to specify a range of inputs.
 */

public class RangeInput {
    private int value;
    private int min;
    private int max;

    /**
     * Sets the minimum and maximum bounds and calculates the value.
     * @param minimum The minimum value in the range.
     * @param maximum The maximum value in the range.
     */
    public RangeInput(int minimum, int maximum) {
        min = minimum;
        max = maximum;
        value = (min + max) / 2;
    }

    /**
     * Increments the value by 1.
     */
    public void up() { value = Math.min(value + 1, max); }

    /**
     * Decrements the value by 1.
     */
    public void down() { value = Math.max(value - 1, min); }

    /**
     * Retrieve the minimum value.
     * @return The minimum value.
     */
    public int minValue() { return min; }

    /**
     * Retrieves the maximum value.
     * @return The maximum value.
     */
    public int maxValue() { return max; }

    /**
     * Returns the current value in the range.
     * @return The current value.
     */
    public int getValue() { return value; }
}