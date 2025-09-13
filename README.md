# 此项目用于个人练习，不可用于任何非法及盈利途径
1. 爬取失败可能是因为知网源代码更新，需更新源代码中的Xpath关键字：
~~~
title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,"/html/body/div[2]/div[1]/div[3]/div/div[3]/div[1]/div/h1"))).text
authors = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,"/html/body/div[2]/div[1]/div[3]/div/div[3]/div[1]/div/h3[1]"))).text
institute = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div[3]/div[1]/div/h3[2]/span/a"))).text
abstract = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "abstract-text"))).text
~~~
2. 爬取过程中会存在数据丢失的可能，尚未排查出原因，请读者自行解决。
