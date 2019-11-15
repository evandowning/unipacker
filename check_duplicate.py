import sys
import os
from hashlib import sha256

def usage():
    sys.stderr.write('usage: python check_duplicate.py binaries/\n')
    sys.exit(2)

def _main():
    if len(sys.argv) != 2:
        usage()

    folder = sys.argv[1]

    family = dict()

    # Get SHA256 values for each sample
    for root,dirs,files in os.walk(folder):
        for fn in files:
            f = root.split('/')[-1]

            if f not in family:
                family[f] = dict()
                family[f]['total'] = 0
                family[f]['sha'] = set()

            path = os.path.join(root,fn)

            # Get sha256 value
            val = sha256(open(path,'rb').read()).hexdigest()

            # Add to dictionary
            family[f]['total'] += 1
            family[f]['sha'].add(val)

    famBeforeCheck = 0
    totalBeforeCheck = 0
    totalAfterCheck = 0

    famAfterFilter = 0
    totalAfterFilter = 0

    # Print out counts
    for k,v in sorted(family.items(), key=lambda x:x[1]['total'], reverse=True):
        # Focus on the families we care about
        if v['total'] > 10:
            sys.stdout.write('Family: {0}\tTotal: {1}\tUnique: {2}\n'.format(k,v['total'],len(v['sha'])))

            famBeforeCheck += 1
            totalBeforeCheck += v['total']
            totalAfterCheck += len(v['sha'])

            if len(v['sha']) > 10:
                famAfterFilter += 1
                totalAfterFilter += len(v['sha'])

    sys.stdout.write('+++++++++++++++++++++++++++++\n')
    sys.stdout.write('# families before check: {0}\n'.format(famBeforeCheck))
    sys.stdout.write('# samples before check: {0}\n'.format(totalBeforeCheck))
    sys.stdout.write('# samples after check: {0}\n'.format(totalAfterCheck))
    sys.stdout.write('+++++++++++++++++++++++++++++\n')
    sys.stdout.write('# families after check & filter: {0}\n'.format(famAfterFilter))
    sys.stdout.write('# samples after check & filter: {0}\n'.format(totalAfterFilter))

if __name__ == '__main__':
    _main()
