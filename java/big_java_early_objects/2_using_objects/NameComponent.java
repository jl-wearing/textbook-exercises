import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JComponent;
import java.awt.Color;
import java.awt.Font;

public class NameComponent extends JComponent {
    public void paintComponent(Graphics g) {
        //Recover the Graphics2D object.
        Graphics2D g2 = (Graphics2D)g;

        //Change the font size.
        Font font = new Font("Serif", Font.PLAIN, 50);
        g2.setFont(font);

        //Draw the string.
        g2.setColor(Color.RED);
        g2.drawString("Justin", 100, 100);
    }
}