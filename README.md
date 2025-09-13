# 此项目用于个人练习，不可用于任何非法及盈利途径
1. 爬取失败可能是因为知网源代码更新，需更新源代码中的Xpath关键字：
~~~
title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,"/html/body/div[2]/div[1]/div[3]/div/div[3]/div[1]/div/h1"))).text
authors = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,"/html/body/div[2]/div[1]/div[3]/div/div[3]/div[1]/div/h3[1]"))).text
institute = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div[3]/div[1]/div/h3[2]/span/a"))).text
abstract = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "abstract-text"))).text
~~~
2. 爬取过程中会存在数据丢失的可能，尚未排查出原因，请读者自行解决。
3. 该项目使用Edge浏览器，若无法启动浏览器，则为浏览器驱动版本错误，请自行检查浏览器版本并下载相应的驱动程序，若使用其他浏览器，请读者自行更改源码，以下是常见的浏览器驱动下载网页：
> Firefox浏览器驱动：https://link.zhihu.com/?target=https%3A//github.com/mozilla/geckodriver/releases
> 
> Chrome浏览器驱动：https://registry.npmmirror.com/binary.html?path=chromedriver/
> 
> IE浏览器驱动IEDriverServer：https://link.zhihu.com/?target=http%3A//selenium-release.storage.googleapis.com/index.html
> 
> Edge浏览器驱动MicrosoftWebDriver：https://link.zhihu.com/?target=https%3A//developer.microsoft.com/en-us/microsoft-edge/tools/webdriver
