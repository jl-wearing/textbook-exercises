import java.awt.Rectangle;

public class AreaTester {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(0, 0, 45, 80);
        double area = rect.getWidth() * rect.getHeight();

        System.out.printf("Area: %.2f\n", area);
        System.out.printf("Expected area: 3600\n");
    }
}