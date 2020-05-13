# investmentTracker

Purpose --------------------------------------------------------------------------------------------------------------

Recently, I got into investing and purchased mutual funds to grow my savings that I earned through summer jobs. During busy periods like exam seasons, I often forget to check the markets, which means if my investments start going down, I am not aware and unable to sell in time before making a loss. The goal of Investment Tracker is to automatically open a window whenever I turn my laptop on in the morning to give me information regarding the mutual funds and stocks I am interested or invested in. Since I use my laptop every day, there is no way I will be unaware of the market’s situation if the information is automatically opened and presented to me. 

Tools  --------------------------------------------------------------------------------------------------------------

•	Python for scripting

•	Selenium for web scraping and automating Google Chrome

•	Time library for giving webpages time to load and time to stay open for user to read

•	Windows Task Scheduler to run script every time laptop is started

How it Works ----------------------------------------------------------------------------------------------------------------

Windows Task Scheduler is first passed the task to run the investmentTracker.py file on startup or login. When the script is run, Selenium Webdriver is used to automatically open a chrome tab and navigate to The Globe and Mail’s watchlist page. The login button is then clicked, and login credentials entered by the script. Once that is complete, the website will load the watchlist giving the user information about their stocks/funds. 

Setup -----------------------------------------------------------------------------------------------------------------

Before running the program for the first time, the following must be done:

•	Create an account with The Globe and Mail and setup a watchlist: https://www.theglobeandmail.com/investing/markets/watchlist/

•	Create a task in Windows Task Scheduler to run the file on startup or login

1) Open task scheduler
2) Click create basic task
3) Give the task a name and short description, then click next
4) Select When the computer starts or When I log on based on your preferences
5) Click next
6) Enter the file path (location where investmentTracker.py is stored on the computer)
7) Click finish

•	Install Python version 3.8.2 or later 

•	Install Selenium: Enter 'pip install selenium' in the command prompt

•	Install Chrome Driver: https://sites.google.com/a/chromium.org/chromedriver/downloads

•	Open the code in an IDE and enter your username and password into the corresponding lines (replace ####)

Username: username.send_keys(“####”) 

Password: password.send_keys(“####”)
    
*Note: This program was written to run on Windows 10
