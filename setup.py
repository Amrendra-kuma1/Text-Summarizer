import setuptools 

with open("README.md", "r", encoding="utf-8")  as f:
    long_description = f.read()


__version__ ="0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "Amrendra-kuma1"
SRC_REPO="textsummarizer"
AUTHOR_EMAIL = "amrendra001122@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Amrendra-kuma1/Text-Summarizer",
    project_urls={
        "Bug Tracker": f"https://github.com/Amrendra-kuma1/Text-Summarizer",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "transformers",
        "datasets",
        "rouge_score",
        "py7zr",
        "pandas",
        "numpy",
        "nltk",
        "tqdm",
        "PyYAML",
        "matplotlib",
        "seaborn",
        "notebook",
        "boto3",
        "mypy-boto3-s3",
        "python-box==6.0.2",
        "ensure==1.0.2",
        "fastapi==0.78.0",
        "uvicorn==0.18.3",
        "Jinja2==3.1.2",
    ],
)
