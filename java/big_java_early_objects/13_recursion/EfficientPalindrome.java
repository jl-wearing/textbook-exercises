public class EfficientPalindrome {
    public static boolean isPalindrome(String text) {
        return isPalindrome(text, 0, text.length() - 1);
    }

    private static boolean isPalindrome(String text, int start, int end) {
        if(text == null) {
            return false;
        }

        if(start >= end) {
            return true;
        }
        else {
            char first = Character.toLowerCase(text.charAt(0));
            char last = Character.toLowerCase(text.charAt(text.length() - 1));

            if(Character.isLetter(first) && Character.isLetter(last)) {
                if(first == last) {
                    return isPalindrome(text, start + 1, end - 1);
                }
                else {
                    return false;
                }
            }
            else if(!Character.isLetter(last)) {
                return isPalindrome(text, start, end - 1);
            }
            else {
                return isPalindrome(text, start + 1, end);
            }
        }
    }
}
