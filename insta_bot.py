from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep	

class InstaBot():
	def __init__(self,username):
		self.browser = webdriver.Chrome('/bin/chromedriver')

		self.browser.get('http://www.instagram.com')
		sleep(4)

		self.username=username

		#Inputting username 
		self.browser.find_element(By.XPATH,"//input[@name=\"username\"]").send_keys(username)
		#Inputting password
		self.browser.find_element(By.XPATH,"//input[@name=\"password\"]").send_keys('your_password')
		#clicking submit button
		self.browser.find_element(By.XPATH,"//button[@type=\"submit\"]").click()
		sleep(5)

		self.browser.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click()
		sleep(5)

	def open_profile(self):
		#opening the user profile
		self.browser.find_element(By.XPATH,"//a[contains(@href,'/{}')]".format(self.username)).click()
		sleep(5)

	def get_unfollowers(self):
		#opening the user's following.
		self.browser.find_element(By.XPATH,"//a[contains(@href,'/{}/following')]".format(self.username)).click()
		sleep(2)
		following=self.names_to_list()
		sleep(3)

		#opening the user's followers.
		self.browser.find_element(By.XPATH,"//a[contains(@href,'/{}/followers')]".format(self.username)).click()
		sleep(2)
		followers=self.names_to_list()
		sleep(3)

		not_following_back_list = [user for user in following if user not in followers]

		print("These are {} people/pages that don't follow you back.".format(len(not_following_back_list)))
		print(*not_following_back_list,sep="\n")
		
	def names_to_list(self):
		sleep(4)
		scrolling_box= self.browser.find_element(By.XPATH,"/html/body/div[4]/div/div[2]")
		self.browser.execute_script('arguments[0].scrollIntoView()',scrolling_box)


		start_height,stop_height=0,1

		while stop_height != start_height:
			stop_height=start_height
			#wait if there are more users to be loaded
			sleep(2)
			start_height= self.browser.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """,scrolling_box)

		links = scrolling_box.find_elements_by_tag_name('a')
		#adding each name to list
		names = [name.text for name in links if name.text != '']
		# close button
		self.browser.find_element(By.XPATH,"/html/body/div[4]/div/div[1]/div/div[2]/button").click()
		return names


bot = InstaBot('your_username')
bot.open_profile()
bot.get_unfollowers()










