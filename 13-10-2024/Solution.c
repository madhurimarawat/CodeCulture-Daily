/**
 * @file Solution.c
 * @brief This program performs arithmetic operations on complex numbers.
 *
 * This program allows users to perform addition, subtraction, multiplication,
 * and division on complex numbers. It takes two complex numbers as input
 * (each having a real and an imaginary part) and allows the user to choose
 * which operation to perform via a menu.
 *
 * Complex numbers are represented as (a + bi) where `a` is the real part
 * and `b` is the imaginary part. The program includes a simple menu that
 * allows users to perform one of the following operations:
 * - Addition
 * - Subtraction
 * - Multiplication
 * - Division
 *
 * The program will continue to prompt the user to choose operations until
 * they choose to exit.
 *
 * @author Madhurima Rawat
 * @date 13 October 2024
 */

// Including Header Files
#include <stdio.h>
#include <string.h>
#include <ctype.h>

// Function for Printing Result
void print_Result(int real, int imag)
{

    printf("\nResult is: %d + %di\n", real, imag);
}

// Function for Addition
void complex_Addition(int a, int b, int c, int d)
{

    // Variables for Storing Result
    int real = a + c;
    int imag = b + d;

    // Calling Print Function
    print_Result(real, imag);

    // A little humor
    printf("\nWhy did the complex number break up? It couldn't find a real solution!\n");
}

// Function for Subtraction
void complex_Subtraction(int a, int b, int c, int d)
{

    // Variables for Storing Result
    int real = a - c;
    int imag = b - d;

    // Calling Print Function
    print_Result(real, imag);

    // Another joke
    printf("\nWhy did the imaginary unit feel so lonely? It had no real friends!\n");
}

// Function for Multiplication
void complex_Multiplication(int a, int b, int c, int d)
{

    // Variables for Storing Result
    int real = (a * c) - (b * d);
    int imag = (a * d) + (b * c);

    // Calling Print Function
    print_Result(real, imag);

    // Yet another joke
    printf("\nWhat did one complex number say to the other? 'You complete me!'\n");
}

// Function for Division
// Formula is already derived and it is done using multiplication formula
// First, we multiply c - di as numerator and denominator
// Then we take the conjugate in the denominator and multiplication in the numerator
void complex_Division(int a, int b, int c, int d)
{

    // Variables for storing the result
    int real = 0, imag = 0;

    // Perform division
    int denominator = c * c + d * d;

    real = (a * c + b * d) / denominator;
    imag = (b * c - a * d) / denominator;

    // Calling Print Function
    print_Result(real, imag);

    // Adding a joke to lighten the mood
    printf("\nWhy was the complex number a good partner? It knew how to handle real and imaginary issues!\n");
}

// Function for Choice
// Menu Function
void choice(int option, int a, int b, int c, int d)
{

    // Switch case for different operations
    switch (option)
    {

    case 1:
        printf("\n****Complex Number Addition****");
        complex_Addition(a, b, c, d);
        break;

    case 2:
        printf("\n****Complex Number Subtraction****");
        complex_Subtraction(a, b, c, d);
        break;

    case 3:
        printf("\n****Complex Number Multiplication****");
        complex_Multiplication(a, b, c, d);
        break;

    case 4:
        printf("\n****Complex Number Division****");
        complex_Division(a, b, c, d);
        break;

    default:
        printf("Invalid choice!\n");
        break;
    }
}

/**
 * This program takes the real and imaginary parts of two complex numbers as input
 * and performs operations such as addition, subtraction, multiplication, and division
 * based on the user's choice. The user can continue choosing operations until
 * they decide to exit the program.
 */
int main()
{

    // Declaring Variables
    int a, b, c, d, option;

    printf("Enter the real and imaginary parts of the First Complex number: ");
    scanf("%d %d", &a, &b);

    printf("\nEnter the real and imaginary parts of the Second Complex number: ");
    scanf("%d %d", &c, &d);

    // Menu loop
    while (1)
    {

        // Displaying Menu
        printf("\nEnter the Operation Code for Operation else Press any other key to Exit...");
        printf("\n\nChoose operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n\nEnter choice: ");

        // Check if the input is an integer
        if (scanf("%d", &option) == 1)
        {

            if (option == 1 || option == 2 || option == 3 || option == 4)
            {

                // Perform the chosen operation
                choice(option, a, b, c, d);
            }
            else
            {
                // Exit the program if the choice is not in the valid range
                printf("\n...............Program Terminated Successfully...........\n");
                printf("<>>>>>>>>>>>>>>>>>@@@ Have a Good Day @@@>>>>>>>>>>>>>><>\n");
                break;
            }
        }
        else
        {
            // Clear the input buffer in case of non-integer input
            while (getchar() != '\n')
                ;
            printf("\nInvalid input. Please enter a valid integer.\n");
        }
    }

    return 0;
}
