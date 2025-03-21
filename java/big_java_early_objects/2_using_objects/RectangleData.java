import java.awt.Rectangle;

public class RectangleData {
    public static void main(String[] args) {
        //Construct a rectangle with area 42.
        Rectangle rect = new Rectangle(0, 0, 6, 7);

        //Construct a rectangle with perimeter 42.
        Rectangle perRect = new Rectangle(0, 0, 10, 11);

        //Output the data.
        System.out.printf("Height: %.2f\tWidth: %.2f\n", rect.getHeight(), rect.getWidth());
        System.out.printf("Height: %.2f\tWidth: %.2f\n", perRect.getHeight(), perRect.getWidth());
    }
}