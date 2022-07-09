# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime
import time

import pymysql
import pandas as pd

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import json
import datetime






def writeinto_jsonfile(filename, list_data):
    with open(filename, 'w', encoding='utf-8') as fw:
        json.dump(list_data, fw, indent=4, ensure_ascii=False)


if __name__ == "__main__":

    engine_ = create_engine('mysql+pymysql://root:123456@localhost:3306/JP_RealEstate')

    tokyo_area_list = ["千代田区", "中央区", "港区", "新宿区", "文京区", "台東区", "墨田区", "江東区", "品川区", "目黒区", "大田区", "世田谷区", "渋谷区",
                       "中野区", "杉並区", "豊島区", "北区", "荒川区", "板橋区", "練馬区", "足立区", "葛飾区", "江戸川区"]

    f_result = []
    station_result = {}
    area_result = {}
    area_result["area"] = []
    for item_area in tokyo_area_list:

        # area----->station---url-> area_station_json
        # station---->line---->
        sql_tsn = 'select _station from line_station_area where _area= "{0}"  ; '.format(item_area)
        df_js225 = pd.read_sql_query(sql_tsn, engine_)
        list_set_station = list(set(x[0] for x in df_js225.values.tolist()))

        #[station:lines]

        list_set_station_line = []
        for item_station in list_set_station:
            # one_station = {}
            # one_station[]
            list_set_station_line.append({item_station:[x[0] for x in pd.read_sql_query('select _line from line_station_area where _station= "{0}"  ; '.format(item_station),engine_).values.tolist()]})



        f_result.append({item_area:list_set_station_line})

        # area_result["area"].append(station_result["station"])

    writeinto_jsonfile("area_station_line.json",f_result)







    #_line,_station,_area,_10minutes_URL
# create table line_station_area (id int not null primary key auto_increment,
# _line text,
# _station text,
# _area text,
# _10minutes_URL text,
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;


#  drop table line_station_area;