# LP: ANTLR - MINI SCHEME

This project is focused on using ANTLR (Another Tool for Language Recognition) 
for language processing tasks. 
The goal is to create a small version of the Scheme programming language, 
which includes a subset of its syntax and features.

## Overview

This project involves building a mini Scheme interpreter that can parse, 
interpret, and evaluate expressions written in a reduced version of Scheme. 
It leverages ANTLR to generate a parser that understands the Scheme grammar, 
allowing us to build a functional interpreter.

### Architecture

The project is organized into the following key components:

- `scheme.g4`: The Scheme grammar written in ANTLR. It defines the syntax rules of the language.

- `scheme.py`: The main interpreter file, responsible for processing inputs and executing operations.

- `generated/`: Directory containing the files generated by ANTLR.
 
- `tests/`: A set of tests to validate the interpreter's functionalities.

### Architectural Design Choices

The design follows a **fully expression-based interpreter** approach without imposed limitations. All expressions can 
be combined with one another, provided no type errors occur. This flexible design ensures that the interpreter 
maintains the dynamic and versatile nature of the Scheme language.

A key design decision was to leverage the `begin` expression for implementing function code. This provides a consistent 
and intuitive structure for handling blocks of code in the interpreter, aligning with the principles of functional  
programming, while simplifying the visitor logic and avoiding potential conflicts in parsing nested expressions.

---
### Prerequisites

- [Python3](https://www.python.org/downloads/)
- [ANTLR 4](https://www.antlr.org/download.html)

### Installation
1. **Install Python3**
    ```sh
    sudo apt update
    sudo apt install python3
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
    Ensure your Makefile contains the following:

    <details>
    <summary>Makefile</summary>

    ```Makefile
    # Directories
    ANTL_DIR = generated
    TEST_DIR = tests

    # ANTLR settings
    ANTLR_CMD = antlr4
    GRAMMAR_FILE = scheme.g4

    all: antlr
        @echo "Running tests silently..."
        @python3 $(TEST_DIR)/tests.py --silent

    antlr:
        @echo "Generating ANTLR files..."
        @mkdir -p $(ANTL_DIR)
        @$(ANTLR_CMD) -Dlanguage=Python3 -no-listener -visitor $(GRAMMAR_FILE) -o $(ANTL_DIR)
        @echo "ANTLR files generated successfully."
        @echo ""

    tests: antlr
        @echo "Running tests..."
        @python3 $(TEST_DIR)/tests.py 

    clean:
        @echo "Cleaning ANTLR files..."
        @rm -rf $(ANTL_DIR)

    help:
        @echo "Available targets:"
        @echo "  all           - Generate ANTLR files and run tests silently"
        @echo "  tests         - Generate ANTLR files and run tests with output"
        @echo "  antlr         - Generate ANTLR files"
        @echo "  clean         - Clean generated ANTLR files"

    # Phony targets
    .PHONY: all antlr tests clean help
    ```

    </details>

    The project uses a Makefile to automate key tasks, such as generating ANTLR files, running tests, and cleaning up generated files.
    For more detailed information, you can run `make help`.

2. **Running the Interpreter**
    Once the parser and lexer have been generated, you can run the interpreter. 
    Ensure you have the necessary input files (such as input_file.scm) 
    to test the interpreter.
    ```sh
    python3 scheme.py path/to/input_file.scm
    ```

### Supported Features

The mini Scheme interpreter supports the following features:

- **Arithmetic operations:**
Perform mathematical calculations using operators like addition, subtraction, multiplication, and division. These operations can accept one or more numbers and return a single numeric result.
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
Enable comparisons between numbers, producing boolean results (#t or #f). The = operator also works with booleans.
    - `=`, `<`, `>`, `<=`, `>=`, `<>`
    - Types accepted: 
        - `number`
        - `=` -> `number` or `boolean`
    - Types returned:
        - `boolean`
    - Example:
        ```scheme
        (= 3 3) ; #t
        (< 2 5) ; #t
        ```

- **Logical operations:**
Combine or manipulate boolean values using logical operators like and, or, and more. The result is also a boolean.
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
Manipulate and query lists using operations like accessing elements, appending lists, and checking for null. ***(a non-list type will be treated as a one-element list containing that value).***
    - `car`, `cdr`, `cons`, `null?`, `append`, `length`
    - Types accepted: 
        - `any` 
    - Types returned:
        - `car`, `length` -> `number`
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
Define functions to encapsulate reusable logic and call them with arguments. Functions can accept any type of input and return any type of value.
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
Execute code conditionally based on boolean tests. Use if for single conditions or cond for multiple branches.
    - `if`, `cond`
    - Types accepted: 
        - `if` -> `boolean` `any` `any`
        - `cond` -> pairs of (`boolean` `any`)
    - Types returned:
        - `any`
    - Example:
        ```scheme
        (if (> 3 2) "yes" "no") ; yes
        (cond ((> 3 2) "yes") (else "no")) ; yes
        ```

- **Let expressions:**
Create local variables within a block and compute values using them. Returns the result of the last expression in the block.
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
    Allows you to execute multiple expressions sequentially outside of `main function`. Returns the result of the last executed expression.
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
Handle user interaction and display information in MiniScheme. The `read` operation reads input from the user, while `display` prints output to the console.
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

- **Other operations:**
Perform miscellaneous tasks such as logical negation (`not`), inserting new lines (`newline`), and updating variable values (`set!`).
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

These features provide a foundation for writing and evaluating simple Scheme programs using the mini Scheme interpreter.



### Quick reference
This menu provides an overview of all possible expressions and their usages. Use it as a quick reference:

<details>
<summary>Qucik Summary</summary>

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
| `=`              | `number`, `boolean` | `(= expression[2])`                              |
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
| `define`         | `any`               | `(define IDENTIFIER (IDENTIFIER[*]) expression)` |
| `if`             | `boolean` + `any` + `any` | `(if expression[3])`                       |
| `cond`           | pairs of (`boolean` + `any`) | `(cond (expression expression)[*])`     |
| `let`            | `any`               | `(let ((IDENTIFIER expression)[*]) expression )` |
| `begin`          | `any`               | `(begin expression[1..*])`                       |
| `read`           | `none`              | `(read)`                                         |
| `display`        | `any`               | `(display expression)`                           |
| `not`            | `boolean`           | `(not expression)`                               |
| `newline`        | `none`              | `(newline)`                                      |
| `set!`           | `any`               | `(set! IDENTIFIER expression)`                   |

- `[2..*]`: This notation indicates that the expression requires at least two arguments but can accept more.
 For example, `(+ 1 2)` and `(+ 1 2 3 4)` are both valid.
- `[1..*]`: This notation indicates that the expression requires at least one argument but can accept more. 
For example, `(begin (display "Hello") (+ 1 2))` is valid.
- `[2]`: This notation indicates that the expression requires exactly two arguments. For example, 
`(append '(1 2) '(3 4))` is valid.
- `[*]`: This notation indicates that the expression can accept any number of arguments, including none.
For example, `(cond ((> 3 2) "yes") (else "no"))` is valid and `(cond)` is valid and will do nothing.
- `IDENTIFIER` indicates a name that represents a variable or function. For example, `x`, `y`, or `fibonacci`.
</details>

## Acknowledgments

- [Jordi Petit - Exercise instructions](https://github.com/jordi-petit/lp-mini-scheme) 
for guiding in the practical exercises and providing helpful 
resources for implementation. 
- [ANTLR](https://www.antlr.org/) for providing the tool for 
language recognition.
- [Scheme Documentation](https://docs.scheme.org/) for official 
Scheme documentation.
