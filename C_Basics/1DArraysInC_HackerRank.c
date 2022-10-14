// https://www.hackerrank.com/challenges/1d-arrays-in-c/problem?isFullScreen=true

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void printIntArr(int arr[], int size){
    for(int i=0; i<size; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    int n;
    scanf("%d", &n);                            // getting input for size of the array
    
    int *arr = (int*)malloc(n * sizeof(int));   // creating int array with malloc
    int input;
    for(int i=0; i<n; i++){                     // getting input for the array
        scanf("%d", &input);
        arr[i] = input;
    }

    int sum = 0;
    for(int i=0; i< n; i++){                    // summing up the array
        sum += arr[i];
    }
    
    printf("%d", sum);                          // print the sum
    free(arr);                                  // free the memory used up by arr
    
    return 0;
}