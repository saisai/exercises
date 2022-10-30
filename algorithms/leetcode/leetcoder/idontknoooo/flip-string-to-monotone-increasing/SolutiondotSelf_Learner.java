
/*
 * https://leetcode.com/problems/flip-string-to-monotone-increasing/
 * https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/183855/Java-DP-solution-O(n)-time-O(1)-space
 */
class SolutiondotLearnerdotSelf_Learner {

    public static void main(String[] args){

        SolutiondotLearnerdotSelf_Learner S = new SolutiondotLearnerdotSelf_Learner();
        String s = "00110";
        System.out.println(S.minFlipsMonoIncr(s));


    }

    public int minFlipsMonoIncr(String s) {
        if(s == null || s.length() <= 1) return 0;
        int n = s.length();
        int cntEndWithOne = 0, cntEndWithZero = 0;

        for(int i= 0; i < n; i++) {
            char c = s.charAt(i);
            cntEndWithOne = Math.min(cntEndWithZero, cntEndWithOne) + (c == '1' ? 0: 1);
            cntEndWithZero += (c == '0' ? 0: 1);
        }
        return Math.min(cntEndWithOne, cntEndWithZero);
    }
}