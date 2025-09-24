#!/usr/bin/env python3
"""
Setup script for TCGInventoryUpdater
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tcg-inventory-updater",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python application for automating TCGPlayer inventory quantity updates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/TCGInventoryUpdater",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.3.0",
    ],
    entry_points={
        "console_scripts": [
            "tcg-inventory-updater=tcg_inventory_updater:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.csv", "*.md"],
    },
)
