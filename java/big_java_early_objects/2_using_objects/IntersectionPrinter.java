import java.awt.Rectangle;

public class IntersectionPrinter {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle(0, 0, 50, 125);
        Rectangle r2 = new Rectangle(150, 150, 125, 50);

        //Output the string representation of each rectangle.
        System.out.println(rect);
        System.out.println(r2);

        if(rect.intersects(r2)) {
            System.out.println("The 2 rectangles intersect!");
            System.out.println(rect.intersection(r2));
        } else {
            System.out.println("The 2 rectangles do not intersect!");
            System.out.println(rect.intersection(r2));
        }
    }
}

//Returns negative values when there is no intersection