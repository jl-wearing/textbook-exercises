import javax.swing.JOptionPane;

public class Dialog3{
    public static void main(String[] args){
        String name = JOptionPane.showInputDialog("What is your name?");
        JOptionPane.showMessageDialog(null, "My name is Hal! What would you like me to do?");
        JOptionPane.showMessageDialog(null, "I'm sorry Justin. I'm afraid I can't do that.");
    }
}