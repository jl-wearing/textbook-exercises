import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.Color;
import javax.swing.JComponent;

public class CenteredSquareComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Draw the shapes & add them to the component.
        Rectangle square = new Rectangle(100, 100, 200, 200);
        g2.setColor(Color.BLUE);
        g2.fill(square);

        //Re-size the square such that it is half its original length but has the same center.
        square.grow(-50, -50);

        //Add the shape to the component.
        g2.setColor(Color.YELLOW);
        g2.fill(square);
    }
}