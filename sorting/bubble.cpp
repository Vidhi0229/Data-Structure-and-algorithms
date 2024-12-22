#include <iostream>
#include <vector>
void swap(int *a, int *b);
using namespace std;

int main(){
    vector <int> v = {25, 11, 9, 2, 55, 4, 26, 7};
    int n = v.size();
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n-1; j++){
            if(v[j] >= v[j+1]){
                swap(&v[j], &v[j+1]);
            }
            else{
                continue;
            }
        }
    }

    for(auto i : v){
        cout << i << " ";
    }
}

void swap(int *a, int *b){
    int c = *a;
    *a = *b;
    *b = c;
}

