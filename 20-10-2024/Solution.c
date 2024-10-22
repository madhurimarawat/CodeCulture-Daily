// Program to See size of structure elements
#include<stdio.h>
#include<string.h>

// Declaring a Structure Student
struct student{
	char gender[10];
	int rollno;
	float marks;
	char name[20];
	char address[30];
};


int main(){

    // Declaring object/ instance of structure or structure variable
    struct student s1;

    // Passing Argument to Name
	strcpy (s1.name, "XYZ");

	s1.rollno = 90;
	s1.marks = 75;

    // Passing Argument to Gender
	strcpy(s1.gender, "Female");

    // Passing Argument to Address
	strcpy(s1.address, "Chhattisgarh");


	// Printing Variables
	printf("Roll Number is - %d \n", s1.rollno);
	printf("Marks is - %f \n", s1.marks);
    printf("Name is - %s \n", s1.name);
    printf("Gender is - %s \n", s1.gender);
    printf("Address is - %s \n", s1.address);
	

	printf("Size of Structure Member Roll Number(Integer) is: %d\n", sizeof(s1.rollno));
	printf("Size of Structure Member Marks(Float) is: %d\n", sizeof(s1.marks));
    printf("Size of Structure Member Name(String) is: %d\n", sizeof(s1.name));
	printf("Size of Structure Member Gender(String) is: %d\n", sizeof(s1.gender));
	printf("Size of Structure Member Address(String) is: %d\n", sizeof(s1.address));

	// It is the combined size of all structure elements
	printf("Size of Structure is: %d\n", sizeof(s1));
	
	return 0; 
}

/*

Let's break down the size calculation for the structure "student" in this program step by step:

```c
struct student {
    char gender[10];
    int rollno;
    float marks;
    char name[20];
    char address[30];
};
```

1. **Gender (char[10]):**
   - Size of a character is typically 1 byte.
   - 10 characters * 1 byte/character = 10 bytes.

2. **Roll Number (int):**
   - Size of an integer is typically 4 bytes.

3. **Marks (float):**
   - Size of a float is typically 4 bytes.

4. **Name (char[20]):**
   - Size of a character is 1 byte.
   - 20 characters * 1 byte/character = 20 bytes.

5. **Address (char[30]):**
   - Size of a character is 1 byte.
   - 30 characters * 1 byte/character = 30 bytes.

Now, let's add up the sizes of all the members:

- Size of Gender + Size of Roll Number + Size of Marks + Size of Name + Size of Address
  = 10 bytes + 4 bytes + 4 bytes + 20 bytes + 30 bytes
  = 68 bytes

Additionally, compilers may add padding to align data structures in memory for optimization 
purposes. In this case, the total size might be adjusted to meet alignment requirements. It 
seems that in your case, with padding considered, the total size is 72 bytes.

Keep in mind that the actual size of a structure can vary between different compilers and 
platforms due to alignment and padding considerations.

*/