# 筛选使用了模板 LookingGlass 的网页
import os
import re
import sys
import pickle
from bs4 import BeautifulSoup

WEBPAGES_DIR = f'../../data/webpages/'
SRC_WEBSITES_FILE = sys.argv[1]
IDX = sys.argv[2]

# 1. using this template and get information sucessfully
# 2. using this template but fail to get information
# 3. not using this template
DST_FILES_DIR = f'./result/template_{IDX}'
os.system(f'mkdir -p {DST_FILES_DIR}')

TBD_WEBSITES_FILE = open(f'{DST_FILES_DIR}/tbd_websites.txt', 'w')
BAD_WEBSITES_FILE = open(f'{DST_FILES_DIR}/bad_websites.txt', 'w')

ipv4 = 'ipv4'
ipv6 = 'ipv6'
def get_items_from_webpage(soup, pos_begin):
    (position, v4, v6) = ('None', 'None', 'None')
    for elem in soup(text=re.compile(pos_begin, re.IGNORECASE)):
        info_block = elem.parent.parent
        list_info = info_block.get_text().split('\n')

        for info in list_info:
            # 为了确保是 xx: yyy 的形式
            if ':' not in info: continue

            try:
                if re.search(pos_begin, info, re.IGNORECASE):
                    position = info.split(':')[1].strip()
                elif re.search(ipv4, info, re.IGNORECASE):
                    v4 = info.split(':')[1].split()[0]
                elif re.search(ipv6, info, re.IGNORECASE):
                    v6 = info[info.find(':')+1 : ].split()[0]
            except:
                pass
    return (position, v4, v6)


lg_keyword = 'LookingGlass'
info_keyword_china = '网络信息'
def check_one_soup(soup):
    footer = soup.footer
    if footer:
        if re.search(lg_keyword, footer.get_text()):
            if re.search('network information', soup.get_text(), re.IGNORECASE):
                return get_items_from_webpage(soup, 'location:')
            elif re.search('网络信息', soup.get_text(), re.IGNORECASE):
                return get_items_from_webpage(soup, '位置:')
            else:
                return 'TBD'
    return 'BAD'

list_good_routers = list()
with open(SRC_WEBSITES_FILE, encoding='utf-8') as srcfile:
    for idx, row in enumerate(srcfile):
        print(idx)
        website = row.strip()
        filename = website.replace('/', '_').replace(':', '.')
        filepath = f'{WEBPAGES_DIR}/{filename}.txt'

        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r') as srcfile:
            result = check_one_soup(BeautifulSoup(srcfile.read(), "lxml"))
            if result == 'BAD':
                BAD_WEBSITES_FILE.writelines(website + '\n')
            elif result == 'TBD':
                TBD_WEBSITES_FILE.writelines(website + '\n')
            else:
                one_result = {
                    'website': website,
                    'geohint': ('', result[0], ''),
                    'ipv4hint': result[1],
                    'ipv6hint': result[2],
                }
                list_good_routers.append(one_result)
pickle.dump(list_good_routers, open(f'{DST_FILES_DIR}/list_good_routers.bin', 'wb'))

for one_result in list_good_routers:
    print(one_result)
