import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iam-imaging", # Replace with your own username
    version="0.0.1",
    author="SPanigrahi",
    author_email="sp@bla.com",
    description="A general image processing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://imm.cnrs.fr",
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['iam-imaging=iam_imaging.iam_imaging_cmd:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Image Processing :: Image',
    ],
    python_requires='>=3.5',
)