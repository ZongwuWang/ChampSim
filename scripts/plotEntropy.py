import numpy as np
import matplotlib.pyplot as plt
import os
import re
import seaborn as sns

def plotEntropy():
	path = '/home/wzw/Documents/ACA_Proj/Tools/ChampSim/EntropyRateResults'

	if os.path.exists(path):
		files = os.listdir(path)
	else:
		print('Path not exist!!!')
		os.kill()

	fig, ax = plt.subplots(figsize=(20, 14))
	with open('ExtractResults/aveEntropy.csv', 'w') as fw:
		for file in files:
			with open("%s/%s" % (path, file), 'r') as fr:
				bench = '_'.join(file.split('.')[1:2])
				print(bench)
				p = re.compile(r'Entropy{([0-9.]*)}', re.DOTALL)
				match = p.findall(fr.read())
				match = list(map(float, match))
				kwargs = {'cumulative': True}
				# sns.distplot(match, hist_kws=kwargs, kde_kws=kwargs)
				sns.distplot(match, hist=False, kde_kws={'cumulative': True}, label=bench+"_%.2f" % np.average(np.array(match)), ax=ax)
				fw.write("%s,%.2f\n" % (bench, np.average(np.array(match))))
		plt.legend()
		plt.savefig("ExtractResults/dpcTraceEntropy.png", dpi=900, bbox_inches='tight')
		plt.show()

if __name__ == '__main__':
	plotEntropy()
