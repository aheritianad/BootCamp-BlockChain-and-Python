from json import dumps as _dumps

__annotations__ = {
    "repository": {
        "name": "bcbcpy",
        "url": "https://github.com/aheritianad/BootCamp-BlockChain-and-Python/scr/bcbcpy",
    },
    "tutorial": {
        "notebook": "https://github.com/aheritianad/BootCamp-BlockChain-and-Python/tuto/demo.ipynb",
        "blog": "https://aheritianad.github.io/teaching/ankatso/mafi/BootCamp-BlockChain-and-Python/",
    },
}

__author__ = _dumps(
    {
        "firstname": "Heritiana Daniel",
        "lastname": "Andriasolofo",
        "email": "aheritianad@gmail.com",
        "homepage": "https://aheritianad.github.io",
    }
)
del _dumps
