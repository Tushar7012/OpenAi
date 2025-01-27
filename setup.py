from setuptools import setup, find_packages

setup(
    name="MCQ-GENERATOR",  # Replace with your project's name
    version="0.0.1",
    author="Tushar Das",
    author_email="td220627@gmail.com",
    install_requires=[
        # List your project dependencies here
        "openai",
        "langchain","streamlit","python-dotenv","PyPDF2"
        # Add other dependencies as needed
    ],
    packages = find_packages()
)