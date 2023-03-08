import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
        name="ezpylogger",
        version="0.1.2",
        author="Kensuke Saito",
        author_email="bebf.heavysec@gmail.com",
        description="ezpylogger: Log easier and simpler",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/bonohub13/ezpylogger.git",
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src"),
        python_requires=">=3.4")
