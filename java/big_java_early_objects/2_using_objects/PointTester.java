import java.awt.geom.Point2D;

public class PointTester {
    public static void main(String[] args) {
        Point2D.Double p1 = new Point2D.Double(3, 4);
        Point2D.Double p2 = new Point2D.Double(-3, -4);
        double distance = p1.distance(p2);

        //Output
        System.out.printf("Actual distance: %.2f units\n", distance);
        System.out.printf("Expected distance: 10 units\n");
    }
}