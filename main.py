from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import random

credentials = {"email1":"password1", "email2":"password2", "email3":"password3"}

comment_words = ["Great, a test", "Perfect, a test", "Awesome, a test", "Nice, a test", "This is Awesome, a test", "Beautiful"]

def main(username, password):
    try:
        chop = webdriver.ChromeOptions()
        chop.add_extension('Unlimited-Free-VPN-Hola_v1.15.258.crx')
        #chop.set_preference("extensions.Unlimited-Free-VPN-Hola_v1.15.258.currentVersion", "1.15.258")
        browser = webdriver.Chrome(chrome_options = chop)
        time.sleep(10)
        browser.get('chrome-extension:///gkojfkhlekighikafcpjkiklfbnlmeio/js/popup.html')
        time.sleep(20)
        search_field = browser.find_element_by_class_name("tt-input")
        search_field.send_keys("facebook.com")
        search_field.send_keys(Keys.RETURN)
        time.sleep(20)
        browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + "t")
        window_handles_list = browser.window_handles
        to_switch = window_handles_list[-1]
        browser.switch_to_window(to_switch)
        time.sleep(2)
        #print browser.page_source
        email_field = browser.find_element_by_id("email")
        password_field = browser.find_element_by_id("pass")
        email_field.send_keys(username)
        time.sleep(3)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(25)
        web_body = browser.find_element_by_tag_name('body')
        web_body.send_keys(Keys.ESCAPE)
        for i in range(10):
            web_body.send_keys(Keys.PAGE_DOWN)
            time.sleep(2)

        for i in range(20):
            web_body.send_keys(Keys.PAGE_UP)
            time.sleep(2)
        time.sleep(20)
        like_links = browser.find_elements_by_class_name("_khz")
        comment_links = browser.find_elements_by_xpath("//span/a[starts-with(@class,'comment_link')]")
    
        max_length = min(len(like_links), len(comment_links))

        if max_length < 20:
            iterations = max_length
        else:
            iterations = 20
        for i in range(iterations):
            rand_wait = random.randint(1, 9)
            try:
                like_links[i].click()
                print "liked"
            except:
                print "could not like"
            time.sleep(rand_wait)
        
            try:
                comment_links[i].click()
                time.sleep(2)
                print "clicked comment link"
            except:
                print "couldn't click comment"
        comment_box = browser.find_elements_by_class_name("_5rpu")
        print len(comment_box)
    
        for i in range(len(comment_box)):
            rand_comment = random.choice(comment_words)
            try:
                comment_box[i].click()
                time.sleep(2)
                comment_box[i].send_keys(rand_comment)
                comment_box[i].send_keys(Keys.RETURN)
                rand_wait = random.randint(1,7)
                time.sleep(rand_wait)
                print "commented"
            except:
                print "could not comment"
    except:
        print "failed for username", username






if __name__ == '__main__':
    for key in credentials:
        username = key
        password = credentials[key]
        main(username, password)
