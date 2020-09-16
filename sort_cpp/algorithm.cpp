#include <iostream>
#include "sort_util.h"
using std::cout;
using std::endl;

void swap(int &a, int &b){
    int tmp = a;
    a = b;
    b = tmp;
}

void bubble_sort(int a[], int length){
    for (int i=0; i<length; ++i){
        for (int j=0; j<length-i-1; j++){
            if (a[j] > a[j+1]){
                swap(a[j], a[j+1]);
            }
        }
    }
}

void select_sort(int a[], int length){
    for (int i=0; i<length; ++i){
       int index = i;
       for (int j=index; j<length; ++j){
           if (a[j] < a[index]){
               swap(a[j], a[index]);
           }
       }
       ++index;
    }
}

void insert_sort(int a[], int length){
    for (int i=1; i<length; ++i){
        int key = a[i];
        int j = i-1;
        while (j>=0 && a[j]>key){
            a[j+1] = a[j];
            --j;
        }
        a[j+1] = key; //j+1 because alread --j
    }
}


void shell_sort(int a[], int length){
    int i, j, gap;
    for (gap=length/2; gap>0; gap/=2){
        for (i=gap; i<length; ++i){
            for (j=i-gap; j>=0 && a[j]>a[j+gap]; j-=gap){
                swap(a[j], a[j+gap]);
            }
        }
    }
}


void quick_sort(int a[], int left, int right){
    if (left < right){
        int anchor = a[right];
        int i = left;
        for (int j=left; j<right; ++j){
            if (a[j] <= anchor){
                swap(a[j], a[i]);
                ++i;
            }
        }
        swap(a[right], a[i]);
        
        quick_sort(a, left, i-1);
        quick_sort(a, i+1, right);
    }
}


void max_heap(int a[], int length, int i){
    int left = 2*i+1;
    int right = 2*i+2;
    int largest = i;
    if (left < length && a[largest] < a[left]){
        largest = left;
    }
    if (right < length && a[largest] < a[right]){
        largest = right;
    }
    if (largest != i){
        swap(a[largest], a[i]);
        max_heap(a, length, largest);
    }
    
}

void heap_sort(int a[], int length){
    for (int i=length/2-1; i>=0; --i){
        max_heap(a, length, i);
    }
    for (int i=length-1; i>0; --i){
        swap(a[i], a[0]);
        max_heap(a, i, 0);
    }
}


