import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="minds_epg",
    version="0.0.1",
    author="Heni Fazzani",
    author_email="heni.fazzani@gmail.com",
    description="Epg channel prediction with mindsDB machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fazzani/minds_epg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)