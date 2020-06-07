import sys
import os
from hashlib import sha256

def usage():
    sys.stderr.write('usage: python check_duplicate_list.py binaries.txt\n')
    sys.exit(2)

def _main():
    if len(sys.argv) != 2:
        usage()

    fn = sys.argv[1]

    h = dict()

    # Get SHA256 values for each sample
    with open(fn,'r') as fr:
        for line in fr:
            line = line.strip('\n')

            # Get sha256 value
            val = sha256(open(line,'rb').read()).hexdigest()

            if val not in h.keys():
                h[val] = list()
            h[val].append(line)

    # Print out deduplicated set
    for k,v in h.items():
        sys.stdout.write('{0}\n'.format(v[0]))

if __name__ == '__main__':
    _main()
