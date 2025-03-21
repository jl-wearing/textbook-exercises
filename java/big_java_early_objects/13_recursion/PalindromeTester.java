public class PalindromeTester {
    public static void main(String[] args) {
        String s = "racecar";
        System.out.printf("Is %s a palindrome: ", s);
        if(Palindromes.isPalindrome(s)) {
            System.out.printf("Yes it is!\n");
        }
        else {
            System.out.printf("No it is not!\n");
        }

        s = "Madam, I'm Adam!";
        System.out.printf("Is %s a palindrome?: %b\n", s, Palindromes.isPalindrome(s));
    }
}