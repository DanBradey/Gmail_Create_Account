from selenium import webdriver
import time

#create a new Chrom session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

#navigate to the application home page
driver.get("https://accounts.google.com/SignUp")

#get the first name textbox
first_name = driver.find_element_by_id("FirstName")
first_name.clear()

#enter first name
first_name.send_keys("First Name")

#get the surname textbox
surname = driver.find_element_by_id("LastName")
surname.clear()

#enter surname
surname.send_keys("Surname")


#get username textbox
username = driver.find_element_by_id("GmailAddress")
username.clear()

#enter username
username.send_keys("ENTER USERNAME")

#get password textbox
password = driver.find_element_by_id("Passwd")
password.clear()

#enter password
password.send_keys("ENTER PASSWORD")

#get confirm password textbox
confirm_password = driver.find_element_by_id("RE ENTER PASSWORD")
confirm_password.clear()

#re enter password
confirm_password.send_keys("RE ENTER PASSWORD")

#select month from birthday dropdown
month = driver.find_element_by_id(":0").click()
january = driver.find_element_by_id(":1").click()

#get birth day textbox
birth_day = driver.find_element_by_id("BirthDay")
birth_day.clear()

#enter birth day
birth_day.send_keys("01")

#get birth year textbox
birth_year = driver.find_element_by_id("BirthYear")
birth_year.clear()

#enter birth year
birth_year.send_keys("1990")

#select gender from gender dropdonw
gender = driver.find_element_by_id("Gender").click()
female = driver.find_element_by_id(":e").click()

#submit form
submit = driver.find_element_by_id("submitbutton").submit()
time.sleep(2)
submit_again = driver.find_element_by_id("submitbutton").submit()

#contract agreement
scroll_button = driver.find_element_by_id("tos-scroll-button").click()
time.sleep(2)
contract_agreement = driver.find_element_by_id("iagreebutton").click()
time.sleep(2)

#verify account
phone_number = driver.find_element_by_id("signupidvinput")
phone_number.clear()
phone_number.send_keys("0400384496")

verify_submit = driver.find_element_by_id("next-button").click()










