import javax.swing.JComponent;
import java.awt.Rectangle;
import java.awt.Graphics;
import java.awt.Graphics2D;

public class RectangleComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //The draw() method of the Graphics2D class is used to add a drawing to a component.
        Rectangle box = new Rectangle(5, 5, 50, 75);
        g2.draw(box);

        //The translate() method alters the location of a Rectangle.
        box.translate(25, 25);
        g2.draw(box);
    }
}