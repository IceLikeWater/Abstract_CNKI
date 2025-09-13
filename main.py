import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from openpyxl import Workbook
import tkinter

def GUI():
    # 定义一个新窗口
    root = tkinter.Tk()
    # 窗口标题
    root.title("偷偷干坏事")
    # 定义窗口大小和位置
    root.geometry("400x200+200+200")
    # 设置窗口不可缩放
    root.resizable(False, False)
    # 更改默认图标
    # root.iconbitmap("")
    # 添加文本内容并设置位置
    tkinter.Label(root, text="请输入查询内容：").grid(row=0, column=0, padx=5, pady=5)
    tkinter.Label(root, text="请设置爬取数量：").grid(row=1, column=0, padx=5, pady=5)

    # 添加输入框
    theme = tkinter.Entry(root)
    theme.grid(row=0, column=1, padx=5, pady=5)

    num = tkinter.Entry(root)
    num.grid(row=1, column=1, padx=5, pady=5)
    # 设置按钮，按下按钮开始干坏事
    tkinter.Button(root, text="RUN", command=lambda:run_code(int(num.get()),theme.get())).grid(row=0, column=2, sticky=tkinter.W)
    tkinter.Button(root, text="Exit", command=lambda:exit()).grid(row=1, column=2,sticky=tkinter.W)
    # 设置窗口循环
    root.mainloop()
def open_page(driver, theme):
    # 打开页面
    driver.get("https://kns.cnki.net/kns8/AdvSearch")
    # 传入关键字
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/dl/dd[1]/div[2]/input'))).send_keys(theme)
    # 点击搜索
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[3]/input"))).click()
    time.sleep(3)
    # 点击切换中文文献
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/div/div/div/a[1]"))).click()
    time.sleep(3)
    # 获取总文献数和页数
    res_unm = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[1]/span[1]/em"))).text
    # 去除千分位里的逗号
    res_unm = int(res_unm.replace(",", ''))
    page_unm = int(res_unm / 20) + 1
    print(f"共找到 {res_unm} 条结果, {page_unm} 页。")
    return res_unm


def crawl(driver, papers_need, theme):
    # 赋值序号, 控制爬取的文章数量
    count = 1
    worKbook = Workbook()
    sheet = worKbook.active # 激活表
    sheet.title = "Information"
    title = ['序号','文献名称','作者','学院','日期','来源','期刊','关键字','摘要','链接']
    row = ["A","B","C","D","E","F","G","H","I","J"]
    for i in range(len(title)):
        sheet[row[i]+"1"] = title[i]


    # 当爬取数量小于需求时，循环网页页码
    while count <= papers_need:
        # 等待加载完全，休眠3S
        time.sleep(3)

        title_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fz14")))
        # 循环网页一页中的条目
        for i in range(len(title_list)):
            try:
                term = count % 20  # 本页的第几个条目
                title_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[{term}]/td[2]"
                author_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[{term}]/td[3]"
                source_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[{term}]/td[4]"
                date_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[{term}]/td[5]"
                database_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/div/table/tbody/tr[{term}]/td[6]"
                title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, title_xpath))).text
                authors = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, author_xpath))).text
                source = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, source_xpath))).text
                date = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, date_xpath))).text
                database = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, database_xpath))).text

                # 点击条目
                title_list[i].click()
                # 获取driver的句柄
                n = driver.window_handles
                # driver切换至最新生产的页面
                driver.switch_to.window(n[-1])
                time.sleep(3)
                # 开始获取页面信息
                title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,"/html/body/div[2]/div[1]/div[3]/div/div[3]/div[1]/div/h1"))).text
                authors = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH ,"/html/body/div[2]/div[1]/div[3]/div/div[3]/div[1]/div/h3[1]"))).text
                institute = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div[3]/div[1]/div/h3[2]/span/a"))).text
                abstract = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "abstract-text"))).text
                try:
                    keywords = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "keywords"))).text[:-1]
                except:
                    keywords = '无'
                url = driver.current_url
                # 获取下载链接
                # link = WebDriverWait( driver, 10 ).until( EC.presence_of_all_elements_located((By.CLASS_NAME  ,"btn-dlcaj") ) )[0].get_attribute('href')
                # link = urljoin(driver.current_url, link)

                # 写入文件
                res = []
                res.append(count)
                res.append(title)
                res.append(authors)
                res.append(institute)
                res.append(date)
                res.append(source)
                res.append(database)
                res.append(keywords)
                res.append(abstract)
                res.append(url)
                print(res)
                for i in range(len(res)):
                    sheet.cell(row=count+1, column=i+1).value = res[i]
                worKbook.save(f"{theme}.xlsx")
                """
                res = f"{count}\t{title}\t{authors}\t{institute}\t{date}\t{source}\t{database}\t{keywords}\t{abstract}\t{url}".replace(
                    "\n", "") + "\n"
                with open(f'CNKI_{theme}.tsv', 'a', encoding='gbk') as f:
                    f.write(res)
                """
            except:
                print(f" 第{count} 条爬取失败\n")
                # 跳过本条，接着下一个
                continue
            finally:
                # 如果有多个窗口，关闭第二个窗口， 切换回主页
                n2 = driver.window_handles
                if len(n2) > 1:
                    driver.close()
                    driver.switch_to.window(n2[0])
                # 计数,判断需求是否足够
                count += 1
                if count-1 == papers_need:
                    exit()

        # 切换到下一页
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='PageNext']"))).click()

def run_code(num,theme):
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"

    # 设置谷歌驱动器的环境
    options = webdriver.EdgeOptions()
    # 设置chrome不加载图片，提高速度
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # # 设置不显示窗口
    # options.add_argument('--headless')
    # 创建一个谷歌驱动器
    driver = webdriver.Edge(options=options)

    res_unm = int(open_page(driver, theme))
    # 判断所需是否大于总篇数
    num = num if (num <= res_unm) else res_unm

    crawl(driver, num, theme)

    # 关闭浏览器
    driver.close()


if __name__ == "__main__":
    GUI()