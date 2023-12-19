import os
import unittest
from bs4 import BeautifulSoup
import requests
from flask import Flask


# Lesson 1: Introduction to Python
# This class demonstrates basic Python concepts such as variables, data types, and control flow.
class BasicPython:
    def __init__(self):
        # Variables
        self.name = "John"
        self.age = 25

    def control_flow_example(self):
        # if-else statement
        if self.age >= 18:
            print("You are an adult.")
        else:
            print("You are a minor.")

        # for loop
        for i in range(5):
            print(i)

        # while loop
        count = 0
        while count < 5:
            print(count)
            count += 1


# Lesson 2: Functions and Modules
# This class demonstrates defining functions, using modules, and working with external libraries.
class FunctionsAndModules:
    def __init__(self):
        pass  # No initialization required for this example

    def greet(self, name):
        # Function definition
        return f"Hello, {name}!"

    def use_requests_library(self):
        # Using the requests library
        import requests
        response = requests.get('https://www.example.com')
        print(response.text)


# Lesson 3: Object-Oriented Programming (OOP)
# This class demonstrates the basics of OOP in Python, including class definition, instantiation, and method usage.
class OOPBasics:
    class Dog:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def bark(self):
            print("Woof!")

    def demonstrate_oop(self):
        # Object instantiation
        my_dog = self.Dog("Buddy", 3)

        # Accessing attributes and methods
        print(my_dog.name)
        my_dog.bark()


# Lesson 4: Data Structures - Lists, Dictionaries, Tuples
# This class demonstrates working with common data structures in Python.
class DataStructures:
    def __init__(self):
        pass  # No initialization required for this example

    def demonstrate_lists(self):
        # Creating a list
        my_list = [1, 2, 3, 'hello', True]

        # Accessing elements
        print(my_list[0])  # Output: 1

        # Slicing
        print(my_list[1:3])  # Output: [2, 3]

        # Modifying elements
        my_list[0] = 'one'

        # Adding elements
        my_list.append(4)

        # Removing elements
        my_list.remove('hello')

    def demonstrate_dictionaries(self):
        # Creating a dictionary
        my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

        # Accessing values
        print(my_dict['name'])  # Output: John

        # Modifying values
        my_dict['age'] = 26

        # Adding new key-value pairs
        my_dict['occupation'] = 'Developer'

        # Removing key-value pairs
        del my_dict['city']

    def demonstrate_tuples(self):
        # Creating a tuple
        my_tuple = (1, 2, 'three')

        # Accessing elements
        print(my_tuple[0])  # Output: 1

        # Tuple unpacking
        a, b, c = my_tuple


# Lesson 5: File Handling
# This class demonstrates reading from and writing to files in Python.
class FileHandling:
    def __init__(self):
        pass  # No initialization required for this example

    def read_from_file(self):
        # Reading from a file
        with open('example.txt', 'r') as file:
            content = file.read()
            print(content)

    def write_to_file(self):
        # Writing to a file
        with open('example.txt', 'w') as file:
            file.write('Hello, World!')


# Lesson 6: Exception Handling
# This class demonstrates handling exceptions in Python.
class ExceptionHandling:
    def __init__(self):
        pass  # No initialization required for this example

    def handle_exception(self):
        # Exception handling
        try:
            result = 10 / 0
        except ZeroDivisionError:
            print("Cannot divide by zero!")
        else:
            print(f"Result: {result}")
        finally:
            print("This will always execute.")


# Lesson 7: Virtual Environments
# This class demonstrates creating and activating virtual environments in Python.
class VirtualEnvironments:
    def __init__(self):
        pass  # No initialization required for this example

    def create_virtual_environment(self):
        # Creating a virtual environment
        import os
        os.system('python -m venv myenv')

    def activate_virtual_environment(self):
        # Activating the virtual environment
        # On Windows
        os.system('.\\myenv\\Scripts\\activate')
        # On Unix or MacOS
        os.system('source myenv/bin/activate')


# Lesson 8: Working with External Libraries - BeautifulSoup
# This class demonstrates web scraping with BeautifulSoup, an external library for parsing HTML.
class WebScrapingWithBeautifulSoup:
    def __init__(self):
        # Installing BeautifulSoup
        import os
        os.system('pip install beautifulsoup4')

    def web_scraping_example(self):
        # Using BeautifulSoup for web scraping
        from bs4 import BeautifulSoup
        import requests

        url = 'https://example.com'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extracting information
        title = soup.title.text
        print(f'Title: {title}')


# Lesson 9: Advanced Functions - Lambda Functions, Decorators
# This class demonstrates advanced functions in Python, including lambda functions and decorators.
class AdvancedFunctions:
    def __init__(self):
        pass  # No initialization required for this example

    def demonstrate_lambda_functions(self):
        # Lambda function
        multiply = lambda x, y: x * y
        result = multiply(3, 4)
        print(result)  # Output: 12

    def demonstrate_decorators(self):
        # Decorator
        def my_decorator(func):
            def wrapper():
                print("Something is happening before the function is called.")
                func()
                print("Something is happening after the function is called.")

            return wrapper

        @my_decorator
        def say_hello():
            print("Hello!")

        say_hello()


# Lesson 10: Generators
# This class demonstrates using generators in Python.
class Generators:
    def __init__(self):
        pass  # No initialization required for this example

    def generator_example(self):
        # Generator function
        def my_generator():
            for i in range(5):
                yield i

        # Using the generator
        for number in my_generator():
            print(number)


# Lesson 11: Context Managers
# This class demonstrates using context managers in Python.
class ContextManagers:
    def __init__(self):
        pass  # No initialization required for this example

    def context_manager_example(self):
        # Context manager
        with open('example.txt', 'r') as file:
            content = file.read()
            print(content)
        # File is automatically closed outside the block


# Lesson 12: Object-Oriented Programming (OOP) - Advanced
# This class demonstrates advanced OOP concepts such as class methods, static methods, and property decorators.
class AdvancedOOP:
    def __init__(self):
        pass  # No initialization required for this example

    class MyClass:
        class_variable = 0

        def __init__(self, value):
            self.instance_variable = value

        @classmethod
        def increment_class_variable(cls):
            cls.class_variable += 1

        @staticmethod
        def utility_method():
            print("This is a static method.")

    class Person:
        def __init__(self, first_name, last_name):
            self._first_name = first_name
            self._last_name = last_name

        @property
        def full_name(self):
            return f"{self._first_name} {self._last_name}"

        @full_name.setter
        def full_name(self, name):
            first, last = name.split()
            self._first_name = first
            self._last_name = last


# Lesson 13: Testing in Python - unittest
# This class demonstrates unit testing in Python using the unittest module.
class TestingWithUnittest:
    def __init__(self):
        pass  # No initialization required for this example

    def add(self, a, b):
        return a + b

    class TestAddition(unittest.TestCase):
        def test_add_positive_numbers(self):
            result = self.add(3, 4)
            self.assertEqual(result, 7)


# Lesson 14: Web Scraping with BeautifulSoup
# This class demonstrates building a simple web application using the Flask framework.
class FlaskWebApp:
    def __init__(self):
        # Importing Flask
        from flask import Flask

        # Creating a Flask app
        self.app = Flask(__name__)

        # Defining a route
        @self.app.route('/')
        def hello():
            return 'Hello, World!'

    def run_app(self):
        # Running the app
        if __name__ == '__main__':
            self.app.run(debug=True)


# Instances of each class to demonstrate the code
basic_python_instance = BasicPython()
functions_and_modules_instance = FunctionsAndModules()
oop_basics_instance = OOPBasics()
data_structures_instance = DataStructures()
file_handling_instance = FileHandling()
exception_handling_instance = ExceptionHandling()
virtual_environments_instance = VirtualEnvironments()
web_scraping_instance = WebScrapingWithBeautifulSoup()
advanced_functions_instance = AdvancedFunctions()
generators_instance = Generators()
context_managers_instance = ContextManagers()
advanced_oop_instance = AdvancedOOP()
testing_with_unittest_instance = TestingWithUnittest()
flask_web_app_instance = FlaskWebApp()

# Running examples
basic_python_instance.control_flow_example()
#functions_and_modules_instance.use_module()
functions_and_modules_instance.use_requests_library()
oop_basics_instance.demonstrate_oop()
data_structures_instance.demonstrate_lists()
data_structures_instance.demonstrate_dictionaries()
data_structures_instance.demonstrate_tuples()
file_handling_instance.read_from_file()
file_handling_instance.write_to_file()
exception_handling_instance.handle_exception()
virtual_environments_instance.create_virtual_environment()
virtual_environments_instance.activate_virtual_environment()
web_scraping_instance.web_scraping_example()
advanced_functions_instance.demonstrate_lambda_functions()
advanced_functions_instance.demonstrate_decorators()
generators_instance.generator_example()
context_managers_instance.context_manager_example()
advanced_oop_instance.MyClass.increment_class_variable()
advanced_oop_instance.MyClass.utility_method()
testing_with_unittest_instance.TestAddition().test_add_positive_numbers()
flask_web_app_instance.run_app()
