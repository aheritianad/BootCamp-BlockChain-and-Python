import setuptools

with open("src/bcbcpy/readme.md") as f:
    long_description = f.read()

with open("LICENSE") as f:
    license = f.read()

setuptools.setup(
    name="bcbcpy",
    version="1.0.0dev1",
    description="A standalone(no-third-party) crypto & blockchain demo package on python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Heritiana Daniel, Andriasolofo",
    author_email="aheritianad@gmail.com",
    project_urls={
        "Source": "https://github.com/aheritiana/BootCamp-BlockChain-and-Python/",
    },
    url="https://github.com/aheritiana/BootCamp-BlockChain-and-Python/",
    packages=setuptools.find_packages(
        include=(
            "bcbcpy",
            "bcbcpy.*",
        )
    ),
    package_dir={"bcbcpy": "bcbcpy"},
    keywords=[
        "cryptography",
        "blockchain",
        "hash",
    ],
    license=license,
    python_requires=">=3.9",
    include_dirs=["tuto"],
    package_data={"tuto": ["tuto.ipynb"]},
)
