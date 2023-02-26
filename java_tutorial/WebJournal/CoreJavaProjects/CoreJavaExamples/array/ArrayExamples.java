
import java.util.Arrays;

public class ArrayExamples{
    
    public static void main(String[] args) {
        String str = "journaldev.com";
        char[] charArr = str.toCharArray();

        System.out.println("String converted to char Array: " + Arrays.toString(charArr));

        String str1 = new String(charArr);
        System.out.println("char array converted to string: " + str1);

        System.out.println("str == str1 ? " + (str == str1));
        System.out.println("str.equals(str1)? " + (str.equals(str1)));
    }
}
