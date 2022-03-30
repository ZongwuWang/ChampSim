##########################################################################
# File Name: extractResults.sh
# Author: Wang Zongwu
# mail: wangzongwu@outlook.com
# Created Time: Wed 20 Oct 2021 05:54:35 PM CST
# Description: A demo script for extracting the results(MPKI)
#########################################################################
#!/bin/bash

awk '/MPKI/{printf "%9.4f\t%s\n", $8, FILENAME}' ../results_10M/*
