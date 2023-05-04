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
    packages=find_packages(),
    # packages=["bcbcpy", "blockhain", "crypto", "exo", "functional", "block", "math"],
    # package_dir={
    #     "bcbcpy": "src/bcbcpy",
    #     "blockhain": "src/bcbcpy/blockchain",
    #     "crypto": "src/bcbcpy/crypto",
    #     "exo": "src/bcbcpy/exo",
    #     "functional": "src/bcbcpy/functional",
    #     "block": "src/bcbcpy/blockchain/block",
    #     "math": "src/bcbcpy/functional/math",
    # },
    package_data={
        "bcbcpy": ["./tuto/demo.ipynb"],
    },
    keywords=[
        "cryptography",
        "blockchain",
        "hash",
    ],
    license=license,
)
