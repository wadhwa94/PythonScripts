from selenium import webdriver
#wd = webdriver.Firefox()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from bs4 import BeautifulSoup
import time

usr = "XXXXXXXXXX"
pwd = "XXXXXXXXXX"

#driver = webdriver.Firefox()
#driver = webdriver.Ie(r"C:\Users\jatin\Desktop\IEDriverServer.exe")

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
#driver = webdriver.Chrome(chrome_options=chrome_options)


driver = webdriver.Chrome(r"C:\Users\jatin\Downloads\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
# or you can use Chrome(executable_path="/usr/bin/chromedriver")
driver.get("http://www.facebook.org")
assert "Facebook" in driver.title
#time.sleep(5)
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

driver.get("https://www.facebook.com/jatin.wadhwa.52/friends?source_ref=pb_friends_tl")
time.sleep(2)

#element_new = driver.find_element_by_tag_name('html')
#element_new.send_keys(Keys.ESCAPE)
#element_new.send_keys(Keys.END)
for i in range(22):
	#print (i)
	start = 0 + i*1000
	end = (i+1)*1000
	driver.execute_script("window.scrollTo("+ str(start) + "," + str(end) +");")
	time.sleep(2)	 
# driver.execute_script("window.scrollTo(0, 1000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(1000, 2000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(2000, 3000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(3000, 4000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, 1000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(1000, 2000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(2000, 3000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(3000, 4000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, 1000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(1000, 2000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(2000, 3000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(3000, 4000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(0, 1000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(1000, 2000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(2000, 3000);")
# time.sleep(2)
# driver.execute_script("window.scrollTo(3000, 4000);")
# time.sleep(2)
friends = []
print ("Mam")
f = driver.find_elements_by_xpath("//ul")
print (len(f))
for i in f:
	if (i.get_attribute('innerHTML').find('as a friend') != -1):
		k = i.get_attribute('innerHTML').encode("UTF-8")
		tree = html.fromstring(k)
		#print (" curren ttype i s =")
		#print (type(k))
		#print (k)
		soup = BeautifulSoup(k,"lxml")
		mydivs = soup.findAll("button", { "class" : "_42ft _4jy0 FriendRequestOutgoing enableFriendListFlyout outgoingButton enableFriendListFlyout hidden_elem _4jy3 _517h _51sy" })
		# buyers = tree.xpath('//button/text()')
		for i_1 in mydivs:
			i_1 = i_1.encode("utf-8")
			#print (" curren ttype i s =")
			#print (i_1)
			#print (type(i_1))
			soup1 = BeautifulSoup(i_1,"lxml")
			for tag in soup1.findAll('button'):
				 friends.append(tag.attrs['data-profileid'])
			#soup1.findAll(lambda tag:[inputTag.append(a[1]) for a in tag.attrs if a[0].startswith('data-profileid')])
			# inputTag = soup1.find(attrs={"name" : "class"})
			# print (inputTag)
			# output = inputTag['value']
			# print (output)
		#print (mydivs)
		# print (i.get_attribute('innerHTML').encode("UTF-8"))
		#print ("\n\n\n")
#elem = driver.find_element_by_css_selector(".input.textInput")
#elem.send_keys("Posted using Python's Selenium WebDriver bindings!")
#elem = driver.find_element_by_css_selector("input[value=\"Publicar\"]")
#elem.click() as a friend - Rohit - Id - 100001265210378
import fbchat
from getpass import getpass

print (len(friends))

#no_of_friends = int(raw_input("Number of friends: "))
for i in friends:
    # name = str(input("Name: "))
    # friends = client.getUsers(name)  # return a list of names
    # friend = friends[0]
    # print (friend)
    #name = input("just a stopper - do you want to continue");
    msg = "Hi\nPlease, Suggest One movie and One Book (just 1 each) that you can suggest anyone, to watch and read respectively.\nIrrespective of Genre and Language.\nPlease Reply!\n-- Sent by Python Script. [Advertising Happyness] \n"
    sent = client.send(i, msg)
    if sent:
        print(str(i) + "Message sent successfully!")


#driver.close()


# wd = webdriver.Chrome(r"C:\Users\jatin\Downloads\chromedriver_win32\chromedriver.exe")
# wd.get("https://www.facebook.com/jatin.wadhwa.52/friends?source_ref=pb_friends_tl")
# f = wd.find_elements_by_xpath("//ul")
# print (f[0].get_attribute('innerHTML').encode("UTF-8"))


# elem = wd.find_element_by_css_selector('#my-id')
# element.get_attribute('innerHTML')
