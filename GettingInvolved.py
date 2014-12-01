import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class GettingInvolved(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://localhost:4567/')
        self.assertIn("Ember.js", self.driver.title)

    '''
    As a tester of ember.js,
    I want to be able to link quickly to the bug reporting rules and the bug reporting system, 
    so that I can report bugs.
    '''
    def test_tester_links(self):
        driver = self.driver
        community = driver.find_element_by_xpath("//ul[@id = 'nav']/li[4]/a")
        community.click()
        link = driver.find_element_by_xpath("//div[@id = 'content']/div[2]/p[1]/a[1]")
        link.click()
        #issue tracker
        self.assertIn("https://github.com/emberjs/ember.js/issues",driver.current_url)
        driver.back()
        link = driver.find_element_by_xpath("//div[@id = 'content']/div[2]/p[1]/a[4]")
        link.click()
        #github contributing page
        self.assertIn("https://github.com/emberjs/ember.js/blob/master/CONTRIBUTING.md",driver.current_url)
        driver.back()
        link = driver.find_element_by_xpath("//div[@id = 'content']/div[2]/p[2]/a")
        link.click()
        #bug reports regarding security
        self.assertIn("http://localhost:4567/security",driver.current_url)
    '''
    As a Ember.js developer,
    I want to be able to find forums and get help with the questions I have, 
    so that I do not get stuck when working with Ember.js
    '''

    def test_forum_links(self):
        driver = self.driver
        community = driver.find_element_by_xpath("//ul[@id = 'nav']/li[4]/a")
        community.click()
        link = driver.find_element_by_xpath("//div[@id = 'content']/div[3]/p[1]/a[1]")
        link.click()
        #link to stackoverflow with ember js tag
        self.assertIn("ember.js",driver.current_url)
        self.assertIn("stackoverflow",driver.current_url)
        driver.back()
        link = driver.find_element_by_xpath("//div[@id = 'content']/div[3]/p[2]/a[1]")
        link.click()
        #link to emberjs discussion board
        self.assertIn("http://discuss.emberjs.com/",driver.current_url)

    '''
    As a contributer to Ember.js,
    I want to be able to meetup with other contributers, 
    so that I can discuss the future of Ember.js and talk to people like me.
    '''
    def test_meetup_links(self):
        driver = self.driver
        community = driver.find_element_by_xpath("//ul[@id = 'nav']/li[4]/a")
        community.click()
        #test each of the meetup links and make sure they correspond to the correct city
        for x in range(1, 20):
            meetup = driver.find_element_by_xpath("//div[@id = 'content']/div[4]/table/tbody/tr/td[1]/ul/li["+str(x)+"]/a")
            text = meetup.text
            city = text.split(" ")[0]
            meetup.click()
            self.assertIn(city,driver.page_source)
            driver.back()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
