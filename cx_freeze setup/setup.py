from cx_Freeze import setup, Executable
target = Executable(
    script="Calculator.py",
    icon="icon.ico"
    )

build_exe_options = {
    "packages": ["os", "sys"], 
    "includes": ["bs4", "from bs4 import BeautifulSoup", "import time", "import requests", "import asyncio"]
}



setup(
    name="Bazaar Calculator",
    version="0.1",
    description="A simple python program which checks and gives the user any bazaar item price and will calculate how many you can buy depending on how much money you have",
    author="mmzaini on github",
    executables=[target]
    )
