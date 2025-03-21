import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.Color;
import javax.swing.JComponent;

public class GrowSquarePrinterComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Draw the square and add it to the component.
        Rectangle square = new Rectangle(100, 100, 100, 100);
        g2.setColor(Color.YELLOW);
        g2.fill(square);

        //Re-size the square and add it to the component.
        square.grow(-25, -25);
        square.translate(-25, -25);
        g2.setColor(Color.GREEN);
        g2.fill(square);
    }
}