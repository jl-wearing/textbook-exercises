public class GenTest<T, U>{
    T first;
    U second;

    public GenTest(T a, U b){
        first = a;
        second = b;
    }

    public T getT(){
        return first;
    }

    public U getU(){
        return second;
    }

    public void setT(T a){
        first = a;
    }

    public void setU(U b){
        second = b;
    }

    @Override
    public String toString(){
        return "[" + this.first + "," + this.second + "]";
    }

    public static void main(String[] args){
        GenTest<String, Integer> pair = new GenTest<String, Integer>("Justin", 22);
        String result = pair.toString();
        System.out.println(result);
    }
}