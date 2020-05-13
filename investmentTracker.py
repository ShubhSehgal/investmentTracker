import time
from selenium import webdriver

#function for opening the Watchlist on Google Chrome
def getWatchlistInfo():
    driver = webdriver.Chrome() 
    driver.get('https://www.theglobeandmail.com/investing/markets/watchlist/') #open the Globe and Mail website
    time.sleep(2) #give the website 2 seconds to load

    #somtimes there is a login popup, in this case, click the login button in the popup
    try:
        driver.find_element_by_id("js-login").click()
        time.sleep(5)

    #if there is no popup, click the login button at the top-right of the page
    except:
        driver.find_element_by_id("c-site-header-login-button").click() #click login button
        time.sleep(2)

    #enter username
    username = driver.find_element_by_id("inputEmail") #find username element
    username.clear() #clear any text currently there
    username.send_keys("####") # --- INSERT USERNAME HERE ---#

    #enter password
    password = driver.find_element_by_id("inputPassword") #find password element
    password.clear() #clear any text currently there 
    password.send_keys("####") # --- INSET PASSWORD HERE --- #

    time.sleep(2)

    #click login button
    driver.find_element_by_id("loginButton").click()

    #the tab will be open for an hour 
    time.sleep(3600)

    driver.quit()

def main():
    getWatchlistInfo()

main()