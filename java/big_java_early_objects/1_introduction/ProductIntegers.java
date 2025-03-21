//E1.3

public class ProductIntegers{
    public static void main(String[] args){
        int prod = ProductIntegers.product(1, 10);
        System.out.println(prod);

    }

    public static int product(int start, int end){
        if(start == end){
            return start;
        }
        
        return start * product(start + 1, end);
    }
}