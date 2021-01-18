import re
import sys
# Two inputs to the pg i.e mlst result and the senterica db file
read_ml = open('../mlst_overall.txt').readlines()
read_db = open('../senterica.txt').readlines()


def profile():
    """Given an allelic profile it returns the ST"""
    st_profile = {}
    for line in read_db[1:]:
        split_line = line.strip().split('\t')
        st = split_line[0]
        print(split_line)
        st_prof = '-'.join(split_line[1:])

        #st = re.search(r'\d+', ''.join(line)).group()
        #st_prof = '-'.join(re.findall(r'\d+', ''.join(line[len(st):])))
        #s = {st_prof: st}
        assert st_prof not in st_profile
        st_profile[st_prof] = st
        #if st_prof in st_profile:
        #    print(f'Key {st_prof} already in dictionartry')
        #    sys.exit()
        #else:
        #    st_profile[st_prof] = st
        #st_profile.update(s)
    return st_profile


def matching():
    """Processes all the samples & printing all the results to screen"""
    s_prof = profile()
    for line in read_ml:
        al_prof = '-'.join(re.findall(r'\d+', ''.join(line)))
        # continuing with matching
        #print("contigs.fa\tsenterica\t" + s_prof[al_prof] + " " + line)
        print("contigs.fa", "senterica", s_prof[al_prof], line, sep = '\t')



matching()
