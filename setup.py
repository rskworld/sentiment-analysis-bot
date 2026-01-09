"""
Sentiment Analysis Bot Setup Script
Author: RSK World (https://rskworld.in)
Founded by: Molla Samser
Designer & Tester: Rima Khatun
Contact: help@rskworld.in, +91 93305 39277
Year: 2026
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="sentiment-analysis-bot",
    version="1.0.0",
    author="RSK World",
    author_email="help@rskworld.in",
    description="Real-time sentiment analysis chatbot with emotion detection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://rskworld.in",
    project_urls={
        "Website": "https://rskworld.in",
        "Contact": "https://rskworld.in/contact.php",
        "Source": "https://rskworld.in/project",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: Educational Use Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Framework :: Flask",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.2",
            "pytest-flask>=1.2.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
        "advanced": [
            "transformers>=4.33.2",
            "torch>=2.0.1",
            "sqlalchemy>=2.0.20",
        ],
    },
    entry_points={
        "console_scripts": [
            "sentiment-bot=run:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["templates/*.html", "static/*", "*.md", "*.txt"],
    },
    keywords=[
        "sentiment analysis",
        "chatbot",
        "nlp",
        "emotion detection",
        "flask",
        "nltk",
        "spacy",
        "textblob",
        "artificial intelligence",
        "machine learning",
        "natural language processing",
    ],
    zip_safe=False,
)
