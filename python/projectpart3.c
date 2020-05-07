// Project part 3: eval and type checking

// ------------------------------------------------------------

// Base Functionality 80 Points
// 1) The file has a main function only.
// 2) All of the statements and expressions are implemented.
// 3) eval works but the only way your program has output is
//    using a print statement.
// 4) No type checking, but your interpreter still never crashes.

int main() {

    int x;
    int y;
    bool z;

    x = 55;
    y = x * 8;
    z = true;
    z = !z + 33; // does not type check
    print(z);

    while (x > 0) {
        if (x % 2 == 0)
            print(x);
        x = x - 1;
    }
}

// -------------------------------------------------------------------------------

// Mid-level Functionality 90 Points
// 1) Functions are implemented (but no recursion)
// 2) Grammar needs to be extended with function call syntax
// 3) Static type checking works and type checking is done before eval is run.
// Hint: Each function has an environment that consists of the local declarations
// and parameters. An environment maps names (decls) to values (int, bool, float).
int f(int x) {
    return x*x;
}

int main() {
   int x;
   float y;
   bool z;
   x = f(33);  // <-- Need to add function call syntax

   // It is not hard to add function call syntax. It is just an identifier
   // followed by zero or more expressions separated by commas.

   y = x * 3.14;  // type checking. int * float is a float
   x = 3.14;      // convert to an int by truncating

   z = 3;              // type error because z is a boolean
   print(true && 5);   // type error

   x = "hello"; // Type error but the grammar disallows this

   print(f(f(33)));   // function composition should work
}

// Type checking rules
//  1) ints can be promoted to floats as needed in expressions;
//  2) assigning floats to ints, convert to an int and truncate
//  3) booleans are strict and not convertible to ints

// ----------------------------------------------------------------------

// Full Featured Functionality 100 points (design)
// Good design that is DRY and SOLID
// recursion works and mutual recursion works.

// compute x^y recursively
int exp(int x, int y) {
    if (y == 0)
        return 1;
    else
        return x*exp(x,y-1);
    print(y);
}

// Hint: Use a stack of environments (stack of dictionaries)
//       Essentially a list of dictionaries.
//       When a function is called a new dictionary is pushed on to the stack.

// Extra Credit
//   1) Exponentiation operator works  (5 points)
//   2) initializers on declarations (5 points)
//         int x = 33 * 99;

// Due final exam week when you make an appointment with me.

// Make a Zoom appointment Final Exam Week when all three team members can meet.

