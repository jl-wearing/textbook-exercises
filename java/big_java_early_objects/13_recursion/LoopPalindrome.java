public class LoopPalindrome {
    public static boolean isPrime(String text) {
        int start = 0;
        int end = text.length() - 1;
        while(start < end) {
            char first = Character.toLowerCase(text.charAt(start));
            char last = Character.toLowerCase(text.charAt(end));

            if(Character.isLetter(start) && Character.isLetter(last)) {
                if(first == last) {
                    start++;
                    end--;
                }
                else {
                    return false;
                }
            }
            if(!Character.isLetter(last)) {
                end--;
            }
            if(!Character.isLetter(first)) {
                start++;
            }
        }
        return true;
    }
}