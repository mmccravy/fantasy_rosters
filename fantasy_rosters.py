import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import csv#to do

def getPercentage(word):
	if word == '--':
		return '--'
	first = word.split('/')[0]
	last = word.split('/')[1]
	return round(float(first)/float(last),3)

def getStats(location):

	playerName = driver.find_element_by_xpath(introStr + location + "]/td[2]").text.split(",")[0]
	minutes = driver.find_element_by_xpath(introStr + location + "]/td[4]").text
	fg = driver.find_element_by_xpath(introStr + location + "]/td[5]").text
	ft = driver.find_element_by_xpath(introStr + location + "]/td[7]").text
	threes = driver.find_element_by_xpath(introStr + location + "]/td[9]").text
	oboards = driver.find_element_by_xpath(introStr + location + "]/td[10]").text
	dboards = driver.find_element_by_xpath(introStr + location + "]/td[11]").text
	assists = driver.find_element_by_xpath(introStr + location + "]/td[12]").text
	steals = driver.find_element_by_xpath(introStr + location + "]/td[13]").text
	blocks = driver.find_element_by_xpath(introStr + location + "]/td[14]").text
	points = driver.find_element_by_xpath(introStr + location + "]/td[15]").text
	print playerName, minutes, getPercentage(fg), getPercentage(ft), threes, oboards, dboards, assists, steals, blocks, points


chrome_path = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

introStr = "//*[@id="
locationStr = "'playertable_0']/tbody/tr["

driver.get("http://games.espn.com/fba/clubhouse?leagueId=190685&teamId=1&seasonId=2017")
WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"(//iframe)")))

driver.switch_to.frame("disneyid-iframe")
time.sleep(2)
driver.find_element_by_css_selector("div.field-username-email input").send_keys("matthewmccravy")
driver.find_element_by_css_selector("div.field-password input").send_keys("matthew111")
driver.find_element_by_xpath("//button[contains(., 'Log In')]").click()

time.sleep(10)

for i in range(0,13):#myteam
	location = str("'pncPlayerRow_" + str(i) + "'")
	getStats(location)

for a in range(2,11):
	driver.get("http://games.espn.com/fba/clubhouse?leagueId=190685&teamId=" + str(a) + "&seasonId=2017")

	for i in range(3,18):#other
		if i == 13 or i == 14:
			continue
		var = str("'playertable_0']/tbody/tr[" + str(i))
		getStats(var)

time.sleep(5)

driver.quit();