import java.awt.Rectangle;

public class CenteredSquarePrinter {
    public static void main(String[] args) {
        Rectangle square = new Rectangle(100, 100, 200, 200);
        System.out.println(square);
        square.grow(-50, -50);
        square.translate(-25, -25);
        System.out.println(square);
    }
}