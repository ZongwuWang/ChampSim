'''
Author: Wang Zongwu
Date: 2022-03-22 18:59:08
LastEditTime: 2022-03-22 23:14:52
LastEditors: Wang Zongwu
Description: Extract performance from results folder
FilePath: /tmp/home/wzw/Documents/ACA_Proj/Tools/ChampSim/scripts/extractResults.py
Mail: wangzongwu@sjtu.edu.cn
Please ask for permission before quote the code.
'''
import sys
import os
import re

Workspace = os.path.abspath(".")

def extraction(sim_model):
	if not os.path.exists(os.path.join(Workspace, 'results_10M')):
		print("Default results folder is not exist!!!")
		return -1;
	else:
		results_fold = os.path.join(Workspace, 'results_10M')
		print(results_fold)
		with open(os.path.join(Workspace, 'ExtractResults/%s.csv' % sim_model), 'w') as fw:
			p = re.compile(r'Branch Prediction Accuracy: ([0-9.%]*).*?MPKI: ([0-9.%]*).*?NOT_BRANCH: [0-9]* ([0-9.%]*).*?BRANCH_DIRECT_JUMP: [0-9]* ([0-9.%]*).*?BRANCH_INDIRECT: [0-9]* ([0-9.%]*).*?BRANCH_CONDITIONAL: [0-9]* ([0-9.%]*).*?BRANCH_DIRECT_CALL: [0-9]* ([0-9.%]*).*?BRANCH_INDIRECT_CALL: [0-9]* ([0-9.%]*).*?BRANCH_RETURN: [0-9]* ([0-9.%]*)', re.DOTALL)
			fw.write("bench_name,bp_method,BP_ACCURACY,MPKI,NOT_BRANCH,BRANCH_DIRECT_JUMP,BRANCH_INDIRECT,BRANCH_CONDITIONAL,BRANCH_DIRECT_CALL,BRANCH_INDIRECT_CALL,BRANCH_RETURN\n")
			for root, dirs, files in os.walk(results_fold):
				for filename in files:
					if sim_model in filename:
						# extract information in filename
						fn_list = filename.split('.')
						bench_name = fn_list[1]
						sim_model = fn_list[3]
						bp_method = sim_model.split('-')[1]
						# ExtractResultsFolder = os.path.join(Workspace, 'ExtractResults')
						with open(os.path.join(results_fold, filename), 'r') as fr:
							match = p.findall(fr.read())
							assert len(match)!=0
							fw.write("%s,%s,%s\n" % (bench_name, bp_method, ",".join(match[0])))


if __name__ == "__main__":
	# sim_model = 'bimodal-no-no-no-no-lru-1core'
	# sim_model = 'my_GAg-no-no-no-no-lru-1core'
	print(sys.argv[1])
	extraction(sim_model=sys.argv[1])