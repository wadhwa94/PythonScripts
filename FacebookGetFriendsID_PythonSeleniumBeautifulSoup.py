from selenium import webdriver
#wd = webdriver.Firefox()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from lxml import html
from bs4 import BeautifulSoup

usr = "wadhwajatin94@gmail.com"
pwd = "9255731200"

#driver = webdriver.Firefox()
driver = webdriver.Chrome(r"C:\Users\jatin\Downloads\chromedriver_win32\chromedriver.exe")
# or you can use Chrome(executable_path="/usr/bin/chromedriver")
driver.get("http://www.facebook.org")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)

driver.get("https://www.facebook.com/jatin.wadhwa.52/friends?source_ref=pb_friends_tl")
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
				 print (tag.attrs['data-profileid'])
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
#elem.click() as a friend



driver.close()


# wd = webdriver.Chrome(r"C:\Users\jatin\Downloads\chromedriver_win32\chromedriver.exe")
# wd.get("https://www.facebook.com/jatin.wadhwa.52/friends?source_ref=pb_friends_tl")
# f = wd.find_elements_by_xpath("//ul")
# print (f[0].get_attribute('innerHTML').encode("UTF-8"))


# elem = wd.find_element_by_css_selector('#my-id')
# element.get_attribute('innerHTML')
