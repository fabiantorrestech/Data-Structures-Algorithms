//problem: https://www.hackerrank.com/challenges/frequency-of-digits-1/problem?isFullScreen=true

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

void printIntFrequency(int arr[]){
    
    for(int i=0;i<10;i++){
        printf("%d", arr[i]);
        if(i==9)
            continue;
        else
            printf(" ");
    }
}

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    
    char s[1000];       
    scanf("%s", s);     // take user input
    
    int numOccurences[10] = {0};  // create an array of zeroes to keep count of each digit
    
    for(int i=0; i<strlen(s); i++){
        if((s[i] > 47) && (s[i] < 58)){   // check that the character is a digit via ASCII value
            if(s[i] == '0')
                numOccurences[0]++;
            else if(s[i] == '1')
                numOccurences[1]++;
            else if(s[i] == '2')
                numOccurences[2]++;
            else if(s[i] == '3')
                numOccurences[3]++;
            else if(s[i] == '4')
                numOccurences[4]++;
            else if(s[i] == '5')
                numOccurences[5]++;
            else if(s[i] == '6')
                numOccurences[6]++;
            else if(s[i] == '7')
                numOccurences[7]++;
            else if(s[i] == '8')
                numOccurences[8]++;
            else if(s[i] == '9')
                numOccurences[9]++;
        }
        else{
            continue;
        }
    }

    printIntFrequency(numOccurences);
 
    return 0;
}
