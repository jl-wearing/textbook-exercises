import java.awt.Rectangle;

public class PerimeterTester {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(0, 0, 10, 20);
        double perimeter = 2 * rect.getHeight() + 2 * rect.getWidth();

        //Ouput
        System.out.printf("Perimeter: %.2f\n", perimeter);
        System.out.printf("Expected Perimeter: 60 units\n");
    }
}