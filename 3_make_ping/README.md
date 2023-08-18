In this directory, we use our collected Looking Glasses to ping collected end points. 

### Output
The output will be located in the subdirectory `pickle_bin`. The output is used for the next stage, we have given those demo files in that directory. You can skip this stage :-)

### Requirement
1. This directory needs two source files, which should be put in the subdirectory `src`: `dict_server_info.bin` and `dict_client_info.bin`. Both of these two files have the following form: `{ ip1: {k11:v11, k12:v12, ..}, ip2: {k21:v21, k22:v22, ..}, ...  }`.

- `dict_server_info.bin`: this file contains the LGs we can use which can be acquired by the folder `1_looking_glass`. For each ip, the dictionary `dict_server_info[ip]` must have keyword 'coordinate'.
- `dict_client_info.bin`: this file can be acquired by the folder `2_end_points`, whose subfolders output some information of the end points. For each ip, there is no keyword requirement for dictionary `dict_client_info[ip]`.


2. We recommend that you should first use a small number of endpoints and then filter the good Looking Glasses.
