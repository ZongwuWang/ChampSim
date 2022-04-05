#!/bin/bash
###
 # @Author: Wang Zongwu
 # @Date: 2021-06-06 00:04:44
 # @LastEditTime: 2022-04-05 20:16:30
 # @LastEditors: Wang Zongwu
 # @Description: Run the simulation for all traces in the folder "dpc3_traces" to calculate Entropy, please make sure #define ENTROPY is set before simulation.
 # @FilePath: /ChampSim/batch_simEntro.sh
### 

# Parameters
# $1: binary
# $2: N_WARM
# $3: N_SIM


# if [ $# -ne 1 ]
# then
#     echo "one input for bp parameter is needed"
#     exit
# fi

rm ToggleRateResults/*

binary=calEntropy-no-no-no-no-lru-1core

./build_champsim.sh calEntropy no no no no lru 1

N_WARM=1
N_SIM=10

files=$(ls ./dpc3_traces)

for file in $files
do
    echo `basename $file`
    ./run_champsim.sh $binary $N_WARM $N_SIM $file &
done

filter=${binary:0:8}

while
    effProc=`ps -u wzw | grep $filter | wc -l`
    [[ effProc -gt 0 ]]
do 
echo "${effProc} procedure left";
sleep 5;
done

echo "Start extract simulation results"

echo $binary
python scripts/plotEntropy.py