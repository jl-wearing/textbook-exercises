import java.util.Scanner;

public class QuestionDemo1 {
    public static void main(String[] args) {
        Question q = new Question();
        q.setText("Who invented Java?");
        q.setAnswer("James Gosling");

        Scanner console = new Scanner(System.in);
        q.display();
        String answer = console.nextLine();
        if(q.checkAnswer(answer)) {
            System.out.println("Correct!");
        }
        else {
            System.out.println("Incorrect! The correct answer was James Gosling!");
        }
        console.close();
    }
}