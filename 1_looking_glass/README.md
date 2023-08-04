This directory is used to infer the geographical location of the Looking Glass and the API of ping that can automatically be used.

Requirment: You should put the file `websites.txt` which contains Looking Glass's websites to the directory `data`. We have given this file as a demo.

Tips_01: `0_getwebpages` crawl the content of websites in the file `data/websites.txt` and put the each reuslt file in the directory `data/webpages`. We have given our collected data as `webpages.tar.gz` file in that directory, you can unzip this file and skip execution of `0_getwebpages`.

Tips_02: This output of this directory is the file `dict_lg_info.bin` in the directory `pickle_bin`. We have given our result. So you can skip the step totally :)

Note: Thanks very much to the authors of the paper 'Zhuang S, Wang J H, Wang J, et al. Discovering obscure looking glass sites on the web to facilitate internet measurement research[C]//Proceedings of the 17th International Conference on Emerging Networking EXperiments and Technologies. 2021: 426-439.', we get the looking glass websites from their open source data.
