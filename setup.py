from setuptools import setup, find_packages

setup(
    name="replaceapplemusic",
    version="0.0.1",
    py_modules=["main", "bridge", "file_reader"],
    packages=find_packages(),
    install_requires=[
        "appscript",
        "mutagen",
    ],
    entry_points={
        "console_scripts": [
            "ramusic=main:main",
            "replaceapplemusic=main:main",
        ],
    },
    author="realtvop",
    description="A Python utility to replace source files of songs in Apple Music while preserving metadata",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/realtvop/ReplaceAppleMusic",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
) 