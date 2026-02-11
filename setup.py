"""Setup-Konfiguration für die Package-Installation."""
from setuptools import setup, find_packages

setup(
    name="my_python_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.0.0",
        "python-dotenv>=0.19.0",
    ],
    author="Ihr Name",
    author_email="ihre.email@example.com",
    description="Ein Python-Projekt",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/username/my_python_project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
