import os
import pandas as pd
import re

os.chdir('../phen')
gen_df = pd.read_csv('2020.10.13.all_benk_amrfinder_res.one_sample_per_line.tsv',delimiter='\t')

def phen():
    '''Manipulating the phenotype_df'''
    phen_df = pd.read_csv('2020.10.28.BenK_rtype_str.txt', delimiter='\t')
    print(phen_df.info)
    # rename Sample_ID for phen_df & make it index then split the Sam_ from all rows & reset the index
    # phen_df = phen_df.rename(columns={'Sample ID': 'Sample'}).set_index('Sample')
    # phen_df.rename(index={index: ''.join(index.split('Sample_')) for index in phen_df.index}, inplace=True)
    # phen_df.reset_index(inplace=True)
    # print(phen_df)

def gen():
    '''Manipulating gen_df'''
    # set Sample col as index & rename
    gen_df.set_index('Sample', inplace=True)
    # print(gen_df)
    gen_df.rename(index={index: re.search(r'\d+-\w+$', index).group() for index in gen_df.index}, inplace=True)
    gen_df.reset_index(inplace=True)
    # print(gen_df)

# # merging the manipulated dfs i.e phen & gen
# phen_gen_merge = pd.merge(phen_df,gen_df,on='Sample')
# # dropping null valuesim
# dropped= phen_gen_merge.dropna(axis=1,how='all')
# # dropped.to_excel('Phen_Geno_Match.xlsx',index=False)    # install openpyxl module.........
# dropped.to_csv('Pheno_Geno_Match.csv',index=False)
# # print(dropped.compare(phen_df))
# # print(phen_gen_merge)

phen()

