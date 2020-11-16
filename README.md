# holiday-shopping-hackathon
## Applitools Holiday Shopping Hackathon
### Prerequisites:

1. Python 3 [Install Python 3](https://realpython.com/installing-python/) 
2. Package manager pip [Install pip](https://pip.pypa.io/en/stable/installing/)
3. Python version and environment manager pyenv [Install pyenv](https://realpython.com/intro-to-pyenv/)
4. Chrome browser [Install Chrome browser](https://www.google.com/chrome/)  
5. Chrome Webdriver (added to PATH) [Download Chrome Webdriver](https://chromedriver.chromium.org/downloads)
6. Applitools account

### Run the tests:
1. Git clone this repo
`git clone git@github.com:joannalaine/holiday-shopping-hackathon.git`, or download [this as a Zip file](https://github.com/joannalaine/holiday-shopping-hackathon/archive/main.zip) and unzip it
2. `cd holiday-shopping-hackathon`
3. Set the APPLITOOLS_KEY environment variable
    - Mac: `export APPLITOOLS_KEY='YOUR_API_KEY'`
    - Windows: `set APPLITOOLS_KEY='YOUR_API_KEY'`
4. Install requirements `pip install -r requirements.txt`
5. Run tests by calling pytest using custom markers: 
    - `pytest -m part1`
    - `pytest -m part2`
    - `pytest -m part3`
    
    Support for pytest-html is also included. Exporting results to HTML can be helpful when examining failures not 
    related to Applitools. Reports can be generated using the following example commands:
    - `pytest -m part1 --html=report1.html`
    - `pytest -m part2 --html=report2.html`
    - `pytest -m part3 --html=report3.html`
