import java.awt.Rectangle;

public class FourRectanglePrinter {
    public static void main(String[] args) {
        Rectangle box = new Rectangle(0, 0, 100, 50);
        System.out.println(box);

        box.translate(0, 50);
        System.out.println(box);

        box.translate(100, 0);
        System.out.println(box);

        box.translate(0, -50);
        System.out.println(box);
    }
}