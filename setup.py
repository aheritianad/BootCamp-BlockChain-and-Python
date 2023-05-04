from setuptools import setup, find_packages

with open("src/bcbcpy/readme.md") as f:
    long_description = f.read()
with open("LICENSE") as f:
    license = f.read()

setup(
    name="BootCamp-BlockChain-and-Python",
    version="1.0.0dev1",
    description="A standalone crypto & blockchain demo package on python.",
    long_description=long_description,
    author="Heritiana Daniel, Andriasolofo",
    author_email="aheritianad@gmail.com",
    url="https://github.com/aheritiana/BootCamp-BlockChain-and-Python/",
    download_url="https://github.com/aheritiana/BootCamp-BlockChain-and-Python/",
    packages=["bcbcpy"],
    package_dir={
        "bcbcpy": "src/bcbcpy",
    },
    keywords=[
        "cryptography",
        "blockchain",
        "hash",
    ],
    license=license,
)
