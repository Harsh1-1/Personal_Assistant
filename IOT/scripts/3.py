from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

binary = '/root/images_to_spoof/firefox/firefox'
browser = webdriver.Firefox(firefox_binary=binary)
browser.get('https://usebackpack.com')

element = browser.find_element_by_css_selector('#loginButton')

element.click()

email = browser.find_element_by_id('user_email')
email.send_keys('mohd16034@iiitd.ac.in')
password = browser.find_element_by_id('user_password')
password.send_keys('l3g3nd@ry')

submit_button = browser.find_element_by_name('commit')
submit_button.click()

main_page_source = browser.page_source
soup = BeautifulSoup(main_page_source, 'html.parser')

deadlines_list = soup.find_all('div',id='deadlines-list')

deadline_data = deadlines_list[0].get_text()
# deadline_data = deadline_data.replace("\n",'')
deadline_data = deadline_data.replace("            ",'')

print deadline_data

browser.close()

# first = browser.find_element_by_class_name("deadline-item")
# # first.click()
# print first.get_attribute("href")

# for link in deadlines_list.find_all('a'):
#     print(link.get('href'))


#
# browser.execute_script('''window.open("https://facebook.com","_blank");''') #for switching to new tab and open another website
#
#
# fbemail = browser.find_element_by_id('email')
# fbemail.send_keys('')
# fbpassword = browser.find_element_by_id('pass')
# fbpassword.send_keys("")
# submit = browser.find_element_by_id('u_0_5')
# submit.click()
