[![Testing in Python with Pytest](https://tse4.mm.bing.net/th/id/OIP.b3eJha6Rm0Xvr6rnUl5yZQHaEK?pid=Api)](https://www.freecodecamp.org/news/testing-in-python-with-pytest/)

Here's a comprehensive documentation for your repository [KaiokkFernandes/Pytest](https://github.com/KaiokkFernandes/Pytest), emphasizing its role in your studies of Python testing and best practices:

---

# 🧪 Pytest Learning Repository

## Overview

This repository serves as a practical exploration of Python's testing capabilities, focusing on the **Pytest** framework. It encompasses various test cases and scenarios to understand:

* Unit testing fundamentals
* Test discovery and execution
* Assertions and exception handling
* Test organization and structure

## Repository Structure

```
Pytest/
├── UniTest/
│   ├── test_calculadora.py
│   └── calculadora.py
├── python-checkers/
│   ├── test_checkers.py
│   └── checkers.py
├── requirements.txt
└── .gitignore
```

* **UniTest/**: Contains tests for a calculator module, demonstrating basic arithmetic operation validations.
* **python-checkers/**: Includes tests for a checkers game logic, showcasing more complex test scenarios.
* **requirements.txt**: Lists the Python dependencies required to run the tests.

## Getting Started

### Prerequisites

* Python 3.8 or higher
* pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/KaiokkFernandes/Pytest.git
   cd Pytest
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Tests

Navigate to the directory containing the tests you wish to run and execute:

```bash
pytest
```

For example, to run tests in the `UniTest` directory:

```bash
cd UniTest
pytest
```

Pytest will automatically discover and run all test files matching the pattern `test_*.py`.

## Sample Test Case

Here's an example from `test_calculadora.py`:

```python
import pytest
from calculadora import soma

def test_soma_positivos():
    assert soma(2, 3) == 5
```

This test verifies that the `soma` function correctly adds two positive numbers.

## Learning Objectives

Through this repository, the following concepts are explored:

* Writing and organizing test cases using Pytest
* Understanding test discovery mechanisms
* Implementing assertions to validate code behavior
* Structuring tests for both simple and complex modules

## Contributions

As this is a personal learning project, contributions are not currently being accepted. However, feedback and suggestions are welcome!

