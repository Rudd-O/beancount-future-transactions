#!/usr/bin/python3

from setuptools import setup
import os

dir = os.path.dirname(__file__)
path_to_main_file = os.path.join(
    dir, "src/beancount_extensions/future_transactions/__init__.py"
)
path_to_readme = os.path.join(dir, "README.md")
for line in open(path_to_main_file):
    if line.startswith("__version__"):
        version = line.split()[-1].strip("'").strip('"')
        break
else:
    raise ValueError(
        '"__version__" not found in "src/beancount_extensions/future_transactions/__init__.py"'
    )
readme = open(path_to_readme).read(-1)

classifiers = [
    "Development Status :: 4 - Beta",
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python :: 3 :: Only",
]

setup(
    name="beancount-future-transactions",
    version=version,
    description="A plugin for Beancount that suppresses future transactions",
    long_description=readme,
    long_description_content_type='text/markdown',
    author="Manuel Amador (Rudd-O)",
    author_email="rudd-o@rudd-o.com",
    license="GPL",
    url="http://github.com/Rudd-O/beancount-future-transactions",
    package_dir=dict(
        [
            (
                "beancount_extensions.future_transactions",
                "src/beancount_extensions/future_transactions",
            ),
        ]
    ),
    classifiers=classifiers,
    packages=["beancount_extensions.future_transactions"],
    requires=["beancount"],
    zip_safe=False,
    options={"bdist_rpm": {"requires": "python3-beancount", "no_autoreq": True}},
)
