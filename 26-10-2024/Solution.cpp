// Program for Dutch National Flag Problem using Loop and Switch Case
/*

Suppose you have the input array: `[1, 0, 2, 1, 0, 2, 1, 0]`

The goal is to sort it in a way that all 0s come first, followed by all 1s, and then all 2s.

Here's how the algorithm works step by step:

1. **Initialization:** Start with three variables - `low`, `mid`, and `high`.
   - `low` initially points to the start of the array (index 0).
   - `mid` also starts at the beginning (index 0).
   - `high` initially points to the end of the array (index 7).

2. **Iteration:**
   - Begin iterating through the array with the `mid` pointer.
   - Check the value at `arr[mid]`:
      - If it's 0, swap `arr[mid]` with `arr[low]` and increment both `low` and `mid`.
      - If it's 1, no swapping is needed; just increment `mid`.
      - If it's 2, swap `arr[mid]` with `arr[high]` and decrement `high`.
      
      ** We do not increment the value of mid after swapping with high because we 
      want to check that the value is in terms with rules of array **

      ** In other words to ensure that even after swapping array will remain sorted **

3. **Repeat Until Mid Exceeds High:**
   - Keep iterating until `mid` crosses or equals `high`.

4. **Final Sorted Array:**
   After the single traversal, the array will be sorted as follows:
   `[0, 0, 0, 1, 1, 1, 2, 2]`

Explanation:
- During the traversal, the algorithm moves all 0s to the beginning, 1s to the middle, and 2s to the end, 
resulting in the desired sorted order.

This algorithm is efficient because it sorts the array in a single pass, making it a good solution for 
scenarios where we need to minimize the number of iterations through the array.

*/

#include<iostream>
using namespace std;


// For Swapping Elements
void swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}

// For Printing Array
void print(int arr[], int n){
    for(int i = 0; i < n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main(){

    // Printing Statement
    cout<<"Dutch National Flag Problem in Array"<<endl;

    // Declaring Array
    int arr[] = {1, 1, 0, 2, 1, 2, 0};

    // Declaring Variables
    int n = 7; // Change here: Correct the size of the array
    int i = 0;

    cout<<"\nArray Before Sorting is:\n";
    print(arr,n);

    // Initializing three values
    int mid = 0, low = 0, high = n-1;


    // Using While loop
    while(mid <= high){

        // Using Switch Case
        switch(arr[mid]){

            // For Case 0 we Swap mid and low i.e add element at the start
            case 0:
                swap(arr[mid],arr[low]);
                low++;
                mid++;
                break;

            // For Case 1 we just increment mid as 1 is going to be the middle element
            case 1:
                mid++;
                break;

            // For Case 2 we Swap mid and high i.e add element at the end
            case 2:
                swap(arr[mid],arr[high]);
                high--;
                break;
        }

    }

    // Printing Array
    cout<<"\nArray after Sorting is:\n";
    print(arr,n);

    return 0;
}
