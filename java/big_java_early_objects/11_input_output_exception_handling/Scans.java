import java.util.Scanner;

public class Scans {
    public static void main(String[] args) {
        String str = "Mary had a little lamb.";
        Scanner in = new Scanner(str);

        while(in.hasNext()) {
            String word = in.next();
            System.out.println(word);
        }
        System.out.println();
        //The word lamb. contains a period because it is not white space.
        //The next() method returns any sequence of characters that is not white space.

        //Sometimes you want to read just the word and discard anything that is not whitespace.
        //You use the useDelimiter() method to achieve just that.
        in = new Scanner(str);
        in.useDelimiter("[^A-Za-z]+");
        while(in.hasNext()) {
            String word = in.next();
            System.out.println(word);
        }
        System.out.println();

        //Sometimes you want to read each character in a String.
        //This is achieved by setting the useDelimiterMethod() with an empty string "".
        in = new Scanner(str);
        in.useDelimiter("");
        while(in.hasNext()) {
            char ch = in.next().charAt(0);
            System.out.println(ch);
        }
    }
}