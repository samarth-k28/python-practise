#include <iostream>
using namespace std;

int main(){
   vector <int> vector1{};
   vector <int> vector2{};
   vector1.push_back(69);
   vector1.push_back(20);
   vector2.push_back(100);
   vector2.push_back(200);
   cout << "first digit" << vector1.at(0) <<endl;
   cout << "second digit" << vector1.at(1) << endl;
   cout << vector1.size() << endl;
   cout << "first digit" << vector2.at(0) <<endl;
   cout << "second digit" << vector2.at(1) << endl;
   cout << vector2.size() << endl;
   vector <vector<int>> vector_2d{};
   vector_2d.push_back(vector1);
   vector_2d.push_back(vector2);
   cout << vector_2d.at(0).at(0) << endl;
   cout << vector_2d.at(1).at(1) << endl;



}