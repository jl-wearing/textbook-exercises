public class Mississippi {
    public static void main(String[] args) {
        String river = "Mississippi";
        river = river.replace("i", "ii");
        System.out.println(river);
        System.out.println(river.length() + " characters");

        System.out.println();
        river = river.replace("ss", "s");
        System.out.println(river);
        System.out.println(river.length() + " characters");
    }
}