public class ObjectReference {
    public static void main(String[] args) {
        String river = "Mississippi";
        String str = river;
        river = river.replace("issipp", "our");
        System.out.println(river);
        System.out.println(str);
    }
}