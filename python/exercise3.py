import MySQLdb
import json
import time
from selenium import webdriver

conn = MySQLdb.connect(host="localhost", user="pmx", passwd="?/>.<,123456", db="zhihu_vis")
cur = conn.cursor()
browser = webdriver.Chrome()


def from_zhihu_id_to_path(zhihu_id):
    return "https://www.zhihu.com/people/%s" % (zhihu_id)


def from_path_to_zhihu_id(path):
    return path.split("/")[-1]


def is_user_exists_in_db(zhihu_id):
    cur.execute("select count(*) from `users` where path = '%s'" % (zhihu_id))
    count = cur.fetchone()[0]
    return False if count == 0 else True


def create_record_for_user(zhihu_id, image_path=None):
    if not image_path:
        img = browser.find_element_by_css_selector("div.UserAvatar img")
        img_path = img.get_attribute("src")
    sql = "INSERT INTO `users` (`path`, `image`) VALUES"
    if isinstance(zhihu_id, list):
        cur.executemany(sql + "('%s','%s')", zhihu_id)
    else:
        cur.execute(sql + "('%s','%s')" % (zhihu_id, image_path))
    conn.commit()


def is_user_fetched(zhihu_id):
    cur.execute("select count(*) from `users` WHERE fetched = 1 and path = '%s'" % zhihu_id)
    count = cur.fetchone()[0]
    return False if count == 0 else True


def get_current_page_followings():
    links = browser.find_elements_by_css_selector(".ContentItem-image .UserLink-link")
    data = []
    for link in links:
        href = link.get_attribute("href")
        zhihu_id = from_path_to_zhihu_id(href)
        image = link.find_element_by_class_name("Avatar")
        pic_url = image.get_attribute("src")
        data.append([zhihu_id, pic_url])
    return data


def go_next_page():
    try:
        button = browser.find_element_by_css_selector("button.PaginationButton-next")
        button.click()
        return True
    except:
        return False


def set_fetched(zhihu_id):
    cur.execute("update `users` set fetched = 1 WHERE path ='%s'" % zhihu_id)
    conn.commit()


def make_links(id_from, id_to_array):
    sql = "INSERT INTO `links` (`from`, `to`) VALUES"
    params = [[id_from, id_to] for id_to in id_to_array]
    cur.executemany(sql, params)
    conn.commit()


def get_following(zhihu_id, start_page=1):
    url = 'https://www.zhihu.com/people/%s/following?page=%s' % (zhihu_id, start_page)
    browser.get(url)
    zhihu_path = from_zhihu_id_to_path(zhihu_id)
    if not is_user_exists_in_db(zhihu_id):
        create_record_for_user(zhihu_id)
    elif is_user_fetched(zhihu_id):
        return
    data = get_current_page_followings()
    while go_next_page():
        data.extend(get_current_page_followings())
    create_record_for_user(data)
    set_fetched(zhihu_id)
    followings = [p[0] for p in data]
    make_links(zhihu_id, followings)


def fetch_next_available(initial_zhihu_id):
    cur.execute("SELECT path FROM `users` WHERE fetched = 0 LIMIT 1")
    record = cur.fetchone()
    zhihu_id = initial_zhihu_id if not record else record[0]
    get_following(zhihu_id)


for i in range(1, 1000):
    fetch_next_available("peng-meng-xiong")
    time.sleep(10)
