from selenium import webdriver

driver = webdriver.Firefox()

f = open('sub1_3001_3353.txt', 'r')
f_r = open('sub1_3001_3353_results.txt', 'w')

try:
    for currentLine in f:
        driver.get(currentLine)
        while(True):
            found = False
            store = driver.find_element_by_id("store")
            all_links = store.find_elements_by_tag_name("a")
            all_result_links = store.find_elements_by_class_name("result")
            for currentResultLink in all_result_links:
                currentResultLink = currentResultLink.find_element_by_tag_name("a")
                #print currentResultLink.get_attribute("href")
                f_r.write(currentResultLink.get_attribute("href") + "\n")
            for currentLink in all_links:
                if (currentLink.text == "Next >"):
                    driver.get(currentLink.get_attribute("href"))
                    found = True
                    break
            if (found == False):
                break
except:
    pass
finally:
    f.close()
    f_r.close()
    driver.quit()


    
            