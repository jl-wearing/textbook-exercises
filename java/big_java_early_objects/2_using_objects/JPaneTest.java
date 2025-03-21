import javax.swing.JOptionPane;
import javax.swing.ImageIcon;
import java.net.URL;

public class JPaneTest{
    public static void main(String[] args) throws Exception {
        String name = JOptionPane.showInputDialog("Enter your name: ");
        JOptionPane.showMessageDialog(null, "Hello Justin", "Title", 0);

        URL imageLocation = new URL("https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png");
        JOptionPane.showMessageDialog(null, null, "Title", JOptionPane.PLAIN_MESSAGE, new ImageIcon(imageLocation));
    }
}