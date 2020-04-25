// Project part 3: eval and type checking

// Base Functionality 80 Points
// main program (function) only and all of the statements and expressions
// are implemented. eval works and no type checking.

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

// Mid-level Functionality 90 Points
// We have functions (but no recursion)
// grammar needs to be extended with function call syntax
// static type checking works  typeof function
// Each function has an environment that consists of the local declarations
// and parameters. An environment maps names (decls) to values (int, bool, float).
int f(int x) {
    return x*x;
}

int main() {

   int x;
   float y;
   bool z;
   x = f(33);

   // not hard to add function call syntax identifier
   // followed ( zero or more expressions separated by commas )

   y = x * 3.14;

   x = 3.14;  // convert to an int and truncate

   z = 3; // type error
   print(true && 5);   // type error

   x = "hello"; // grammar disallows this

   print(f(f(33)));   // function composition should work

}

// Type checking
//  1) ints can be promoted to floats as needed in expressions;
//  2) assigning floats to ints, convert to an int and truncate
//  3) booleans are strict and not convertible to ints
//

// Full Featured Functionality 100 points (design)
// DRY, SOLID
// recursion works and mutual recursion works.

// compute x^y
int exp(int x, int y) {
    if (y == 0)
        return 1;
    else
        return x*exp(y-1);
    print(y);
}

// stack of environments (stack of dictionaries) a list of dictionaries

// last function called is the first to return. Stack


// Extra Credit
//   1) exponentiation operator works  (5 points)
//   2) initializers on declarations (5 points)
//         int x = 33 * 99;

// Due final exam week when you make an appointment with me.
// Make a Zoom appointment Final Exam Week when all three team members can meet.

