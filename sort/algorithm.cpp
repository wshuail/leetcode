#include <iostream>
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











