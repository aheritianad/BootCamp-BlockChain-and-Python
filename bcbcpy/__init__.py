from json import dumps

__annotations__ = {
    "firstname": "Heritiana Daniel",
    "lastname": "Andriasolofo",
    "email": "aheritianad@gmail.com",
    "homepage": "http://aheritianad.github.io",
    "repository": {
        "name": "bcbcpy",
        "url": "https://github.com/aheritianad/BootCamp-BlockChain-and-Python/bcbcpy",
    },
    "tutorial": {
        "notebook": "https://github.com/aheritianad/BootCamp-BlockChain-and-Python/tuto/demo.ipynb",
        "blog": "http://aheritianad.github.io/teaching/ankatso/mafi/BootCamp-BlockChain-and-Python/",
    },
}

__author__ = dumps(
    {
        "firstname": "Heritiana Daniel",
        "lastname": "Andriasolofo",
        "email": "aheritianad@gmail.com",
        "homepage": "http://aheritianad.github.io",
    }
)
del dumps
