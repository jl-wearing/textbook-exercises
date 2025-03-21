import java.awt.Graphics2D;
import java.awt.geom.Line2D;
import java.awt.geom.Point2D;
import java.awt.Rectangle;
import java.awt.geom.Ellipse2D;

/**
 * A car shape that can be positioned anywhere on the screen.
 */

public class Car {
    private int x;
    private int y;

    public Car(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void draw(Graphics2D g2) {
        //Construct the body.
        Rectangle body = new Rectangle(x, y+10, 60, 10);
        //Construct the tyres.
        Ellipse2D.Double frontTyre = new Ellipse2D.Double(x, y+20, 10, 10);
        Ellipse2D.Double rearTyre = new Ellipse2D.Double(x+40, y+20, 10, 10);
        //Construct the front windshield.
        Point2D.Double r1 = new Point2D.Double(x+10, y+10);
        Point2D.Double r2 = new Point2D.Double(x+20, y);
        Line2D.Double frontWindShield = new Line2D.Double(r1, r2);
        //Construct the top frame.
        Point2D.Double r3 = new Point2D.Double(x+40, y);
        Line2D.Double topFrame = new Line2D.Double(r2, r3);
        //Construct the rear windshield.
        Point2D.Double r4 = new Point2D.Double(x+50, y+10);
        Line2D.Double rearWindShield = new Line2D.Double(r3, r4);

        //Add the drawings to the component.
        g2.draw(body);
        g2.draw(frontTyre);
        g2.draw(rearTyre);
        g2.draw(frontWindShield);
        g2.draw(topFrame);
        g2.draw(rearWindShield);
    }
}