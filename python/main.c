
float f(int n) {
     float z;
     // What is the "environment" in which we run f?

     z = 2.141;
     return 3.14159 * n * n + z;
}

int main() {
    int a;
    float b;
    bool c;

    b = f(21);  // 21 gets passed to n

    // a statement does not have a type, but the LHS and the RHS do have types
    // and those must "agree".
    a = 5;   // type check?

    // legal, truncate the value?
    a = a * 3.14159;  // warning. int(3.14159)   (int) 3.14159

    // int * float should be a float

    a = c;  // Illegal can't assign a bool to an int

    // condition should be a boolean
    // A statement "type checks" if all of the components type check
    if (a < 10 && c) {
        a = 0;
    }
}