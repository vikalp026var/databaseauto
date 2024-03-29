from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "5.0.2"
REPO_NAME = "databaseauto"
PKG_NAME = "databaseauto"
AUTHOR_USER_NAME = "Vikalp"
AUTHOR_EMAIL = "Vikalp026varshney@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with a database.",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Corrected parameter name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
