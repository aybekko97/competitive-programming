#include <iostream>
using namespace std;

void print(int x) {
  // prints all 1's of x 
  // 7 => 0 1 2
  
  for(int i = 0; i < 32; i++) {
    if ((x & (1 << i)) > 0) 
      cout << i << " ";
  }
  cout << "\n";
}

int main() {
  int b = 0;
  int x = 1234;

  do {
    print(b);

    // DEBUG
    cout << "CURRENT";
    cout << " b=" << b; 
    cout << " b-x=" << b-x;
    cout << " x=" << x;
    cout << "\n";
         
  } while ((b=(b-x)&x));

}
