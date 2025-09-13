# 此项目用于个人练习，不可用于任何非法及盈利途径
1. 爬取失败可能是因为知网源代码更新，需更新源代码中的Xpath关键字：
"""
title_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[{term}]/td[2]"
author_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[{term}]/td[3]"
source_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[{term}]/td[4]"
date_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[{term}]/td[5]"
database_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[{term}]/td[6]"
"""
2. 爬取过程中会存在数据丢失的可能，尚未排查出原因，请读者自行解决。
