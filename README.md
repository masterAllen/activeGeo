# Introduction

Official code for the paper [A cheap and accurate delay-based IP Geolocation method using Machine Learning and Looking Glass](https://ieeexplore.ieee.org/document/10186436), IFIP Networking 2023 

Authors: [Allen Hong](https://github.com/masterAllen), [Yahui Li](https://www.insc.tsinghua.edu.cn/info/1157/3380.htm), [Han Zhang](https://www.insc.tsinghua.edu.cn/info/1157/2458.htm), Ming Wang, [Changqing An](https://www.insc.tsinghua.edu.cn/info/1157/2473.htm), [Jilong Wang](https://www.insc.tsinghua.edu.cn/info/1157/2449.htm).

## First statement
**For convenience, we refer to 'country/region' as 'country' in our project! (Using 'country or region' makes a lot of variables too long, such as `dict_city_by_country_or_region`.) This project has nothing to do with politics! If you feel offended by any part of this project, please do not hesitate to contact us!**

## Requirements
Python 3.8+ is ok, then `pip install -r requirements.txt` to install the required packages :)

## Usage
Each directory has a subdirectory called `code`, execute `.py` files then get result. 

The respective roles of each directory are as follows:
- `0_location_hint`: Building some location hint dictionaries.
- `1_looking_glass`: Getting the location and api of Looking Glasses.
- `2_end_points`: Collecting some end points.
- `3_make_ping`: Using Looking Glass to make measurement.
- `4_make_geo`: Geolocating with our measurement data.

## FAQ
Q: Why is there no reproduction code for related work?

A: This repository is just the code of our work. Thanks very much to [the work of Zack et al](https://github.com/zackw/active-geolocator), their code is very helpful for us to reproduce the related works. You can also refer to them. If you have some problems, you can send us email to communicate.

Q: Why are there some differences in the results of the evaluation?

A: The results are highly dependent on the input data. We re-generated training and test data during each evaluation.
