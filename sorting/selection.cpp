#include <bits/stdc++.h>
void swap(int *a, int *b);
using namespace std;

int main(){
    vector <int> v = {25, 11, 9, 2, 55, 4, 26, 7};
    int n = v.size();

    for(int i = 0; i < n; i++){
        auto j = min_element(v.begin()+i, v.end());
        swap(&v[i],  &(*j));
        
    }

    for(auto i : v){
        cout << i << " ";
    }
}

void swap(int *a,  int *b){
    int c = *a;
    *a = *b;
    *b = c;
}

