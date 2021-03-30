/*
 * clang++ -std=c++11 -g -o m helloworld.cc && ./m
 * */

#include <iostream>

using namespace std;

void test1()
{
    string s1="hello world; from cpp";
    cout<<s1<<endl;

    cout<<endl;
    for(auto& i : s1) {
        cout<<i<<endl;
    }
    cout<<endl;
}

int main(int argc, char** argv)
{
    test1();

    return 0;
}
