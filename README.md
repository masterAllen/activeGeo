# Introduction

Official code for the paper [A cheap and accurate delay-based IP Geolocation method using Machine Learning and Looking Glass](https://ieeexplore.ieee.org/document/10186436), IFIP Networking 2023 

Authors: [Allen Hong](https://github.com/masterAllen), [Yahui Li](https://www.insc.tsinghua.edu.cn/info/1157/3380.htm), [Han Zhang](https://www.insc.tsinghua.edu.cn/info/1157/2458.htm), Ming Wang, [Changqing An](https://www.insc.tsinghua.edu.cn/info/1157/2473.htm), Jilong Wang[https://www.insc.tsinghua.edu.cn/info/1157/2449.htm].

## TODO
2023/08/04

The code previously uploaded has some problems. I am reorganizing recently and will re-upload it recently. I'm sorry you'll have to wait.


## First statement
**For convenience, we refer to 'country/region' as 'country' in our project! (Using 'country or region' makes a lot of variables too long, such as `dict_city_by_country_or_region`) This project has nothing to do with politics. If you feel offended by any part of this project, please do not hesitate to contact us!**

## Requirements
Python 3.8+ is ok, then `pip install -r requirements.txt` to install the required packages:)

## Usage
Each directory has a subdirectory called `code`, execute py files then get result. 

The respective roles of each directory are as follows:
- `0_location_hint`: building some location hint dictionaries.
- `1_looking_glass`: getting the location and api of Looking Glasses.
- `2_end_points`: collecting some end points.
- `3_make_ping`: using Looking Glass to make measurement.
- `4_make_geo`: geolocating with our measurement data.

## FAQ
Q: Why is there no reproduction code for related work?

Q: Why are there some differences in the results of the evaluation phase?

