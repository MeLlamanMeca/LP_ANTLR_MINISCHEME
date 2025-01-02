# LP: ANTLR - Mini-Scheme

This project is focused on using ANTLR (Another Tool for Language Recognition) 
for language processing tasks. 
The goal is to create a small version of the Scheme programming language, 
which includes a subset of its syntax and features.

## Overview

This project involves building a Mini-Scheme interpreter that can parse, 
interpret, and evaluate expressions written in a reduced version of Scheme. 
It leverages ANTLR to generate a parser that understands the Scheme grammar, 
allowing us to build a functional interpreter.

### Architecture

The project is organized into the following key components:

- [`scheme.g4`](/scheme.g4): The Scheme grammar written in ANTLR. It defines the syntax rules of the language.

- [`scheme.py`](/scheme.py): The main interpreter file, responsible for processing inputs and executing operations.

- [`treeVisitor.py`](/treeVisitor.py): Contains the `TreeVisitor` class, which interprets and evaluates the parse
tree generated by ANTLR.

- [`myErrorListener.py`](/myErrorListener.py): Implements the `MyErrorListener` class for custom syntax error 
handling during parsing.

- `generated/`: Directory containing the files generated by ANTLR.
 
- `tests/`: A set of tests to validate the interpreter's functionalities.

### Architectural Design Choices

The design follows a **fully expression-based interpreter** approach without imposed limitations. All expressions can 
be combined with one another, provided no type errors occur. This flexible design ensures that the interpreter 
maintains the dynamic and versatile nature of the Scheme language.

A program **must** have a main function, otherwise it will do nothing. The main function is defined without parameters
and can contain an unlimited number of expressions.
```scheme
    (define (main)
    ...
    )
```

# Main Program Flow

## 1. Parsing the Input File
- The program starts by reading the input file passed as an argument (`file_name`) using `FileStream`.
- It then uses `schemeLexer` and `schemeParser`, both generated by ANTLR, to tokenize and parse the content.
- Any syntax errors are handled by the custom error listener `MyErrorListener`, which outputs a clear error 
message and stops the program execution.

## 2. Abstract Syntax Tree Generation
- The program generates a parse tree from ANTLR (`parser = schemeParser(token_stream)`).
- This parse tree is immediately passed to the `TreeVisitor` class, which acts as an interpreter for the 
Mini-Scheme language.

## 3. Interpretation and Evaluation
- The `TreeVisitor` class is responsible for visiting each node of the parse tree, interpreting, and evaluating 
the corresponding expressions.
- Example of specific implementations:
  - **Arithmetic operations:** Handled by `visitArithmeticExpression`.
  - **Conditional expressions:** Evaluated by `visitIfExpression` and `visitCondExpression`.
  - **Function management:** `visitDefineFunction` defines functions, and `visitFunctionCall` handles function calls.
  - **List management:** Handled by `visitListCreation`, `visitCarExpression`, `visitCdrExpression`, etc.

## 4. Error Handling
- The program utilizes `MyErrorListener` class to handle syntax errors during the parsing stage.
- Currently, there is no explicit semantic or runtime error handling.

## 5. Input/Output Management
- **Input:** The `visitReadExpression` function processes user input.
- **Output:** The `visitDisplayExpression` function print results to the console.

## 6. Execution Completion
- After processing all instructions in the `main` function of the Mini-Scheme file, the program completes its execution.

# Getting Started

### Prerequisites

- [Python3](https://www.python.org/downloads/)
- [ANTLR 4](https://www.antlr.org/download.html)
- [Make](https://www.gnu.org/software/make/)

### Installation
1. **Install Python3 and Make**
    ```sh
    sudo apt update
    sudo apt install python3
    sudo apt-get install make
    ```

2. **Install ANTLR 4:**
Run the following commands to download and set up ANTLR 4:

    ```sh
    pip install antlr4-tools
    antlr4
    pip install antlr4-python3-runtime
    ```

3. **Clone the repository:**
Clone this repository to your local machine:

    ```sh
    git clone https://github.com/mellamanmeca/LP_ANTLR_MINISCHEME.git
    cd LP_ANTLR_MINISCHEME
    ```

### Usage

1. **Generate Parser and Lexer:**
    To generate the parser and lexer from the grammar file, 
    run the following command:

    ```sh
    make antlr
    ```

    This command uses the provided Makefile to generate ANTLR files. 

    The project uses a Makefile to automate key tasks, such as generating ANTLR files, running tests, and cleaning 
    up generated files. For more detailed information, you can run `make help`.

2. **Running the Interpreter:**
    Once the parser and lexer have been generated, you can run the interpreter. 
    Ensure you have the necessary input files (such as input_file.scm) 
    to test the interpreter.
    ```sh
    python3 scheme.py path/to/input_file.scm
    ```

### Supported Features
For simplicity, in this implementation, we assume that semantic and type errors never occur. Should they arise,
the program’s behavior is undefined.
Similarly, we assume that runtime errors (such as division by zero, attempting to retrieve the cdr of an 
empty list, etc.) never occur. If they do, the program’s behavior is also undefined.

#### Data types

This project can work with the following data types:

- Numbers (ints): Whole numbers, positive or negative, without decimals.
- Strings (strings): A sequence of characters enclosed (or not) in quotation marks.
- Booleans (bools): Represents truth values; either true or false. Represented as #t and #f. Can also use `else`, 
which is a shorthand for the boolean value #f in conditional expressions, typically used in place of #t to indicate
the fallback or default option when no other condition is met.
- Lists (lists): Unordered collections of elements that can contain different types of data, including other lists.

#### Expressions
The Mini-Scheme interpreter supports the following expressions:

- **Arithmetic operations:**
Perform mathematical calculations using operators like addition, subtraction, multiplication, and division. 
These operations can accept two or more numbers and return a single numeric result.
    - `+`, `-`, `*`, `/`, `mod`, `^`, `max`, `min`
    - Types accepted: 
        - `number`
    - Types returned:
        - `number`
    - Example:
        ```scheme
        (+ 1 2) ; 3
        (+ 1 2 3) ; 6
        (mod 10 3) ; 1
        ```

- **Comparison operations:**
Enable comparisons between numbers, producing boolean results (#t or #f). The `=` operator also works with booleans.
    - `=`, `<`, `>`, `<=`, `>=`, `<>`
    - Types accepted: 
        - `number`
        - `=` -> `number` or `boolean` _(this is a **restrictive OR**, meaning you can only 
        compare **values of the same type**.)_
    - Types returned:
        - `boolean`
    - Example:
        ```scheme
        (= 3 3) ; #t
        (< 2 5) ; #t
        ```

- **Logical operations:**
Combine or manipulate boolean values using logical operators like `and`, `or`, and more. The result is also a boolean.
    - `and`, `or`, `nor`, `xor`, `nand`, `xnor`, `implies`
    - Types accepted: 
        - `boolean`
    - Types returned:
        - `boolean`
    - Example:
        ```scheme
        (and #t #f) ; #f
        (and #t #t #f) ; #f
        (or #t #f) ; #t
        ```

- **Type checking:**
Check if a given value belongs to a specific type (e.g., number, list, etc.).
    - `number?`, `boolean?`, `string?`, `list?`
    - Types accepted: 
        - `any`
    - Types returned:
        - `boolean`
    - Example:
        ```scheme
        (number? 123) ; #t
        (list? '(1 2 3)) ; #t
        ```

- **List operations:**
Manipulate and query lists using operations like accessing elements, appending lists, and checking for null. 
_(a **non-list type** will be treated as a **one-element list** containing that value)_.
    - `car`, `cdr`, `cons`, `null?`, `append`, `length`
    - Types accepted: 
        - `any` 
    - Types returned:
        - `car` -> `any`
        - `length` -> `number`
        - `cdr`, `cons`, `append` -> `list`
        - `null` -> `boolean`
    - Example:
        ```scheme
        (length 5) ; 1
        (car list) ; 1
        (append '(1 2) list) ; (1 2 1 2 3)
        ```

- **Global Variable definitions:**
Define global variables that can hold any type of value.
    - `define`
    - Types accepted: 
        - `any`
    - Types returned:
        - `none`
    - Example:
        ```scheme
        (define list '(1 2 3)) ; list = (1 2 3)
        (define x 10) ; x = 10
        ```

- **Function definitions and calls:**
Define functions to encapsulate reusable logic and call them with arguments. Functions can accept any type of input 
and return any type of value.
    - `define`, function calls
    - Types accepted: 
        - `any`
    - Types returned:
        - `define` -> `none`
        - function calls -> `any`
    - Example:
        ```scheme
        (define (square x) (* x x))
        (square 4) ; 16
        ```

- **Conditional expressions:**
Execute code conditionally based on boolean tests. Use `if` for single conditions or `cond` for multiple branches.
    - `if`, `cond`
    - Types accepted: 
        - `if` -> `boolean` + `any` + `any`
        - `cond` -> pairs of (`boolean` + `any`)
    - Types returned:
        - `any`
    - Example:
        ```scheme
        (if (> 3 2) "yes" "no") ; yes
        (cond ((> 3 2) "yes") (else "no")) ; yes
        ```

- **Let expressions:**
Create local variables within a expression and compute values using them.
    - `let`
    - Types accepted: 
        - `any`
    - Types returned:
        - `any`
    - Example:
        ```scheme
        (let ((x 2) (y 3)) (+ x y)) ; 5
        ```
- **Begin operation:** 
Allows you to execute multiple expressions sequentially. Returns the result of the last executed expression. 
(**Deprecated**)
    - `begin`
    - Types accepted:
        - `any`
    - Types returned:
        - `any`
    - Example:
        ```scheme
        (begin
            (display "Hello, World!")
            (+ 1 2)
        ) ; 3
        ```
- **Input/Output operations:**
Handle user interaction and display information in Mini-Scheme. The `read` operation reads input from the user, while 
`display` prints output to the standard output.
    - `read`, `display`
    - Types accepted: 
        - `display` -> `any`
        - `read` -> `none`
    - Types returned:
        - `display` -> `none`
        - `read` -> `any`
    - Example:
        ```scheme
        (display "Hello, World!")
        (display (read))
        ```
    ### Read formats:

    - **Number:** `42`, `12`.
    - **Single-word string:** `word`, `"hello"`.
    - **Multi-word string:** `"hello, world!"`, `"this is a string."`.
    - **List:** `'(1 2 3)`, `'( (1 2 3) 4 5 )`.

- **Other operations:**
Perform miscellaneous tasks such as logical negation (`not`), inserting new lines (`newline`), and updating variable 
values (`set!`).
    - `not`, `newline`, `set!`
    - Types accepted: 
        - `not` -> `boolean`
        - `set!` -> `any`
        - `newline` -> `none`
    - Types returned:
        - `not` -> `boolean`
        - `others` -> `none`
    - Example:
        ```scheme
        (not #t) ; #f
        (newline) ; (display \n)
        (set! x 20) ; x = 20
        ```

These features provide a foundation for writing and evaluating simple Scheme programs using the Mini-Scheme interpreter.


<details>
<summary>Quick Summary</summary>
This menu provides an overview of all possible expressions and their usages. Use it as a quick reference:

| Expression       | Accepted Parameters | Usage                                            |
|------------------|---------------------|--------------------------------------------------|
| `+`              | `number`            | `(+ expression[2..*])`                           |
| `-`              | `number`            | `(- expression[2..*])`                           |
| `*`              | `number`            | `(* expression[2..*])`                           |
| `/`              | `number`            | `(/ expression[2..*])`                           |
| `mod`            | `number`            | `(mod expression[2..*])`                         |
| `^`              | `number`            | `(^ expression[2..*])`                           |
| `max`            | `number`            | `(max expression[2..*])`                         |
| `min`            | `number`            | `(min expression[2..*])`                         |
| `=`              | `number` or `boolean` | `(= expression[2])`                            |
| `<`              | `number`            | `(< expression[2])`                              |
| `>`              | `number`            | `(> expression[2])`                              |
| `<=`             | `number`            | `(<= expression[2])`                             |
| `>=`             | `number`            | `(>= expression[2])`                             |
| `<>`             | `number`            | `(<> expression[2])`                             |
| `and`            | `boolean`           | `(and expression[2..*])`                         |
| `or`             | `boolean`           | `(or expression[2..*])`                          |
| `nor`            | `boolean`           | `(nor expression[2..*])`                         |
| `xor`            | `boolean`           | `(xor expression[2..*])`                         |
| `nand`           | `boolean`           | `(nand expression[2..*])`                        |
| `xnor`           | `boolean`           | `(xnor expression[2..*])`                        |
| `implies`        | `boolean`           | `(implies expression[2..*])`                     |
| `number?`        | `any`               | `(number? expression)`                           |
| `boolean?`       | `any`               | `(boolean? expression)`                          |
| `string?`        | `any`               | `(string? expression)`                           |
| `list?`          | `any`               | `(list? expression)`                             |
| `car`            | `any`               | `(car expression)`                               |
| `cdr`            | `any`               | `(cdr expression)`                               |
| `cons`           | `any`               | `(cons expression[2])`                           |
| `null?`          | `any`               | `(null? expression)`                             |
| `append`         | `any`               | `(append expression[2])`                         |
| `length`         | `any`               | `(length expression)`                            |
| `define` (function) | `any`         | `(define (IDENTIFIER[1..*]) expression[*])` |
| `define` (variable) | `any`            | `(define IDENTIFIER expression)`                 |
| `if`             | `boolean` + `any` + `any` | `(if expression[3])`                       |
| `cond`           | pairs of (`boolean` + `any`) | `(cond (expression expression)[*])`     |
| `let`            | `any`               | `(let ((IDENTIFIER expression)[*]) expression[*] )` |
| `read`           | `none`              | `(read)`                                         |
| `display`        | `any`               | `(display expression)`                           |
| `not`            | `boolean`           | `(not expression)`                               |
| `newline`        | `none`              | `(newline)`                                      |
| `set!`           | `any`               | `(set! IDENTIFIER expression)`                   |
| `main`           | `any`               | `(define (main) expression[*])`                  |
| `begin`          | `any`               | `(begin expression[*])`                          |

- `[2..*]`: This notation indicates that the expression requires at least two arguments but can accept more.
 For example, `(+ 1 2)` and `(+ 1 2 3 4)` are both valid.
- `[2]`: This notation indicates that the expression requires exactly two arguments. For example, 
`(append '(1 2) '(3 4))` is valid.
- `[*]`: This notation indicates that the expression can accept any number of arguments, including none.
For example, `(cond ((> 3 2) "yes") (else "no"))` is valid and `(cond)` is valid and will do nothing.
- `IDENTIFIER` indicates a name that represents a variable or function. For example, `x`, `y`, or `fibonacci`.
</details>

# Test Sets

Test sets are essential to ensure that the Mini-Scheme interpreter works correctly. These test sets cover a variety 
of cases, ranging from basic arithmetic operations to evaluating conditional expressions and manipulating lists.

### Structure of the Test Sets

The test sets are organized in the `tests/` directory and are divided into different files based on the type of test. 
Each file contains multiple test cases that verify different aspects of the interpreter. In this folder, there is 
also a `tests.py` file which is responsible for executing all the tests and providing a confirmation response.

Each test set consists of an input `.csm` file (located in the `/input/` folder) and an expected output `.out` file 
(located in the `/output/` folder). Additionally, there is a special test in the `/iotest/` folder to check 
input-output interactions.

### Running the Tests

To execute the test sets, use the following command:

```sh
make tests
```

This command will run the `tests.py` file and display the results in the console, confirming whether the tests have
succeeded or failed. If any tests fail, the output will provide detailed information to help debug the issue.

## Acknowledgments

- [Jordi Petit - GitHub](https://github.com/jordi-petit/lp-mini-scheme) 
for guiding in the practical exercises and providing helpful 
resources for implementation. 
- [ANTLR](https://www.antlr.org/) for providing the tool for 
language recognition.
- [Scheme Documentation](https://docs.scheme.org/) for official 
Scheme documentation.
