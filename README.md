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

- Java Development Kit (JDK) 8 or higher
- ANTLR 4

### Installation

1. **Install ANTLR 4:**
Run the following commands to download and set up ANTLR 4:

    ```sh
    curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar
    export CLASSPATH=".:/path/to/antlr-4.9.2-complete.jar:$CLASSPATH"
    alias antlr4='java -jar /path/to/antlr-4.9.2-complete.jar'
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

2. **Running the Interpreter**
Once the parser and lexer have been generated, you can run the interpreter. 
Ensure you have the necessary input files (such as input_file.scm) 
to test the interpreter.
```sh
python3 scheme.py your_file.scm
```

This project does not have a license. 
Please contact the repository owner for more information.

## Acknowledgments

- [Instrucciones de la práctica](https://github.com/jordi-petit/lp-mini-scheme) 
for guiding in the practical exercises and providing helpful 
resources for implementation.
- [ANTLR](https://www.antlr.org/) for providing the tool for 
language recognition.
- [Scheme Documentation](https://docs.scheme.org/) for official 
Scheme documentation.
