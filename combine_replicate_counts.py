import os, sys, glob


'''
    AUTHOR: SHWETHA HARA SRIDHAR
    TECHDEV TEAM, DEPARTMENT OF GENETICS AND GENOMICS
    ICAHN SCHOOL OF MEDICINE AT MOUNT SINAI, NY
    VERSION: 19.7.18
    
    INPUT: FEATURE COUNTS OF A CONDITION WITH/WITHOUT REPLICATES
    OUTPUT: .CSV WITH COMBINED COUNTS FOR ALL THE GENES
'''


def combine_counts(path, file_format="*.txt"):

    data = {}
    sample_name = []
    os.chdir(path)
    outfile = open(path.split("/")[-1]+"_CombinedCounts.csv", "w")

    for filename in glob.glob(os.path.join(path, file_format)):

        file = open(filename, "r")
        skip_line = file.readline()
        header = file.readline()
        colname = header.strip().split("\t")[-1]
        sample_name.append(colname)

        for line in file:
            ensmbl = line.strip().split("\t")[0]
            counts = line.strip().split("\t")[-1]

            if ensmbl in data:
                if colname in data[ensmbl]:
                    data[ensmbl][colname] += counts
                else:
                    data[ensmbl][colname] = counts

            else:
                data[ensmbl]= {}
                if colname in data[ensmbl]:
                    data[ensmbl][colname] += counts
                else:
                    data[ensmbl][colname] = counts

    sys.stdout = outfile

    print("GeneID, ", ", ".join(sample_name)+", remove")

    for ensemble, info in data.items():
        print(ensemble, end = ", ")
        for i in range(len(sample_name)):
            print(info[sample_name[i]], end =", ")
        print("")
    outfile.close()
    return outfile


## MAIN ##


path = "/Candida/Candida_featurecounts"
files = os.listdir(path)
print(files)
for file in files:
    print(combine_counts(path+"/"+file))
