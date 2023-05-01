from setuptools import setup

with open("bcbcpy/readme.md") as f:
    long_description = f.read()

setup(
    name="BootCamp-BlockChain-and-Python",
    description="",
    long_description=long_description,
    author="Heritiana Daniel, Andriasolofo",
    author_email="aheritianad@gmail.com",
    download_url="https://github.com/aheritiana/BootCamp-BlockChain-and-Python/",
    packages=["bcbcpy"],
    package_dir={"bcbcpy": "src/bcbcpy"},
)
