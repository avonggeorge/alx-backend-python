# Unittests and Integration Tests

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code


In software testing, **Unit Tests** and **Integration Tests** serve different purposes and levels of code validation, focusing on ensuring the reliability and quality of individual parts of a program and how they work together. Here’s an overview of each type, when to use them, and how they differ.
In software testing, **Unit Tests** and **Integration Tests** serve different purposes and levels of code validation, focusing on ensuring the reliability and quality of individual parts of a program and how they work together. Here’s an overview of each type, when to use them, and how they differ.

----------

### 1. Unit Tests

**Definition**: Unit tests are designed to verify that individual components or "units" of a program (usually single functions or methods) work as expected, in isolation from other parts of the application.

**Key Characteristics**:

-   **Scope**: Limited to the smallest unit of code, like functions, methods, or classes.
-   **Isolation**: Tests only one function or method, often using mock objects or stubs to simulate dependencies.
-   **Speed**: Typically very fast, as they don’t involve external resources (e.g., databases or network).
-   **Goal**: Detect bugs early, ensuring each piece of code behaves correctly on its own.

**Example of Unit Testing (Python)**:

Suppose you have a function `add(a, b)` that simply returns the sum of `a` and `b`.
```
# Code to be tested
def add(a, b):
    return a + b

# Unit test
import unittest

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
```
In this example:

-   **Tests**: Each test case validates the `add` function for different inputs.
-   **Assertions**: We use `self.assertEqual` to ensure the function’s output matches expected results.
-   **Isolation**: The test doesn’t rely on any external dependencies or other functions.

**When to Use Unit Tests**:

-   Testing simple functions or methods.
-   Catching bugs early in the development process.
-   Ensuring refactored code hasn’t introduced any errors.
### 2. Integration Tests

**Definition**: Integration tests validate the interactions between different parts or modules of a system, ensuring they work together as expected. These tests go beyond individual functions, often involving a few components or layers of the application (e.g., database access, API calls).

**Key Characteristics**:

-   **Scope**: Focuses on how different modules work together.
-   **Dependencies**: May involve actual external dependencies, like a database or a third-party API.
-   **Complexity**: Generally more complex than unit tests since they require coordinating multiple components.
-   **Goal**: Detect issues in the interaction between integrated components.

**Example of Integration Testing (Python)**:

Suppose we have an application with a function `get_user_info` that retrieves user information from a database.
```
# Code to be tested
def get_user_info(user_id, db_connection):
    query = "SELECT * FROM users WHERE id = ?"
    return db_connection.execute(query, (user_id,)).fetchone()

# Integration test
import unittest
import sqlite3

class TestDatabaseIntegration(unittest.TestCase):
    def setUp(self):
        # Set up an in-memory SQLite database for testing
        self.db_connection = sqlite3.connect(":memory:")
        self.db_connection.execute("CREATE TABLE users (id INTEGER, name TEXT)")
        self.db_connection.execute("INSERT INTO users (id, name) VALUES (?, ?)", (1, "Alice"))
        self.db_connection.commit()

    def tearDown(self):
        # Close the database connection after each test
        self.db_connection.close()

    def test_get_user_info(self):
        # Check if the function retrieves the correct user information
        result = get_user_info(1, self.db_connection)
        self.assertEqual(result["name"], "Alice")

if __name__ == "__main__":
    unittest.main()
```
In this example:

-   **Setup**: The `setUp` method initializes an in-memory database with test data before each test.
-   **Teardown**: The `tearDown` method closes the database connection after each test to ensure no side effects.
-   **Interaction**: The test evaluates if `get_user_info` can correctly query and return information from the database, testing real database interaction.

**When to Use Integration Tests**:

-   Testing interactions with external dependencies like databases, APIs, or microservices.
-   Verifying if modules integrate well after updates or new feature additions.
-   Catching issues that might only appear when components work together.

### Key Differences Between Unit Tests and Integration Tests
| Aspect               | Unit Test                                      | Integration Test                               |
|----------------------|------------------------------------------------|------------------------------------------------|
| **Scope**            | Individual functions or methods                | Interactions between components or modules     |
| **Isolation**        | Isolated (often with mocks/stubs)              | Real dependencies or integration points        |
| **Speed**            | Fast                                           | Slower due to setup and dependency handling    |
| **Goal**             | Ensure each part works as expected             | Ensure parts work together correctly           |
| **Setup Complexity** | Minimal                                        | Higher, as dependencies need to be configured  |
| **Examples**         | Testing a single function or class             | Testing DB access, API endpoints, or module flows |


### Combining Unit Tests and Integration Tests

Both unit and integration tests are essential for a comprehensive testing strategy:

-   **Unit tests** help maintain individual code quality and are fast, giving immediate feedback.
-   **Integration tests** provide confidence in the system’s interconnectedness and reveal issues that may arise only when components interact.

A balanced approach is to have **many unit tests** for isolated functionality, supplemented by **fewer but focused integration tests** that cover critical interactions between components. This approach helps ensure both individual units and their combined workflows perform as expected, leading to a more robust application.

### Mocking, Parameterization and Fixtures
In automated testing, patterns like **mocking**, **parameterization**, and **fixtures** help streamline the process and improve the quality of tests. Here’s an overview of these patterns, how they work, and when to use them.
### 1. Mocking

**Definition**: Mocking involves creating "mock" objects that simulate the behavior of real objects. It allows you to test code in isolation by replacing external dependencies (like databases, APIs, or other functions) with mock versions.

**Purpose**:

-   Isolate the code under test.
-   Control and predict the behavior of dependencies.
-   Make tests faster by eliminating dependency on external resources.

**When to Use**:

-   When testing functions that depend on network calls, database queries, or file systems.
-   When you want to simulate specific responses from external dependencies, such as errors or delays.

**Example of Mocking (Python)**:
```
from unittest.mock import Mock

# Code to be tested
def get_weather(city, weather_api):
    response = weather_api.fetch(city)
    return response.get("temperature")

# Mocking the weather API
weather_api_mock = Mock()
weather_api_mock.fetch.return_value = {"temperature": 20}

# Test with the mock
temperature = get_weather("Lagos", weather_api_mock)
print(temperature)  # Outputs: 20
```
In this example:

-   We use `weather_api_mock` to simulate the behavior of an actual weather API.
-   The mock object is configured to return a predefined response (`{"temperature": 20}`), allowing the `get_weather` function to be tested without making a real API call.

----------

### 2. Parameterization

**Definition**: Parameterization is a technique where you run the same test with different sets of input values. This allows you to validate that the code behaves correctly across a range of inputs with a single test function.

**Purpose**:

-   Avoid code duplication in tests.
-   Increase test coverage by testing multiple scenarios.
-   Simplify adding and maintaining test cases with different inputs and expected outputs.

**When to Use**:

-   When you want to test a function with multiple input values.
-   When a function or method has a well-defined set of possible input/output pairs.

**Example of Parameterization (Python, using pytest)**:
```
import pytest

# Code to be tested
def add(a, b):
    return a + b

# Parametrized test function
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300)
])
def test_add(a, b, expected):
    assert add(a, b) == expected
```
In this example:

-   `@pytest.mark.parametrize` decorates the `test_add` function, allowing it to run with each tuple of `(a, b, expected)` values.
-   Each combination is treated as a separate test, helping validate that the `add` function works as expected for various inputs.

----------

### 3. Fixtures

**Definition**: Fixtures provide a setup and teardown mechanism for preparing test environments. They allow you to set up the state needed for tests and clean it up afterward, which helps maintain consistent and isolated test environments.

**Purpose**:

-   Share common setup code among tests.
-   Maintain clean test code by separating setup and teardown logic.
-   Provide a structured way to handle resource-intensive setups, like databases or configurations.

**When to Use**:

-   When tests need a specific setup that’s complex or time-consuming, like database connections.
-   When multiple tests need similar preparation steps.
-   When you want to ensure tests don’t affect each other by using isolated setups.

**Example of Fixtures (Python, using pytest)**:
```
In this example:

-   `@pytest.mark.parametrize` decorates the `test_add` function, allowing it to run with each tuple of `(a, b, expected)` values.
-   Each combination is treated as a separate test, helping validate that the `add` function works as expected for various inputs.

----------

### 3. Fixtures

**Definition**: Fixtures provide a setup and teardown mechanism for preparing test environments. They allow you to set up the state needed for tests and clean it up afterward, which helps maintain consistent and isolated test environments.

**Purpose**:

-   Share common setup code among tests.
-   Maintain clean test code by separating setup and teardown logic.
-   Provide a structured way to handle resource-intensive setups, like databases or configurations.

**When to Use**:

-   When tests need a specific setup that’s complex or time-consuming, like database connections.
-   When multiple tests need similar preparation steps.
-   When you want to ensure tests don’t affect each other by using isolated setups.

**Example of Fixtures (Python, using pytest)**:
```
In this example:

-   The `setup_data` fixture provides input values (`a`, `b`, and `expected`) that the test needs.
-   `test_add_with_fixture` calls the fixture implicitly by using it as an argument, and pytest automatically injects the fixture’s data.
-   Fixtures ensure the setup is reusable across multiple tests if needed, making tests cleaner and reducing repetition.

----------

### Summary Table of Mocking, Parameterization, and Fixtures
| Pattern           | Purpose                                         | When to Use                                          | Example Usage                                        |
|-------------------|-------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| **Mocking**       | Simulate dependencies for isolation             | For external APIs, databases, network dependencies   | Replace a database call with a mock object           |
| **Parameterization** | Run tests with multiple input values          | For testing functions with a variety of inputs       | Test math functions with different input sets        |
| **Fixtures**      | Set up and clean up test environments           | For complex or shared test setups                    | Create a test database connection for multiple tests |

Using these testing patterns strategically can significantly improve test quality, readability, and maintainability, helping you isolate bugs early and ensure code reliability across a range of scenarios.