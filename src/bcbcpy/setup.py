from setuptools import setup, find_packages

with open("readme.md") as f:
    long_description = f.read()

setup(
    name="BootCamp-BlockChain-and-Python",
    version="1.0.0dev1",
    description="A standalone crypto & blockchain demo package on python.",
    long_description=long_description,
    author="Heritiana Daniel, Andriasolofo",
    author_email="aheritianad@gmail.com",
    url="https://github.com/aheritiana/BootCamp-BlockChain-and-Python/",
    download_url="https://github.com/aheritiana/BootCamp-BlockChain-and-Python/",
    packages=["bcbcpy", "blockchain", "crypto", "exo", "functional", "block", "math"],
    package_dir={
        "bcbcpy": ".",
        "blockchain": "./blockchain",
        "crypto": "./crypto",
        "exo": "./exo",
        "functional": "./functional",
        "block": "./blockchain/block",
        "math": "./functional/math",
    },
    keywords=[
        "cryptography",
        "blockchain",
        "hash",
    ],
    license=license,
)
