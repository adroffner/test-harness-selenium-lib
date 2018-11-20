#! /bin/bash
#
# Run Quality Assurance Tests
# ============================================================================
# Run the unittests with nose & coverage.py
# ============================================================================

PYTHON=python3

$PYTHON ./setup.py nosetests --match='qa[_-].*'

echo
echo 'See unit test coverage:'
echo "file://$PWD/htmlcov/index.html"
echo
