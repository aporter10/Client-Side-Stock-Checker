<h2 align = 'center'>Client-Side-Stock-Checker</h2>

[![HitCount](http://hits.dwyl.com/sujaysathya/bunk_bot.svg?style=flat)](http://hits.dwyl.com/sujaysathya/bunk_bot)
![Python 3.8.5](https://img.shields.io/badge/Python-3.8.5-blue?style=flat&logo=python)
[![GitHub stars](https://img.shields.io/github/stars/aporter10/Client-Side-Stock-Checker?color=green)](https://github.com/aporter10/Client-Side-Stock-Checker/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/aporter10/Client-Side-Stock-Checker?color=green)](https://github.com/aporter10/Client-Side-Stock-Checker/network)
[![GitHub issues](https://img.shields.io/github/issues/aporter10/Client-Side-Stock-Checker)](https://github.com/aporter10/Client-Side-Stock-Checker/issues)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?)](https://github.com/aporter10/Client-Side-Stock-Checker/issues)


Client-Side-Stock-Checker is a Python script that will scan the page for the add to cart button then alert you via sms

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pyautogui
pip install time
pip install win32api
pip install twilio
pip install playsound
```
## Usage
Replace with proper [twillo](https://www.twilio.com/) tokens
```bash
client = Client("", "")
```
replace numbers with verified phone number
```bash
client.messages.create(to="",from_="", body="Check Walmart Cart Now")
client.messages.create(to="",from_="", body="Check Walmart Cart Now")
```
change image based on what website your useing 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
