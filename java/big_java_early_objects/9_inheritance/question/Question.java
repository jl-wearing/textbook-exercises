/**
 * A Question with a text and an answer.
 */

public class Question {
    private String text;
    private String answer;

    /**
     * Constructs a question with an empty question and answer.
     */
    public Question() {
        text = "";
        answer = "";
    }

    /**
     * Sets the question text.
     * @param questionText the text of this question.
     */
    public void setText(String questionText) { text = questionText.toLowerCase(); }

    /**
     * Sets the answer for this question.
     * @param correctAnswer the correct response.
     */
    public void setAnswer(String correctAnswer) { answer = correctAnswer.toLowerCase(); }

    /**
     * Checks a given response for correctness.
     * @param response the response to check.
     * @return true if the response was correct, false otherwise.
     */
    public boolean checkAnswer(String response) { return answer.equals(response.toLowerCase());}

    /**
     * Displays the question.
     */
    public void display() { System.out.println(Character.toTitleCase(text.charAt(0)) + text.substring(1)); }
}