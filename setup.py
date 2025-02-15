from setuptools import setup, find_packages

setup(
    name="pyasmd",
    version="0.1.0",
    author="Vishnu Vardhan Reddy",
    author_email="gvvr2001@example.com",
    description="A simple arithmetic operations library supporting dynamic inputs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ThippaluruNithinReddy/pyasmd",
    packages=find_packages(),  # Detects 'asmd' automatically
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
