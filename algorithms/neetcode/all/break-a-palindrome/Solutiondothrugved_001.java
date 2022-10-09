
class Solutiondothrugved_001 {

    public static void main(String[] args) {

        Solutiondothrugved_001 S = new Solutiondothrugved_001();
        String palindrome = "abccba";
        System.out.println(S.breakPalindrome(palindrome));

    }

    public String breakPalindrome(String palindrome) {
        if(palindrome.length() == 1) return "";
        char[] op = palindrome.toCharArray();
        int i = 0;
        int j = op.length - 1;
        while(i < j) {
            if(op[i] == op[j]) {
                char c = op[i];
                op[i] = 'a';
                String comp = new String(op);
                if(comp.compareTo(palindrome) < 0) {
                    return comp;
                } else {
                    op[i] = c;
                }
            }
            i++;
            j--;
        }
        if(new String(op).equals(palindrome)) {
            op[op.length - 1] ='b';
        }
        return new String(op);
    }
}