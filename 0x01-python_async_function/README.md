# Python - Async
In Python, **asynchronous programming** allows you to write code that can perform tasks concurrently, meaning multiple tasks can be initiated and run in parallel (though not necessarily at the same time) without blocking other tasks. This is useful for I/O-bound and high-level structured network code like web applications, web scraping, or API requests.

Python supports async programming primarily with the `asyncio` module and the `async`/`await` syntax introduced in Python 3.5. Here's an overview of how async works in Python and how to use it effectively.

## Resources

**Read or watch**:

-   [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/ "Async IO in Python: A Complete Walkthrough")
-   [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html "asyncio - Asynchronous I/O")
-   [random.uniform](https://docs.python.org/3/library/random.html#random.uniform"random.uniform")

## Learning Objectives

At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.alxswe.com/rltoken/RzzuxS2J7-SysSxP0Hu3cA "explain to anyone"),  **without the help of Google**:

-   `async`  and  `await`  syntax
-   How to execute an async program with  `asyncio`
-   How to run concurrent coroutines
-   How to create  `asyncio`  tasks
-   How to use the  `random`  module


# Overview
## Table of Contents
1. [Key Concepts](#features)
2. [Parallelism with  `asyncio.gather`](#installation)
3. [Parallelism with  `asyncio.gather`](#usage)
4. [Key Functions and Concepts in Async Python:](#configuration)
5. [Real-World Example: Async HTTP Requests](#contributing)
6. [Asyncio vs Multithreading vs Multiprocessing:](#license)
7. [Summary of Python Async:](#contact)

### Key Concepts:

1.  **`async` and `await`:**
    
    -   `async def`: Declares an asynchronous function (coroutine).
    -   `await`: Suspends the execution of the coroutine until the awaited result is ready (e.g., waiting for I/O to finish).
2.  **`asyncio` Library:**
    
    -   The `asyncio` library is the standard Python library for writing asynchronous programs. It provides event loops, coroutines, tasks, and I/O operations that work asynchronously.
3.  **Coroutines:**
    
    -   Coroutines are special functions that can be paused and resumed. When called, they return a coroutine object, which doesn't execute immediately. Execution starts when the coroutine is awaited.
4.  **Event Loop:**
    
    -   The event loop manages the execution of coroutines and ensures that they are run when their tasks are ready.

#### Simple Example of Async Programming in Python
```
import asyncio

# An asynchronous function (coroutine)
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # Simulate a network or I/O operation
    print("World")

# Running the coroutine
async def main():
    print("Start")
    await say_hello()  # This won't block
    print("End")

# Entry point for the event loop
asyncio.run(main())
```
#### Output:
```
Start
Hello
<1-second pause>
World
End
```
In this example, `asyncio.sleep(1)` suspends the execution of `say_hello` for 1 second without blocking the program. Other tasks can be processed during this pause.

### Parallelism with `asyncio.gather`

When you want to run multiple async tasks concurrently, you can use `asyncio.gather()` or `asyncio.create_task()`.

```
import asyncio

async def task_1():
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task_2():
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task_1(), task_2())  # Runs both tasks concurrently

asyncio.run(main())
```
#### Output:
```
Task 2 completed
Task 1 completed
```
Even though `task_1` takes longer to complete, both tasks are run concurrently and `task_2` finishes first.

### Key Functions and Concepts in Async Python:

1.  **`asyncio.run(coroutine)`**:
    
    -   Runs the coroutine and returns its result. It sets up the event loop, runs the coroutine, and closes the loop when done.
2.  **`asyncio.gather(*coroutines)`**:
    
    -   Runs multiple coroutines concurrently and waits for all of them to finish. It returns the results of all the coroutines in the same order they were passed.
3.  **`asyncio.create_task(coroutine)`**:
    
    -   Schedules the coroutine to be run in the event loop and returns a task object. You can use `await` on the task later or let it run in the background.
4.  **`await asyncio.sleep(seconds)`**:
    
    -   A non-blocking sleep. It suspends the coroutine and lets other coroutines run while waiting.
5.  **`asyncio.TimeoutError`**:
    
    -   Used when you want to limit the execution time of a coroutine. You can combine this with `asyncio.wait_for()` to apply time limits.

#### Example with Timeout:
```
import asyncio

async def long_running_task():
    await asyncio.sleep(5)
    return "Task completed"

async def main():
    try:
        result = await asyncio.wait_for(long_running_task(), timeout=3)
        print(result)
    except asyncio.TimeoutError:
        print("Task timed out!")

asyncio.run(main())
```

#### Output:
```
Task timed out!
```
The task takes 5 seconds, but the timeout is 3 seconds, so it raises a `TimeoutError`.

### Real-World Example: Async HTTP Requests

Using `aiohttp`, an asynchronous HTTP client, allows you to make multiple requests without waiting for each one to complete sequentially.
```
import aiohttp
import asyncio

async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    urls = [
        'https://www.example.com',
        'https://www.python.org',
        'https://www.github.com'
    ]
    
    # Fetch all URLs concurrently
    results = await asyncio.gather(*(fetch(url) for url in urls))
    
    for result in results:
        print(result[:100])  # Print the first 100 characters of each response

asyncio.run(main())
```
#### Output:
```
<!doctype html><html lang="en"><head><title>Example Domain</title>...
<!DOCTYPE html>
<html lang="en" class="js-focus-visible" dir="ltr"><head><meta charset...
<!DOCTYPE html><html lang="en" data-color-mode="auto" data-light-theme
```
In this example, `aiohttp` allows for concurrent HTTP requests, which are handled without blocking each other.

### Asyncio vs Multithreading vs Multiprocessing:

-   **Asyncio** is ideal for I/O-bound tasks (network requests, file I/O, database queries) where the tasks are more about waiting for operations to complete rather than consuming CPU resources.
-   **Multithreading** is better for CPU-bound tasks that require parallel execution across multiple cores.
-   **Multiprocessing** is used to run tasks across multiple CPU cores for heavy computational tasks but with more overhead than threading.

### Summary of Python Async:

-   Use `async` and `await` for non-blocking I/O operations.
-   Use `asyncio` to manage coroutines and event loops.
-   Ideal for I/O-bound tasks, not CPU-bound tasks.
-   Libraries like `aiohttp`, `aiomysql`, and `aioredis` offer asynchronous versions of common tasks such as HTTP requests, MySQL queries, and Redis interactions.

Async Python provides a powerful, efficient way to handle concurrent tasks without the complexity of threading, especially for I/O-bound applications.
