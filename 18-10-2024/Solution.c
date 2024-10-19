/*

Question: Find the Output of The following Code

enum{false, true};

int main(){

    int i = 1;

    do {
        printf("%d\n", i);
        i++;

        if (i < 15)

            continue;

        } while(false);

        getchar();

        return 0;
    
}

1. 2
2. 1
3. 4
4. 3

Correct Answer: 2. 1

*/

// Including Header Files
#include<stdio.h>
#include<stdlib.h>

// We need to declare enum else false will be undefined and 
// it will give error
// After this false corresponds to 0 and true corresponds to 1
// Making Enum
enum{false, true};

// Main function
int main(){

    int i = 1;

    do {
        printf("%d\n", i);
        i++;

        // If condition
        if (i < 15)

            continue;

        } while(false);

        getchar();

        return 0;
    
}

/* 

The Output will be 1 as only one time i will be printed
when the first time do is executed

After this false will be corresponding to 0 
thus it will not run and the loop will be stopped
*/