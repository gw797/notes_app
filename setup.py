from setuptools import setup, find_packages

setup(
    name="notes-app",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "notes=cli.main:cli",
        ],
    },
)