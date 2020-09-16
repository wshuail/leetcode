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
    int min=0, max=2*n;
    
    clock_t tic, toc;
    
    cout << "bubble sort..." << endl;
    random_array(a, n, min, max);
    tic = clock();
    bubble_sort(a, n);
    toc = clock();
    assert (check_ascending(a, n-1)==1);
    cout << "elapsed time " << toc-tic << "\n" << endl;
    
    cout << "bubble sort..." << endl;
    random_array(a, n, min, max);
    tic = clock();
    select_sort(a, n);
    toc = clock();
    assert (check_ascending(a, n-1)==1);
    cout << "elapsed time " << toc-tic << "\n" << endl;

    cout << "insert sort..." << endl;
    random_array(a, n, min, max);
    tic = clock();
    insert_sort(a, n);
    toc = clock();
    assert (check_ascending(a, n-1)==1);
    cout << "elapsed time " << toc-tic << "\n" << endl;
    
    cout << "shell sort..." << endl;
    random_array(a, n, min, max);
    tic = clock();
    shell_sort(a, n);
    toc = clock();
    assert (check_ascending(a, n-1)==1);
    cout << "elapsed time " << toc-tic << "\n" << endl;
    
    cout << "quick sort..." << endl;
    random_array(a, n, min, max);
    tic = clock();
    quick_sort(a, 0, n-1);
    toc = clock();
    cout << "elapsed time " << toc-tic << "\n" << endl;
    assert (check_ascending(a, n-1)==1);
    
    cout << "heap sort..." << endl;
    random_array(a, n, min, max);
    tic = clock();
    heap_sort(a, n);
    toc = clock();
    cout << "elapsed time " << toc-tic << "\n" << endl;
    assert (check_ascending(a, n-1)==1);
    
    return 0;
}
