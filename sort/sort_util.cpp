#include <iostream>
using std::cout;
using std::endl;


void random_array(int *a, int n, int min=0, int max=1000){
    for (int i=0; i<=n; i++){
        a[i] = rand()%(max-min+1)+min;
    }
}

void print_array(int *a, int length){
    for (int i=0; i<length; ++i){
        cout << a[i] << " ";
    }
    cout << endl;
}

bool check_ascending(int *a, int length){
    for (int i=0; i<length; ++i){
        if (a[i] > a[i+1]){
            return false;
        };
    }
    return true;
}

/*
int main(){
    int n = 10;
    int a[n];
    // int min=0, max=100;
    // random_array(a, n, min, max);
    random_array(a, n);
    print_array(a, n);
    return 0;
}
*/
