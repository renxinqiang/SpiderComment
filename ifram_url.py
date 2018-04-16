#!/usr/local/bin/python3

import config,driver

url_list = config.CONFIG

for url in url_list:
    dri = driver.driver_result()
    dri.get(url)
    dri.switch_to.frame('commentsiframe')
    all_comment = dri.find_element_by_css_selector('#list_box_hot .more-comments a')
    ifram_url = all_comment.get_attribute('href')

