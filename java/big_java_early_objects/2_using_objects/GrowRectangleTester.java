import java.awt.Rectangle;

public class GrowRectangleTester {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(100, 100, 50 , 50);
        System.out.println(rect);

        //Testing the grow() method.
        rect.grow(25, 25);
        System.out.println(rect);
    }
}