
#include <iostream>
#include <algorithm>
#include <vector>

bool myfunction(int i , int j) {
   return (i == j);
}

int main() {
  int myints[] = {5,20,5,30,30,20,10,10,20};
  std::vector<int> myvector(myints, myints+8);
  std::vector<int>::iterator it;

  it = std::adjacent_find(myvector.begin(), myvector.end());

  if(it != myvector.end())
    std::cout << "the first pair of repeated elements are :" << *it << '\n';

  // using predicate comparision:
  it = std::adjacent_find(++it, myvector.end(), myfunction);

  if(it != myvector.end())
    std::cout <<"the second pair of repated elements are: " << *it << '\n';

  return 0;
}
