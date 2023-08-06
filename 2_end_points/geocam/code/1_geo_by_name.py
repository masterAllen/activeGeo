# 从城市定位到经纬度, 通过 Geonames 数据进行融合

import os
import sys
import csv
import json
import pickle

GEO_BIN = os.path.expanduser('../../../0_location_hint/pickle_bin')
dict_country_code = pickle.load(open(f'{GEO_BIN}/dict_countryname_code.bin', 'rb'))
dict_city_by_country = pickle.load(open(f'{GEO_BIN}/dict_city_by_country.bin', 'rb'))

file_list = [
    '../data/0_pictimo_good.csv',
    '../data/0_insecam_good.csv',
]

list_geocam_result = []
result = open('../data/1_geocam_result.jsonb', 'w')
for this_f in file_list:
    with open(this_f, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            row[2] = row[2].strip().replace('-', '').replace(' ','').lower()
            if row[2] not in dict_country_code:
                print(f'{row} country name not in country_code dict')
                continue
            code = dict_country_code[row[2]].lower()

            try:
                raw_text = row[1][15:] if row[1].startswith('Live') else row[1]
                city_name = raw_text.lower().replace('-', '').replace(' ', '')
                if city_name in dict_city_by_country[code]:
                    city_info = dict_city_by_country[code][city_name]
                    one_result = {
                        'ip': row[0],
                        'city': city_name,
                        'coordinate': city_info[0],
                        'country_code': code,
                    }
                    result.writelines( json.dumps(one_result, ensure_ascii=False) + '\n' )

                    list_geocam_result.append(one_result)
            except:
                print(row)

pickle.dump(list_geocam_result, open(f'../pickle_bin/geocam.bin', 'wb'))
