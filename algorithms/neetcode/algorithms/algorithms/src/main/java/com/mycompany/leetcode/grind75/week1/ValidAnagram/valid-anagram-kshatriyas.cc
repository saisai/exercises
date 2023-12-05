
#include <iostream>
#include <algorithm>

using namespace std;

class Solution{
  public:
    bool isAnagram(string s, string t) {
      sort(s.begin(), s.end());
      sort(t.begin(), t.end());
      return s == t;
    }
};

int main(){
  Solution obj;;
  string s = "anagram", t = "nagaram";
  std::cout << obj.isAnagram(s, t);
}
