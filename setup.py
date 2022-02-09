from setuptools import setup, find_packages

setup(
    name="shell-reader",
    version='0.1.2b1',
    author="Rishiraj0100",
    description="A module for executing and reading shell.",
    packages=find_packages(exclude=["docs", ".github", "examples", "tests"]),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: CC0-1.0 License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Issue tracker": "https://github.com/Rishiraj0100/shell-reader/issues"
    },
    python_requires=">=3.8",
    license="CC0-1.0"
)
