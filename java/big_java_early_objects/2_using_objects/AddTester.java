import java.awt.Rectangle;

public class AddTester {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(5, 10, 20, 30);
        System.out.println(rect);
        rect.add(0, 0);
        System.out.println(rect);
    }
}