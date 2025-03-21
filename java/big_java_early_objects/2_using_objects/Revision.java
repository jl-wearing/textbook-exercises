public class Revision {
    public static void main(String[] args) {
        String river = "Shashe";
        System.out.printf("Length: %d\n", river.length());
        System.out.println(river.toUpperCase());
        System.out.println(river.toLowerCase());
        
        river = "Mississippi";
        System.out.println(river.replace("issipp", "our"));
        river = "aaaaa";
        System.out.println(river.replace("a", "z"));
    }
}
