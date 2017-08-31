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

    try:
        el_error = browser.find_element_by_css_selector("div.error")
        sql = "update `users` set fetched = 2 WHERE path = '%s'" % zhihu_id
        cur.execute(sql)
        return
    except:
        pass

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
    # browser.close()


def fetch_next_available(initial_zhihu_id):
    sql = "SELECT path FROM `users` WHERE fetched=0 LIMIT 1"
    cur.execute(sql)
    record = cur.fetchone()
    zhihu_id = initial_zhihu_id if not record else record[0]
    get_following(zhihu_id)


# def generate_force_layout_configuration():
#     map_node_to_seq = {}
#     used_links_from_a_node = {}
#     nodes_in_graphic = []
#     links_in_graphic = []
#
#     followings_of_a_user = {}
#
#     sql_counts = "SELECT `from`,count(`to`) AS following FROM `links` GROUP BY `from` ORDER BY `from`"
#     cur.execute(sql_counts)
#     for followings in cur.fetchall():
#         user = followings[0]
#         following_count = followings[1]
#         followings_of_a_user[user] = following_count
#
#     values_of_following = followings_of_a_user.values()
#     # min_following = min(values_of_following)
#     max_following = max(values_of_following)
#     for user in followings_of_a_user.keys():
#         followings_of_a_user[user] = int(40 + (followings_of_a_user[user] / max_following) * 40)
#
#     sql_links = """SELECT DISTINCT l.`from`, l.`to`, u.image FROM `links`  l
#                 INNER JOIN `users` u WHERE u.path = l.`from` ORDER BY l.`from`;"""
#     cur.execute(sql_links)
#     for link in cur.fetchall():
#         f = link[0]
#         t = link[1]
#         pic = link[2]
#
#         if f in used_links_from_a_node and used_links_from_a_node[f] >= 10:
#             continue
#
#         if f not in used_links_from_a_node:
#             used_links_from_a_node[f] = 0
#
#         if f not in map_node_to_seq:
#             nodes_in_graphic.append({
#                 "name": f,
#                 "symbol": "image://%s" % pic,
#                 "symbolSize": followings_of_a_user[f],
#                 "category": 0
#             })
#             map_node_to_seq[f] = len(nodes_in_graphic) - 1
#
#         if t not in map_node_to_seq:
#             nodes_in_graphic.append({
#                 "name": t,
#                 "symbolSize": followings_of_a_user[t] if t in followings_of_a_user else 1,
#                 "category": 0
#             })
#             map_node_to_seq[t] = len(nodes_in_graphic) - 1
#
#         links_in_graphic.append({
#             "source": map_node_to_seq[f],
#             "target": map_node_to_seq[t]
#         })
#
#         used_links_from_a_node[f] += 1
#
#     layout = {
#         "type": "force",
#         "categories": [{
#             "name": "user",
#             "keyword": {},
#             "base": "user"
#         }],
#         "nodes": nodes_in_graphic,
#         "links": links_in_graphic
#     }
#     with open(r"C:\Users\Administrator\Desktop\echarts\force.json", "w+", encoding="utf8") as f:
#         f.write(json.dumps(layout))


# generate_force_layout_configuration()
browser = webdriver.Chrome()
for i in range(1, 1000):
    fetch_next_available("peng-meng-xiong")
    time.sleep(10)
