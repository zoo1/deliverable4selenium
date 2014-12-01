import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GettingStarted(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:4567/')
        self.assertIn("Ember.js", self.driver.title)

    '''
    As a new Ember.js developer,
    I want to be able to link quickly to the ember.js github webpage, 
    so that I can quickly get started with Ember.js
    '''
    def test_github_link(self):
        driver = self.driver
        community = driver.find_element_by_xpath("//ul[@id = 'nav']/li[4]/a")
        community.click()
        link = driver.find_element_by_xpath("//div[@id = 'content']/div[1]/p/a")
        link.click()
        self.assertIn("https://github.com/emberjs/ember.js",driver.current_url)
        driver.back()
        elem = driver.find_element_by_xpath("//div[@id = 'github']/a")
        elem.click()
        self.assertEqual("https://github.com/emberjs/ember.js",driver.current_url)
    '''
    As a new Ember.js developer,
    I want to be able to download Ember.js, 
    so that I can quickly get started with Ember.js
    NOTE: This test does not ensure that downloads will work correctly and instead is a good starting point but downloading files should not be done by selenium
    '''
    def test_downloads_existing(self):
        driver = self.driver
        orangebutton = driver.find_element_by_xpath("//div[@id = 'download']/div/a")
        self.assertIn("starter-kit",orangebutton.get_attribute("href"))
        production = driver.find_element_by_xpath("//div[@id = 'download']/div/div/a[1]")
        minimum = driver.find_element_by_xpath("//div[@id = 'download']/div/div/a[2]")
        debug = driver.find_element_by_xpath("//div[@id = 'download']/div/div/a[3]")
        self.assertIn("ember.prod.js",production.get_attribute("href"))
        self.assertIn("ember.min.js",minimum.get_attribute("href"))
        self.assertIn("ember.js",debug.get_attribute("href"))

    '''
    As a new website visitor,
    I want to be able to play with the ember.js previewexamples, 
    so that I can be impressed with ember.js.
    '''
    def test_preview_examples(self):
        #entering name test
        driver = self.driver
        namehere = driver.find_element_by_id("ember793")
        namehere.send_keys("laboon")
        texthere = driver.find_element_by_xpath("//div[@id = 'ember620']/div[2]")
        self.assertIn("LABOON",texthere.text)   
        #testing if changing tabs in code viewer works correctly
        driver.find_element_by_xpath("//div[@id = 'ember635']/div[1]/a[1]").click()
        text1 = driver.find_element_by_xpath("//div[@id = 'ember635']/div[2]").text
        driver.find_element_by_xpath("//div[@id = 'ember635']/div[1]/a[2]").click()
        self.assertNotEqual(text1,driver.find_element_by_xpath("//div[@id = 'ember635']/div[2]").text)
        driver.find_element_by_xpath("//div[@id = 'ember635']/div[1]/a[1]").click()
        self.assertEqual(text1,driver.find_element_by_xpath("//div[@id = 'ember635']/div[2]").text)
        #third code viewer
        driver.find_element_by_xpath("//div[@id = 'ember704']/div[1]/a[1]").click()
        text1 = driver.find_element_by_xpath("//div[@id = 'ember704']/div[2]").text
        driver.find_element_by_xpath("//div[@id = 'ember704']/div[1]/a[2]").click()
        self.assertNotEqual(text1,driver.find_element_by_xpath("//div[@id = 'ember704']/div[2]").text)
        driver.find_element_by_xpath("//div[@id = 'ember704']/div[1]/a[1]").click()
        self.assertEqual(text1,driver.find_element_by_xpath("//div[@id = 'ember704']/div[2]").text)
        #mailbox test inbox and spam folders
        driver.find_element_by_id("ember904").click()
        url = driver.find_element_by_xpath("//div[@id = 'ember738']/div")
        self.assertIn("INBOX",url.text)
        driver.find_element_by_xpath("//div[@id = 'ember738']/section/table/tbody/tr[2]").click()
        self.assertIn("Welcome to Ember", driver.find_element_by_xpath("//div[@id = 'ember738']/section/div").text)
        driver.find_element_by_id("ember923").click()
        url = driver.find_element_by_xpath("//div[@id = 'ember738']/div")
        self.assertIn("SPAM",url.text)
        driver.find_element_by_xpath("//div[@id = 'ember738']/section/table/tbody/tr[2]").click()
        self.assertIn("YOU HAVE ONE THE LOTTERY!!!", driver.find_element_by_xpath("//div[@id = 'ember738']/section/div").text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
