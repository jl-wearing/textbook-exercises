import java.math.BigInteger;

public class BigDigits {
    public static void main(String[] args) {
        BigInteger a = new BigInteger("12345678987654321");

        //Square of a.
        System.out.println(a.pow(2));
        //Fourth power of a.
        System.out.println(a.pow(4));
        //Eighth power of a.
        System.out.println(a.pow(8));
    }
}