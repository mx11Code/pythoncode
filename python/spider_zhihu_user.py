import MySQLdb
import time
from selenium import webdriver
import json

conn = MySQLdb.connect(host="localhost", user="pmx", passwd="?/>.<,123456", db="zhihu_vis")
cur = conn.cursor()


def from_zhihu_id_to_path(zhihu_id):
    return "https://www.zhihu.com/people/%s" % zhihu_id


def from_path_to_zhihu_id(path):
    return path.split("/")[-1]


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


def is_user_exists_in_db(zhihu_id):
    cur.execute("select count(*) from `users` where path='%s'" % zhihu_id)
    result = cur.fetchone()
    count = result[0]
    return False if count == 0 else True


def is_user_fetched(zhihu_id):
    cur.execute("select count(*) from `users` where fetched=1 and path='%s'" % zhihu_id)
    result = cur.fetchone()
    count = result[0]
    return False if count == 0 else True


def make_links(id_from, id_to_array):
    sql = "INSERT INTO links (`from`, `to`) VALUES (%s, %s)"
    params = [[id_from, id_to] for id_to in id_to_array]
    cur.executemany(sql, params)
    conn.commit()


def create_record_for_user(zhihu_id, image_path=None):
    if not image_path:
        img = browser.find_element_by_css_selector("div.UserAvatar img")
        image_path = img.get_attribute("src")
    sql = "INSERT INTO `users` (`path`, `image`) VALUES"
    if isinstance(zhihu_id, list):
        cur.executemany(sql + "(%s, %s)", zhihu_id)
    else:
        cur.execute((sql + "('%s', '%s')") % (zhihu_id, image_path))
    conn.commit()


def set_fetched(zhihu_id):
    sql = "update `users` set fetched=1 where path='%s'" % zhihu_id
    cur.execute(sql)
    conn.commit()


def get_following(zhihu_id, start_page=1):
    url = 'https://www.zhihu.com/people/%s/following?page=%s' % (zhihu_id, start_page)
    browser.get(url)

    zhihu_path = from_zhihu_id_to_path(zhihu_id)
    if not is_user_exists_in_db(zhihu_id):
        create_record_for_user(zhihu_id)
    elif is_user_fetched(zhihu_id):
        return
        # sql = "select * from `users` where fetched=0"
        #
        # sql = "select id from users where path = '%s'" % zhihu_path
        # cur.execute(sql)
        # result_of_id = cur.fetchone()
        # sql = "select path from users where id = '%d'" % (result_of_id[0]+1)
        # cur.execute(sql)
        # result_of_path = cur.fetchone()
        # get_following(result_of_path[0].split('/')[-1])

    data = get_current_page_followings()
    while go_next_page():
        data.extend(get_current_page_followings())

    create_record_for_user(data)
    set_fetched(zhihu_id)
    followings = [p[0] for p in data]
    make_links(zhihu_id, followings)
    # browser.close()


def fetch_next_available():
    sql = "SELECT path FROM `users` WHERE fetched=0 LIMIT 1"
    cur.execute(sql)
    record = cur.fetchone()
    zhihu_id = "wendy-wen-7" if not record else record[0]
    get_following(zhihu_id)


def to_map_dict():
    map_dict = {}
    index = 0
    sql_from = "SELECT `from` FROM `links`"
    cur.execute(sql_from)
    for from_user in cur.fetchmany(200):
        from_name = from_user[0]
        if from_name not in map_dict:
            map_dict[from_name] = index
            index += 1
            new_map_dict = map_dict.copy()
    for item in map_dict:
        sql_to = "SELECT `to` FROM `links` WHERE `from`= '%s'" % item
        cur.execute(sql_to)
        for to_user in cur.fetchmany(21):
            to_name = to_user[0]
            if to_name not in new_map_dict:
                new_map_dict[to_name] = index
                index += 1
    return new_map_dict


# print(to_map_dict())


def generate_force_layout_configuration():
    new_map_dict = to_map_dict()
    layout = {
        "type": "force",
        "categories": [{
            "name": "User",
            "keyword": {},
            "base": "HTMLElement"
        }],
        "nodes": [],
        "links": []
    }
    # i = 0
    # name_map_to_index = {}
    #
    # def add_to_map(user, i):
    #     name_map_to_index[user] = i
    #     i = i + 1
    #     return i
    #
    # sql_user = "SELECT path FROM `users`"
    # cur.execute(sql_user)
    # for user in cur.fetchmany(10):
    #     name = user[0]
    #     node = {"name": name, "value": 1, "category": 1}
    #     layout.get("nodes").append(node)
    #     i = add_to_map(name, i)
    #
    # sql_links = "SELECT `from`, `to` FROM `links`"
    # cur.execute(sql_links)
    # for link in cur.fetchall():
    #     source = name_map_to_index[link[0]]
    #     target = name_map_to_index[link[1]]
    #
    #     graph_link = {"source": source, "target": target}
    #     layout.get("links").append(graph_link)
    for name in new_map_dict.keys():
        node = {"name": name, "value": 1, "category": 1}
        layout.get("nodes").append(node)
    sql_from = "SELECT `from` FROM `links`"
    cur.execute(sql_from)
    for from_user in cur.fetchmany(200):
        from_name = from_user[0]
        sql_to = "SELECT `to` FROM `links` WHERE `from`= '%s'" % from_name
        cur.execute(sql_to)
        for to_user in cur.fetchmany(21):
            to_name = to_user[0]
            source = new_map_dict[from_name]
            target = new_map_dict[to_name]

            graph_link = {"source": source, "target": target}
            if graph_link in layout.get("links"):
                continue
            layout.get("links").append(graph_link)
    with open(r"C:\Users\Administrator\Desktop\echarts\force.json", "w+", encoding="utf8") as f:
        f.write(json.dumps(layout))
generate_force_layout_configuration()
#
# for i in range(1, 1000):
#     browser = webdriver.Chrome()
#     fetch_next_available()
#     time.sleep(10)
