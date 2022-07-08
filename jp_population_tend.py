

# title	_6code
# 千代田区	131016
# 中央区	131024
# 港区	131032
# 新宿区	131041
# 文京区	131059
# 台東区	131067
# 墨田区	131075
# 江東区	131083
# 品川区	131091
# 目黒区	131105
# 大田区	131113
# 世田谷区	131121
# 渋谷区	131130
# 中野区	131148
# 杉並区	131156
# 豊島区	131164
# 北区	131172
# 荒川区	131181
# 板橋区	131199
# 練馬区	131202
# 足立区	131211
# 葛飾区	131229
# 江戸川区	131237
import re


import requests
import pymysql



def to_fetch_area_data_buy(url,area_list):
    resp = requests.get(url)

    area_data_list = [re.findall(re.compile('{0}<span class="searchitem-list-value">(.*?)</span>'.format(x),re.S),resp.text) for x in area_list]
    num_data_list = [re.findall(re.compile('\d+',re.S),x[0])[0] for x in area_data_list]


    # content--->list
    ff_l = []
    f_tup = tuple(num_data_list)
    ff_l.append((f_tup))

    return ff_l


def to_fetch_area_data_rent(url,area_list):
    resp = requests.get(url)

    area_data_list = [re.findall(re.compile('<span>{0}</span><span class="searchitem-list-value">(.*?)</span></label></li>'.format(x),re.S),resp.text) for x in area_list]
    num_data_list = [re.findall(re.compile('\d+',re.S),x[0])[0] for x in area_data_list]
    # content--->list
    ff_l = []
    f_tup = tuple(num_data_list)
    ff_l.append((f_tup))

    return ff_l


def insertDB(content,tablename):


    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JP_RealEstate',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        f_6 = "%s," *23
        cursor.executemany('insert into {1} (_131016,_131024,_131032,_131041,_131059,_131067,_131075,_131083,_131091,_131105,_131113,_131121,_131130,_131148,_131156,_131164,_131172,_131181,_131199,_131202,_131211,_131229,_131237) values ({0})'.format(f_6[:-1],tablename), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass




if __name__ == "__main__":
    tokyo_area_list = ["千代田区", "中央区", "港区", "新宿区", "文京区", "台東区", "墨田区", "江東区", "品川区", "目黒区", "大田区", "世田谷区", "渋谷区",
                       "中野区", "杉並区", "豊島区", "北区", "荒川区", "板橋区", "練馬区", "足立区", "葛飾区", "江戸川区"]

    tokyo_area_buy_url = "https://suumo.jp/ms/chuko/tokyo/city/"
    tokyo_area_rent_url = "https://suumo.jp/chintai/tokyo/city/"
    # rent market
    rent_area_data_list = to_fetch_area_data_rent(tokyo_area_rent_url, tokyo_area_list)
    insertDB(rent_area_data_list,"tokyo_old_rent_market")


    # buy market
    buy_area_data_list = to_fetch_area_data_buy(tokyo_area_buy_url, tokyo_area_list)
    insertDB(buy_area_data_list,"tokyo_old_buy_market")


# create table tokyo_old_rent_market (id int not null primary key auto_increment,
# _131016 text,_131024 text,_131032 text,_131041 text,_131059 text,_131067 text,_131075 text,_131083 text,_131091 text,_131105 text,_131113 text,_131121 text,_131130 text,_131148 text,_131156 text,_131164 text,_131172 text,_131181 text,_131199 text,_131202 text,_131211 text,_131229 text,_131237 text,
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;
#
#
# create table tokyo_old_buy_market (id int not null primary key auto_increment,
# _131016 text,_131024 text,_131032 text,_131041 text,_131059 text,_131067 text,_131075 text,_131083 text,_131091 text,_131105 text,_131113 text,_131121 text,_131130 text,_131148 text,_131156 text,_131164 text,_131172 text,_131181 text,_131199 text,_131202 text,_131211 text,_131229 text,_131237 text,
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;
