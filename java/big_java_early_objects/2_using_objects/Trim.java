public class Trim {
    public static void main(String[] args) {
        //The trim() method is used to remove all trailing and leading spaces.
        String space = "    Coding is fun!   ";
        System.out.printf("***%s***\n", space);
        System.out.printf("***%s***\n", space.trim());
    }
}