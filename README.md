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

### Prerequisites

- Python3
- ANTLR 4

### Installation

1. **Install ANTLR 4:**
Run the following commands to download and set up ANTLR 4:

    ```sh
    pip install antlr4-tools
    antlr4
    pip install antlr4-python3-runtime
    ```

2. **Clone the repository:**
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
    - `car`, `cdr`, `cons`, `null?`, `append`, `length`
    - Types accepted: 
        - `any` ***(a non-list type will be treated as a one-element list containing that value).***
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
    - `define`
    - Types accepted: 
        - `any`
    - Types returned:
        - `nothing`
    - Example:
        ```scheme
        (define list '(1 2 3)) ; list = (1 2 3)
        (define x 10) ; x = 10
        ```

- **Function definitions and calls:**
    - `define`, function calls
    - Types accepted: 
        - `any`
    - Types returned:
        - `define` -> `nothing`
        - function calls -> `any`
    - Example:
        ```scheme
        (define (square x) (* x x))
        (square 4) ; 16
        ```

- **Conditional expressions:**
    - `if`, `cond`
    - Types accepted: 
        - `if` -> `boolean` `any` `any`
        - `cond` -> pairs of (`boolean` `any`)
    - Types returned:
        - `any`
    - Example:
        ```scheme
        (if (> 3 2) 'yes 'no) ; yes
        (cond ((> 3 2) 'yes) (else 'no)) ; yes
        ```

- **Let expressions:**
    - `let`
    - Types accepted: 
        - `any`
    - Types returned:
        - `any`
    - Example:
        ```scheme
        (let ((x 2) (y 3)) (+ x y)) ; 5
        ```

- **Input/Output operations:**
    - `read`, `display`
    - Types accepted: 
        - `any`
    - Types returned:
        - `display` -> `nothing`
        - `read` -> `any`
    - Example:
        ```scheme
        (display "Hello, World!")
        (display (read))
        ```

- **Other operations:**
    - `not`, `newline`, `set!`
    - Types accepted: 
        - `not` -> `boolean`
        - `others` -> `any`
    - Types returned:
        - `not` -> `boolean`
        - `others` -> `nothing`
    - Example:
        ```scheme
        (not #t) ; #f
        (newline) ; (display \n)
        (set! x 20) ; x = 20
        ```

These features provide a foundation for writing and evaluating simple Scheme programs using the mini Scheme interpreter.

## Acknowledgments

- [Jordi Petit - Exercise instructions](https://github.com/jordi-petit/lp-mini-scheme) 
for guiding in the practical exercises and providing helpful 
resources for implementation. 
- [ANTLR](https://www.antlr.org/) for providing the tool for 
language recognition.
- [Scheme Documentation](https://docs.scheme.org/) for official 
Scheme documentation.
