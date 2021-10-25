"""setup file."""
import re

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("src/luserta/__init__.py", "r", encoding="utf-8") as fh:
    version = re.search(r"__version__ = \"(.*)\"", fh.read()).group(1)

setuptools.setup(
    name="luserta",
    version=version,
    author="",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="",
    url="https://github.com/gallotia-galloti/luserta",
    project_urls={
        "Bug Tracker": "https://github.com/gallotia-galloti/luserta/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.10",
)
