

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
import time

import requests
import pymysql
from lxml import etree




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

        f_6 = "%s," *4
        cursor.executemany('insert into {1} (_line,_station,_area,_10minutes_URL) values ({0})'.format(f_6[:-1],tablename), content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass




if __name__ == "__main__":
    line_list_name = ["ＪＲ山手線","ＪＲ京浜東北線","ＪＲ東海道本線","ＪＲ常磐線","ＪＲ南武線","ＪＲ横浜線","ＪＲ横須賀線","ＪＲ中央線","ＪＲ青梅線","ＪＲ五日市線","ＪＲ武蔵野線","ＪＲ八高線","ＪＲ埼京線","ＪＲ高崎線","ＪＲ宇都宮線","ＪＲ総武線","ＪＲ総武線快速","ＪＲ京葉線","湘南新宿ライン宇須","湘南新宿ライン高海","東海道新幹線","上越新幹線","北陸新幹線","東北新幹線","東京メトロ銀座線","東京メトロ丸ノ内線","東京メトロ日比谷線","東京メトロ東西線","東京メトロ千代田線","東京メトロ有楽町線","東京メトロ半蔵門線","東京メトロ南北線","東京メトロ副都心線","西武有楽町線","西武新宿線","西武池袋線","西武拝島線","西武山口線","西武国分寺線","西武多摩川線","西武多摩湖線","西武西武園線","西武豊島線","東武東上線","東武伊勢崎線","東武亀戸線","東武大師線","東急東横線","東急田園都市線","東急池上線","東急目黒線","東急多摩川線","東急大井町線","東急世田谷線","都営浅草線","都営三田線","都営新宿線","都営大江戸線","都電荒川線","日暮里・舎人ライナー","京王井の頭線","京王競馬場線","京王新線","京王線","京王動物園線","京王相模原線","京王高尾線","京成押上線","京成金町線","京成本線","京急本線","京急空港線","小田急線","小田急多摩線","多摩都市モノレール","りんかい線","北総線","東京モノレール","新交通ゆりかもめ","埼玉高速鉄道","つくばエクスプレス","成田スカイアクセス"]

    lines_list_url = ["https://suumo.jp/chintai/tokyo/en_yamanotesen/","https://suumo.jp/chintai/tokyo/en_keihintohokusen/","https://suumo.jp/chintai/tokyo/en_tokaidohonsen/","https://suumo.jp/chintai/tokyo/en_jobansen/","https://suumo.jp/chintai/tokyo/en_nambusen/","https://suumo.jp/chintai/tokyo/en_yokohamasen/","https://suumo.jp/chintai/tokyo/en_yokosukasen/","https://suumo.jp/chintai/tokyo/en_chuosen/","https://suumo.jp/chintai/tokyo/en_omesen/","https://suumo.jp/chintai/tokyo/en_itsukaichisen/","https://suumo.jp/chintai/tokyo/en_musashinosen/","https://suumo.jp/chintai/tokyo/en_hachikosen/","https://suumo.jp/chintai/tokyo/en_saikyosen/","https://suumo.jp/chintai/tokyo/en_takasakisen/","https://suumo.jp/chintai/tokyo/en_utsunomiyasen/","https://suumo.jp/chintai/tokyo/en_sobusen/","https://suumo.jp/chintai/tokyo/en_sobukaisokusen/","https://suumo.jp/chintai/tokyo/en_keiyosen/","https://suumo.jp/chintai/tokyo/en_shonanshinjukulineutsunomiyayokosukasen/","https://suumo.jp/chintai/tokyo/en_shonanshinjukulinetakasakitokaidosen/","https://suumo.jp/chintai/tokyo/en_tokaidoshinkansen/","https://suumo.jp/chintai/tokyo/en_joetsushinkansen/","https://suumo.jp/chintai/tokyo/en_hokurikushinkansen/","https://suumo.jp/chintai/tokyo/en_tohokushinkansen/","https://suumo.jp/chintai/tokyo/en_ginzasen/","https://suumo.jp/chintai/tokyo/en_marunouchisen/","https://suumo.jp/chintai/tokyo/en_hibiyasen/","https://suumo.jp/chintai/tokyo/en_tozaisen/","https://suumo.jp/chintai/tokyo/en_chiyodasen/","https://suumo.jp/chintai/tokyo/en_yurakuchosen/","https://suumo.jp/chintai/tokyo/en_hanzomonsen/","https://suumo.jp/chintai/tokyo/en_nambokusen/","https://suumo.jp/chintai/tokyo/en_fukutoshinsen/","https://suumo.jp/chintai/tokyo/en_seibuyurakuchosen/","https://suumo.jp/chintai/tokyo/en_seibushinjukusen/","https://suumo.jp/chintai/tokyo/en_seibuikebukurosen/","https://suumo.jp/chintai/tokyo/en_seibuhaijimasen/","https://suumo.jp/chintai/tokyo/en_seibuyamaguchisen/","https://suumo.jp/chintai/tokyo/en_seibukokubunjisen/","https://suumo.jp/chintai/tokyo/en_seibutamagawasen/","https://suumo.jp/chintai/tokyo/en_seibutamakosen/","https://suumo.jp/chintai/tokyo/en_seibuseibuensen/","https://suumo.jp/chintai/tokyo/en_seibutoshimasen/","https://suumo.jp/chintai/tokyo/en_tobutojosen/","https://suumo.jp/chintai/tokyo/en_tobuisesakisen/","https://suumo.jp/chintai/tokyo/en_tobukameidosen/","https://suumo.jp/chintai/tokyo/en_tobudaishisen/","https://suumo.jp/chintai/tokyo/en_tokyutoyokosen/","https://suumo.jp/chintai/tokyo/en_tokyudenentoshisen/","https://suumo.jp/chintai/tokyo/en_tokyuikegamisen/","https://suumo.jp/chintai/tokyo/en_tokyumegurosen/","https://suumo.jp/chintai/tokyo/en_tokyutamagawasen/","https://suumo.jp/chintai/tokyo/en_tokyuoimachisen/","https://suumo.jp/chintai/tokyo/en_tokyusetagayasen/","https://suumo.jp/chintai/tokyo/en_toeiasakusasen/","https://suumo.jp/chintai/tokyo/en_toeimitasen/","https://suumo.jp/chintai/tokyo/en_toeishinjukusen/","https://suumo.jp/chintai/tokyo/en_toeioedosen/","https://suumo.jp/chintai/tokyo/en_todenarakawasen/","https://suumo.jp/chintai/tokyo/en_nipporitoneriliner/","https://suumo.jp/chintai/tokyo/en_keioinokashirasen/","https://suumo.jp/chintai/tokyo/en_keiokeibajosen/","https://suumo.jp/chintai/tokyo/en_keioshinsen/","https://suumo.jp/chintai/tokyo/en_keiosen/","https://suumo.jp/chintai/tokyo/en_keiodobutsuensen/","https://suumo.jp/chintai/tokyo/en_keiosagamiharasen/","https://suumo.jp/chintai/tokyo/en_keiotakaosen/","https://suumo.jp/chintai/tokyo/en_keiseioshiagesen/","https://suumo.jp/chintai/tokyo/en_keiseikanamachisen/","https://suumo.jp/chintai/tokyo/en_keiseihonsen/","https://suumo.jp/chintai/tokyo/en_keihinkyukohonsen/","https://suumo.jp/chintai/tokyo/en_keihinkyukokukosen/","https://suumo.jp/chintai/tokyo/en_odakyusen/","https://suumo.jp/chintai/tokyo/en_odakyutamasen/","https://suumo.jp/chintai/tokyo/en_tamatoshimonorail/","https://suumo.jp/chintai/tokyo/en_rinkaisen/","https://suumo.jp/chintai/tokyo/en_hokusosen/","https://suumo.jp/chintai/tokyo/en_tokyomonorail/","https://suumo.jp/chintai/tokyo/en_shinkotsuyurikamome/","https://suumo.jp/chintai/tokyo/en_saitamakosokutetsudosen/","https://suumo.jp/chintai/tokyo/en_tsukubaexpress/","https://suumo.jp/chintai/tokyo/en_naritaskyaccess/"]
    tokyo_area_list = ["千代田区", "中央区", "港区", "新宿区", "文京区", "台東区", "墨田区", "江東区", "品川区", "目黒区", "大田区", "世田谷区", "渋谷区",
                       "中野区", "杉並区", "豊島区", "北区", "荒川区", "板橋区", "練馬区", "足立区", "葛飾区", "江戸川区"]


    for item1,item2 in zip(lines_list_url,line_list_name):
        response = requests.get(item1)
        selector = etree.HTML(response.text)
        station = selector.xpath('//div/ul/li/label/span[1]/text()')
        for_id = selector.xpath('//div/ul/li/label/@for')
        station_data_list = re.findall(re.compile('<span class="searchitem-list-value">(.*?)</span>', re.S),
                                       response.text)
        num_data_list = [re.findall(re.compile('\d+', re.S), x)[0] for x in station_data_list]
        for i1,i2,num in zip(station,for_id,num_data_list):
            if num != "0":
                try:

                    one_station_url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=013&cb=0.0&ct=9999999&et=10&cn=9999999&mb=0&mt=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&fw2=&ek={0}&rn=0005&srch_navi=1".format(i2[2:])
                    response = requests.get(one_station_url)
                    selector = etree.HTML(response.text)
                    station_2_area = selector.xpath('/html/body/div[3]/div/ol/li[4]/a/text()')
                    ff_l = []
                    f_tup = (item2,i1,station_2_area[0],one_station_url)
                    ff_l.append((f_tup))
                    print(ff_l)
                    insertDB(ff_l,"line_station_area")
                except:
                    pass








#_line,_station,_area,_10minutes_URL
# create table line_station_area (id int not null primary key auto_increment,
# _line text,
# _station text,
# _area text,
# _10minutes_URL text,
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;


#  drop table line_station_area;