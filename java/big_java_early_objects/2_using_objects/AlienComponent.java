import java.awt.geom.Line2D;
import java.awt.geom.Ellipse2D;
import java.awt.Rectangle;
import java.awt.Graphics2D;
import java.awt.Graphics;
import java.awt.Color;
import javax.swing.JComponent;

public class AlienComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Draw the face.
        Ellipse2D.Double face = new Ellipse2D.Double(20, 20, 50, 100);

        //Draw the eyes.
        Rectangle leftEye = new Rectangle(30, 40, 10, 10);
        Rectangle rightEye = new Rectangle(50, 40, 10, 10);

        //Draw the mouth.
        Line2D.Double mouth = new Line2D.Double(30, 100, 60, 100);

        //Add the face to the component.
        g2.setColor(Color.GRAY);
        g2.fill(face);

        //Add the eyes to the component.
        g2.setColor(Color.RED);
        g2.fill(leftEye);
        g2.fill(rightEye);

        //Add the mouth to the component.
        g2.setColor(Color.BLACK);
        g2.draw(mouth);

        //Add a message.
        g2.setColor(Color.MAGENTA);
        g2.drawString("Greetings, Humans", 20, 150);
    }
}