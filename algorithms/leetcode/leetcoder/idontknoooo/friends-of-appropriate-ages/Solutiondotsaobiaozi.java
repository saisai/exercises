
class Solutiondotsaobiaozi {

    public static void main(String[] args){

        Solutiondotsaobiaozi S = new Solutiondotsaobiaozi();
        int[] ages = {16,17,18};
        System.out.println(S.numFriendRequests(ages));

    }

    public int numFriendRequests(int[] ages) {
        int res = 0;
        int[] numInAge = new int[121], suminAge = new int[121];
        for(int i: ages){
            numInAge[i]++;
        }

        for(int i = 1; i <= 120; ++i) {
            suminAge[i] = numInAge[i] + suminAge[i-1];
        }

        for(int i = 15; i <= 120; ++i){
            if(numInAge[i]==0) continue;
            int count = suminAge[i] - suminAge[i / 2 + 7];
            res += count * numInAge[i] - numInAge[i]; //people will not friend request themselves, so  - numInAge[i]
        }
        return res;
    }
}