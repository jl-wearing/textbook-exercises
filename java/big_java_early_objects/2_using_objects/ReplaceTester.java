public class ReplaceTester {
    public static void main(String[] args) {
        String river = "Mississippi";

        //Replace i with !
        river = river.replace('i', '!');
        //Replace s with $
        river = river.replace('s', '$');

        //Output
        System.out.printf("Actual result: %s\n", river);
        System.out.printf("Expected result: M!$$!$$!pp!\n");
    }
}