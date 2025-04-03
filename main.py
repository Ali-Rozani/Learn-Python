import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import random

# Basic Setup
st.set_page_config(page_title="Python Tutorial", layout="wide")
st.title("Advanced Python Tutorial with Streamlit")

# Add a description and tutorial navigation
st.markdown("""
    This is a basic to advanced Python tutorial using Streamlit.
    - **Basic**: Introduction to Python fundamentals.
    - **Intermediate**: Data handling and object-oriented programming.
    - **Advanced**: Advanced topics including Machine Learning, Data Visualization, etc.
""")

# Sidebar for navigation
tutorial_section = st.sidebar.radio("Choose Tutorial Section", ["Basic", "Intermediate", "Advanced"])

# Basic Python Concepts
if tutorial_section == "Basic":
    st.header("Basic Python Concepts")
    
    # Introduction to variables
    st.subheader("Variables and Data Types")
    st.write("Variables are used to store values. Python has several built-in data types like integers, floats, strings, and booleans.")
    st.code("x = 10\nname = 'Python'\nflag = True", language='python')

    # Conditional Statements
    st.subheader("If-Else Statement")
    st.write("Conditional statements allow you to execute code based on conditions.")
    st.code("""
if x > 5:
    st.write("x is greater than 5")
else:
    st.write("x is not greater than 5")
    """, language='python')

    # Loops
    st.subheader("Loops in Python")
    st.write("Python supports both `for` and `while` loops.")
    st.code("""
for i in range(5):
    st.write(f'Iteration {i}')
    """, language='python')

    # Functions
    st.subheader("Functions")
    st.write("Functions allow you to organize code into reusable blocks.")
    st.code("""
def greet(name):
    return f"Hello, {name}!"

st.write(greet('World'))
    """, language='python')

# Intermediate Python Concepts
elif tutorial_section == "Intermediate":
    st.header("Intermediate Python Concepts")
    
    # Lists, Tuples, and Dictionaries
    st.subheader("Lists, Tuples, and Dictionaries")
    st.write("These are some of the essential collection types in Python.")
    st.code("""
# List
fruits = ['apple', 'banana', 'cherry']
# Tuple (immutable)
coordinates = (10.0, 20.0)
# Dictionary
person = {'name': 'Alice', 'age': 30}
    """, language='python')

    # Classes and Object-Oriented Programming
    st.subheader("Object-Oriented Programming (OOP)")
    st.write("Python is an object-oriented language. Here's an example of a class in Python.")
    st.code("""
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return f"{self.name} says hello!"

dog = Animal("Buddy", "Dog")
st.write(dog.speak())
    """, language='python')

    # File I/O
    st.subheader("File I/O (Input/Output)")
    st.write("Reading and writing files in Python is easy with built-in functions.")
    st.code("""
with open('example.txt', 'w') as f:
    f.write('Hello, File I/O in Python!')
    
with open('example.txt', 'r') as f:
    st.write(f.read())
    """, language='python')

# Advanced Python Concepts
else:
    st.header("Advanced Python Concepts")
    
    # Lambda Functions
    st.subheader("Lambda Functions")
    st.write("Lambda functions are anonymous, single-expression functions.")
    st.code("""
multiply = lambda x, y: x * y
st.write(multiply(3, 4))
    """, language='python')

    # List Comprehensions
    st.subheader("List Comprehensions")
    st.write("List comprehensions provide a concise way to create lists.")
    st.code("""
squares = [x**2 for x in range(10)]
st.write(squares)
    """, language='python')

    # Advanced Data Visualization with Seaborn
    st.subheader("Data Visualization with Seaborn")
    st.write("Seaborn is a powerful data visualization library built on top of Matplotlib.")
    
    # Generate some random data
    data = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D'],
        'Value': [random.randint(1, 100) for _ in range(4)]
    })
    
    # Seaborn barplot
    fig, ax = plt.subplots()
    sns.barplot(x='Category', y='Value', data=data, ax=ax)
    st.pyplot(fig)
    
    # Interactive DataFrame
    st.subheader("Interactive DataFrame")
    st.write("Here's an interactive table displaying a DataFrame:")
    st.dataframe(data)
    # Asynchronous Programming
st.header("Asynchronous Programming")
st.subheader("Asyncio Library")
st.write("""
Asyncio allows you to write asynchronous code in Python. It helps to improve performance in I/O-bound tasks.
We will use the `async` and `await` keywords to write asynchronous code.
""")
st.code("""
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate a delay
    print("Data fetched!")
    
async def main():
    await fetch_data()
    
# Run the asynchronous code
asyncio.run(main())
    """, language='python')

st.subheader("Asyncio with Multiple Tasks")
st.write("""
You can use asyncio to run multiple asynchronous tasks concurrently. Here's an example of fetching data from multiple sources.
""")
st.code("""
async def fetch_data_from_source(source):
    print(f"Fetching from {source}...")
    await asyncio.sleep(random.randint(1, 3))  # Simulate delay
    print(f"Data from {source} fetched!")

async def main():
    sources = ['Source A', 'Source B', 'Source C']
    tasks = [fetch_data_from_source(source) for source in sources]
    await asyncio.gather(*tasks)

asyncio.run(main())
    """, language='python')

# Web APIs
st.header("Working with Web APIs")
st.subheader("What is an API?")
st.write("""
APIs (Application Programming Interfaces) allow different software systems to communicate with each other. Python's `requests` module is a simple way to interact with APIs.
""")

st.subheader("Fetching Data from a Public API")
st.write("""
Let's use a free public API to fetch some data. Here, we'll get random user data from the 'Random User Generator' API.
""")
st.code("""
import requests

url = 'https://randomuser.me/api/'
response = requests.get(url)
data = response.json()

st.write(data['results'][0]['name'])
st.write(f"Name: {data['results'][0]['name']['first']} {data['results'][0]['name']['last']}")
st.write(f"Location: {data['results'][0]['location']['city']}")
    """, language='python')

st.subheader("Using Python Requests Module")
st.write("""
The `requests` module is used for sending HTTP requests in Python. It supports various HTTP methods such as GET, POST, PUT, and DELETE.
""")
st.code("""
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()

# Display the first 3 posts
for post in posts[:3]:
    st.write(post)
    """, language='python')

# Web Scraping
st.header("Web Scraping with BeautifulSoup")
st.subheader("Installing BeautifulSoup and Requests")
st.write("""
Web scraping is the process of extracting data from websites. To scrape web data, you can use the `requests` and `BeautifulSoup` modules.
First, you need to install the necessary packages:
```bash
pip install requests beautifulsoup4
```
""")
