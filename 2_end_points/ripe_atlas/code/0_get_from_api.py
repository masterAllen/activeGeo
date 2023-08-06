from ripe.atlas.cousteau import AtlasRequest
import json
import pickle

data_file = open('../data/0_ripe_atlas.txt', 'w')
list_ripe_atlas = []

def deal_one_result(result):
    if result['status']['id'] not in {1, 2}:
        return None

    position = result['geometry']
    if position is None or result['country_code'] is None:
        return None

    if position['type'] != 'Point':
        return None

    if result['address_v4']:
        ipinfo = {
            'ip': result['address_v4'],
            'ipv6': result['address_v6'],
            'coordinate': result['geometry']['coordinates'],
        }
        return ipinfo
    return None


base_path = "/api/v2/probes"
idx = 0
while True:
    idx += 1
    print(idx)

    url_path = base_path + f'?page={idx}'
    request = AtlasRequest(**{"url_path": url_path})
    (is_success, response) = request.get()

    if not is_success: break

    for result in response['results']:
        ipinfo = deal_one_result(result)
        if ipinfo is not None:
            list_ripe_atlas.append(ipinfo)
            data_file.writelines( json.dumps(ipinfo, ensure_ascii=False) + '\n' )

    if response['next'] is None:
        break

pickle.dump(list_ripe_atlas, open('../pickle_bin/ripe_atlas.bin', 'wb'))
