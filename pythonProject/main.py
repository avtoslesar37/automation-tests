from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe")

driver.get("https://by.wildberries.ru/catalog/muzhchinam/odezhda")
# time.sleep(2)
el1 = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div[3]/div[2]/div[1]/div[3]/div/div[1]/div/a/div[1]/img")


el1.click()
time.sleep(2)
el2 = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[2]/div/div[5]/ul/li[3]/label/span[1]")
el2.click()
time.sleep(1)
el3 = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[2]/div/div[5]/div[5]/div[1]/button[1]")
el3.click()
time.sleep(1)
el4 = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[2]/div/div[5]/div[5]/div[1]/a")
el4.click()
#name
time.sleep(1)
inp1 = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[1]/form/div[1]/div[3]/div[2]/div[2]/div[1]/div[1]/input")
inp1.send_keys("Сергей")
time.sleep(1)
#last name
inp2 = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[1]/form/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input")
inp2.send_keys("Ковалев")
time.sleep(1)
#phone
inp3 = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[1]/form/div[1]/div[3]/div[2]/div[2]/div[4]/div[1]/input[2]")
inp3.send_keys("298675523")
time.sleep(1)
#get code
el5 = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[1]/form/div[1]/div[3]/div[2]/div[2]/div[4]/div[1]/button")
el5.click()
time.sleep(15)
#enter code
el6 = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[1]/form/div[1]/div[2]/div[2]")
el6.click()
time.sleep(1)
el7 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]/button[2]")
el7.click()
time.sleep(1)
el8 = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div")
el8.click()
time.sleep(1)
el9 = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[1]/ymaps/ymaps/ymaps/ymaps[6]/ymaps/ymaps/ymaps/ymaps[1]/ymaps[2]/ymaps/ymaps/div/div[2]/button")
el9.click()
time.sleep(1)
el10 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div[1]/div/div[2]/button[1]")
el10.click()
time.sleep(1)
#attach card
el11 = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div/div/div[1]/form/div[1]/div[3]/div[1]/div[2]")
el11.click()
time.sleep(1)
el12 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/ul/li/label")
el12.click()
time.sleep(2)
#card number
el13 = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/form/div[2]/div[1]/div[2]/div/div[1]/input")
el13.send_keys("5470111111113461")
time.sleep(0.5)
el14 = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/form/div[2]/div[1]/div[3]/div[1]/div[1]/input")
el14.send_keys("1121")
time.sleep(0.5)
el15 = driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/form/div[2]/div[1]/div[2]/div/div[1]/input")
el15.send_keys("928")

