import setuptools

with open("bcbcpy/readme.md") as f:
    long_description = f.read()

with open("LICENSE") as f:
    license = f.read()

setuptools.setup(
    name="bcbcpy",
    use_git_versioner="short",
    setup_requires=["git-versioner"],
    description="A standalone(no-third-party) crypto & blockchain demo package on python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Heritiana Daniel, Andriasolofo (https://aheritianad.github.io)",
    author_email="aheritianad@gmail.com",
    project_urls={
        "Source": "https://github.com/aheritianad/BootCamp-BlockChain-and-Python/",
    },
    url="https://github.com/aheritianad/BootCamp-BlockChain-and-Python/",
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
)
