# holiday-shopping-hackathon
## Applitools Holiday Shopping Hackathon
### Prerequisites:

1. (Optional, but helpful) Python version and environment manager: pyenv [Install pyenv](https://realpython.com/intro-to-pyenv/) 
2. Python 3 [Install Python 3](https://realpython.com/installing-python/)
3. Package manager: pip [Install pip](https://pip.pypa.io/en/stable/installing/)
4. Chrome browser [Install Chrome browser](https://www.google.com/chrome/)  
5. Chrome Webdriver (added to PATH) [Download Chrome Webdriver](https://chromedriver.chromium.org/downloads)
6. Applitools account

### Run the tests:
1. Git clone this repo
`git clone git@github.com:joannalaine/holiday-shopping-hackathon.git`, or download this repo as a [Zip file](https://github.com/joannalaine/holiday-shopping-hackathon/archive/main.zip) and unzip it
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
    related to visual mismatches. Reports can be generated using the following example commands:
    - `pytest -m part1 --html=report1.html`
    - `pytest -m part2 --html=report2.html`
    - `pytest -m part3 --html=report3.html`

### Project structure:
```
holiday-shopping-hackathon
│
├── applifashion
│   ├── pages 
│   │   └── store_page.py - page element locators and interaction methods
│   ├── tests
│   │   ├── test_applifashion.py - tests picked up by pytest runner, matches test tasks with URL to test and Eyes config to use, separated by part
│   │   └── test_tasks.py - steps for each of the three checks used in parts 1-3
│   └── conftest.py - configuration file to set up pytest fixtures for Applitools Eyes and Chrome WebDriver
├── .gitignore - a list of file types to exclude from the repo
├── pytest.ini - configuration file that defines markers used to run specific tests together
├── README.md (this file) - description of project and instructions for use
└── requirements.txt - python package dependencies
```

### Approach:
For background, see Project Description below.

Since the project requires running the same tests against three different URLs, I made the test tasks resuable. The steps for the tasks are defined in `applifashion/tests/test_tasks.py`.

For the scope of this test suite, there is only one page that browser must interact with, the main page of the store which displays a product grid and various filters. I placed the element locators and UI interaction methods in `applifashion/pages/store_page.py`.

The actual test cases that are picked up by pytest are defined in `applifashion/tests/test_applifashion.py`. 
Since the project runs the same three tasks against three different versions of a page, this file serves to parametrize the test cases with the URLs and pytest markers in an effort to minimize the duplication of code.
I used fixtures to define the two different Eyes configurations (one with just Chrome for the first two parts, and one with multiple browsers for the last part). 
Unfortunately, I discovered that I was unable to use fixture names with parametrization, so part 3 is essentially duplicated and separate from parts 1 and 2.
Future improvement would explore either 1) figuring out how to refactor the Eyes configurations out of fixtures or 2) determining how to have one fixture configure Eyes dynamically based upon the test part.

To help with debugging during development, the output from the most recent run is stored in `mostrecent.log`.
Additionally, I included pytest-html reporting to optionally log the various test runs.
The test result details for visual comparisons are available in the Applitools dashboard.


### Project description:
Source: https://applitools.com/hackathon-v20-3-instructions/
#### Part 1
Imagine you are an engineer assigned to test a retail application, AppliFashion, before the busy holiday season. Your job is to automate the tests below against the [V1 production version](http://demo.applitools.com/tlcHackathonMasterV1.html) of this application. 
For each test, use Applitools Eyes as your verification tool. This project also uses Selenium WebDriver and Python with pytest.
Set Eyes to run each of the three tests on Chrome (1200 x 800) using [Applitools Ultrafast Grid](https://applitools.com/docs/topics/sdk/vg-configuration.html?Highlight=grid).

##### Tests
Include the following tests within an Applitools [batch](https://applitools.com/docs/topics/working-with-test-batches/how-to-group-tests-into-batches.html) called “Holiday Shopping”.

###### Main Page
Check the [main page](https://demo.applitools.com/tlcHackathonMasterV1.html) of the app by using Applitools Eyes to [take a screenshot of the entire page](https://applitools.com/docs/api/eyes-sdk/classes-gen/class_eyes/method-eyes-checkwindow-selenium-java.html).
Please use the following information for your visual check:
- App Name: “AppliFashion”
- Test name: “Test 1”
- Step name: “main page” 

###### Filtered Product Grid
On the left side of the main page, check "Black" under the colors filter and click the "Filter" button.
Use Applitools Eyes’ [Check Region](https://applitools.com/docs/api/eyes-sdk/classes-gen/class_eyes/method-eyes-checkregion-selenium-java.html) feature to only capture a screenshot of the shoes grid (id=product_grid) and verify that only two black shoes appear.
Please use the following information for your visual check:
- App Name: “AppliFashion”
- Test name: “Test 2”
- Step name: “filter by color” 

###### Product Details
Without filtering, click on the "Appli Air x Night" shoe.
Use Applitools to take a screenshot of the entire page to verify all of the details about the product.
Please use the following information for your visual check:
- App Name: “AppliFashion”
- Test name: “Test 3”
- Step name: “product details”

#### Part 2
Run the same tests against the [dev-branch version](http://demo.applitools.com/tlcHackathonDev.html), which contains bugs.
For bugs found, use the Applitools Dashboard to:
- Mark the tests as failed
- Add [Bug Region](https://applitools.com/docs/topics/test-manager/viewers/tm-viewer-test-editor.html#Add) annotations for bugs found. Don’t forget to save your results in the dashboard after failing the tests.
- In Test 3, find the cause of the bug by using the [Root Cause Analysis](https://applitools.com/docs/topics/test-manager/viewers/root-cause-analysis.html) (RCA) feature and provide comments in the bug region annotations explaining the exact cause of the failures, as indicated by RCA.

#### Part 3
All of the bugs have been fixed! Run your tests again in the [final production version](https://demo.applitools.com/tlcHackathonMasterV2.html) of the app but first update your configurations to set Eyes to run each of the three tests across the following configurations using Applitools Ultrafast Grid:
- Chrome (1200 x 800)
- Firefox (1200 x 800)
- Edge Chromium (1200 x 800)
- Safari (1200 x 800)
- iPhone X
Yay, your tests have passed. To see what would have happened if you used a pixel-to-pixel visual validation tool as opposed to Applitools AI-based approach, choose the passed Chrome Desktop run for Test 1 and [preview it in Exact mode](https://applitools.com/docs/topics/test-manager/viewers/tm-viewer-step-editor.html#Preview).

Notice the tests would have failed for a simple pixel shift, which is sometimes common in browser updates. Good thing you now know better than to trust a pixel-based visual testing tool!
