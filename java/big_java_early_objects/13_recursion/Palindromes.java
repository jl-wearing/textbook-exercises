public class Palindromes {
    public static boolean isPalindrome(String s) {
        if(s == null) { return false; }

        if(s.length() <= 1) { return true; }

        char first = Character.toLowerCase(s.charAt(0));
        char last = Character.toLowerCase(s.charAt(s.length() - 1));
        if(Character.isLetter(first) && Character.isLetter(last)) {
            if(first == last) {
                return isPalindrome(s.substring(1, s.length() - 1));
            }
            else {
                return false;
            }
        }
        else if(!Character.isLetter(last)) {
            return isPalindrome(s.substring(0, s.length() - 1));
        }
        else if (!Character.isLetter(first)) {
            return isPalindrome(s.substring(1));
        }
        return false;
    }
}