# Makefile for ms.homeserver Ansible Collection
# 
# Python Version Requirements:
# - Ansible 2.15: Python 3.9+
# - Ansible 2.16+: Python 3.10+

.PHONY: help build test lint clean install check-syntax validate ci-local

# Default target
help:
	@echo "Available targets:"
	@echo "  build        - Build the collection archive"
	@echo "  test         - Run integration tests"
	@echo "  lint         - Run ansible-lint"
	@echo "  yamllint     - Run yamllint"
	@echo "  clean        - Clean build artifacts"
	@echo "  install      - Install collection locally"
	@echo "  install-deps - Install development dependencies"
	@echo "  check-syntax - Check YAML syntax"
	@echo "  validate     - Validate collection structure"
	@echo "  all          - Run all checks (lint, syntax, test)"
	@echo "  ci-local     - Run CI pipeline locally"
	@echo "  release      - Prepare for release"
	@echo ""
	@echo "Python/Ansible compatibility:"
	@echo "  Ansible 2.15: Python 3.9+"
	@echo "  Ansible 2.16+: Python 3.10+"

# Variables
COLLECTION_NAME = ms-homeserver
VERSION = $(shell grep "^version:" galaxy.yml | awk '{print $$2}')
ARCHIVE = $(COLLECTION_NAME)-$(VERSION).tar.gz

# Build collection
build:
	@echo "Building collection $(COLLECTION_NAME) version $(VERSION)..."
	ansible-galaxy collection build --force
	@echo "Collection built: $(ARCHIVE)"

# Run yamllint
yamllint:
	@echo "Running yamllint..."
	yamllint .

# Run linting
lint:
	@echo "Running ansible-lint..."
	ansible-lint .

# Check YAML syntax
check-syntax:
	@echo "Checking YAML syntax..."
	find . -path "./tests/*.yml" -o -path "./examples/*.yml" | xargs -I {} ansible-playbook --syntax-check {}

# Validate collection
validate:
	@echo "Validating collection structure..."
	ansible-galaxy collection build --force > /dev/null
	@echo "Collection structure is valid"

# Run tests
test:
	@echo "Running integration tests..."
	ansible-playbook tests/integration.yml

# Install collection locally
install: build
	@echo "Installing collection locally..."
	ansible-galaxy collection install $(ARCHIVE) --force

# Clean build artifacts
clean:
	@echo "Cleaning build artifacts..."
	rm -f *.tar.gz
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true

# Run all checks
all: yamllint lint check-syntax validate test
	@echo "All checks completed successfully!"

# Run CI pipeline locally
ci-local: clean yamllint lint check-syntax validate build test
	@echo "Local CI pipeline completed successfully!"

# Development setup
install-deps:
	@echo "Setting up development environment..."
	@echo "Note: For Ansible 2.16+, Python 3.10+ is required"
	pip install ansible-lint yamllint
	ansible-galaxy collection install ansible.posix community.general

# Development setup (alias)
dev-setup: install-deps

# Format YAML files
format:
	@echo "Formatting YAML files..."
	find . -name "*.yml" -o -name "*.yaml" | xargs prettier --write || echo "prettier not found, skipping formatting"

# Prepare for release
release: clean all build
	@echo "Release preparation completed!"
	@echo "Archive ready: $(ARCHIVE)"
	@echo "To create a release:"
	@echo "  1. Update CHANGELOG.md"
	@echo "  2. Commit changes"
	@echo "  3. Create tag: git tag v$(VERSION)"
	@echo "  4. Push tag: git push origin v$(VERSION)"

# Security check
security:
	@echo "Running security checks..."
	@command -v safety >/dev/null 2>&1 && safety check || echo "safety not installed, skipping"
	@command -v bandit >/dev/null 2>&1 && bandit -r . || echo "bandit not installed, skipping"
