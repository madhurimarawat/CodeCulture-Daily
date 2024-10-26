/*
In C++, the auto keyword is used for type inference, 
allowing the compiler to automatically deduce the type 
of a variable based on its initializer. 
This can make code more concise and readable, 
especially when dealing with complex types or generic programming.

Syntax:
auto variable_name = initializer;


*/

// C++ Program to demonstrate Basic Usage of auto keyword
#include<iostream>
#include<typeinfo>
using namespace std;

int main(){

    // Using auto for basic data type 

    // i will be automatically deduced as int
    // We do not specify the data type
    auto i = 5;

    // f will be automatically deduced as double
    // We do not specify the data type
    auto f = 5.6;

    // c will be automatically deduced as const char(String)
    // We do not specify the data type
    auto str = "Hello";

    // Seeing the Datatype

    /*
    It will print data type as follows:
    The type of 'i' is displayed as "i," which represents the integer type.
    The type of 'f' is displayed as "d," which represents the double type.
    The type of 'str' is displayed as "PKc," where "P" represents a pointer and "Kc" represents a constant character string (const char*).
    */
    
    cout << "The type of 'i' is: " << typeid(i).name() <<endl;
    cout << "The type of 'i' is: " << typeid(f).name() <<endl;
    cout << "The type of 'i' is: " << typeid(str).name() <<endl;





}