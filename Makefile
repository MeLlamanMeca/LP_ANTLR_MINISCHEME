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