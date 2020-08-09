#include <ctime>
#include <iostream>
#include <assert.h>
#include "sort_util.h"
#include "algorithm.h"
using std::cout;
using std::endl;


int main(){
    int n=10000;
    int a[n];
    int min=0, max=100000;
    
    clock_t tic, toc;
    
    random_array(a, n, min, max);
    tic = clock();
    bubble_sort(a, n);
    toc = clock();
    assert (check_ascending(a, n-1)==1);
    cout << "elapsed time " << toc-tic << endl;
    
    random_array(a, n, min, max);
    tic = clock();
    select_sort(a, n);
    toc = clock();
    assert (check_ascending(a, n-1)==1);
    cout << "elapsed time " << toc-tic << endl;

    random_array(a, n, min, max);
    tic = clock();
    insert_sort(a, n);
    toc = clock();
    assert (check_ascending(a, n-1)==1);
    cout << "elapsed time " << toc-tic << endl;
    
    random_array(a, n, min, max);
    tic = clock();
    quick_sort(a, 0, n-1);
    toc = clock();
    cout << "elapsed time " << toc-tic << endl;
    assert (check_ascending(a, n-1)==1);
    
    return 0;
}
