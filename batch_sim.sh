#!/bin/bash
###
 # @Author: Wang Zongwu
 # @Date: 2021-06-06 00:04:44
 # @LastEditTime: 2022-04-03 18:51:52
 # @LastEditors: Wang Zongwu
 # @Description: Run the simulation for all traces in the folder "dpc3_traces"
 # @FilePath: /ChampSim/batch_sim.bash
### 

# Parameters
# $1: binary
# $2: N_WARM
# $3: N_SIM


if [ $# -ne 1 ]
then
    echo "one input for bp parameter is needed"
    exit
fi

binary=$1-no-no-no-no-lru-1core

./build_champsim.sh $1 no no no no lru 1

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
python scripts/extractResults.py $binary