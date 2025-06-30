from setuptools import setup, find_packages

setup(
    name="compara-prod",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "antlr4-python3-runtime==4.13.1",
    ],
)