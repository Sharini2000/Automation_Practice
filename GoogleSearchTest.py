import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class GoogleSearchTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)  # Wait implicitly for elements to be ready before attempting interactions
        self.driver.maximize_window()

    def test_search_in_google(self):
        driver = self.driver
        driver.get("https://www.google.com")

        # Check the title
        self.assertIn("Google", driver.title)

        # Find the search box
        search_box = driver.find_element(By.NAME, "q")

        # Enter search term and submit
        search_box.send_keys("Facebook")
        search_box.send_keys(Keys.RETURN)

        # Verify that search results contain the search term
        results = driver.find_elements(By.CSS_SELECTOR, 'div.g')
        self.assertGreater(len(results), 0, "No search results found.")
        self.assertTrue(any("Facebook" in result.text for result in results), "Search term not found in search results.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
