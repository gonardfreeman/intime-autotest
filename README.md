# Page-Object-Pattern-BLP
Python WebDriver POP BLP
This is free BLP of Page Object Pattern in python 3.5 && Selenium 3
You can use it whatever you what.
## Usage
In base.py change base_url parametr to whatever you need link
To run Chrome driver you need to download it from https://sites.google.com/a/chromium.org/chromedriver/downloads (choose lastest for correct work)
Selenium URL: http://www.seleniumhq.org/docs/
###base.py
In this file I'm define most common actions with page such as find_element, open url and other(get url and get title u can delete, it's just for my projects, for assertion).
You can write your actions, such as click, hover, timeout and other.
###locators.py
In this file we need define how our actions can find elements on page.
You can read more about By on internet (exmpl: http://selenium-python.readthedocs.io/locating-elements.html)
###pages.py
On this page you need To define most common checks of page. Each class -> each page.
###testPage.py
You may also want to use unittests for assertion, soon I'll add BLP for that.



#### Contacts && License
email: 007arenko@gmail.com
License: MIT
