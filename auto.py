import sys
import os

from unipacker.core import Sample
from unipacker.io_handler import IOHandler

def usage():
    sys.stderr.write('usage: python auto.py samples.txt\n')
    sys.exit(2)

def _main():
    if len(sys.argv) != 2:
        usage()

    samplesFN = sys.argv[1]

    samples = list()

    # Get samples to run unpacking on
    with open(samplesFN,'r') as fr:
        for line in fr:
            line = line.strip('\n')
            samples.append(line)

    # For each sample
    for fn in samples:
        folder = '/'.join(fn.split('/')[:-1])
        print(folder,fn)

        if not os.path.exists(fn):
            sys.stderr.write('{0} does not exist\n'.format(fn))
            continue

        try:
            samples = list()
            samples.extend(Sample.get_samples(fn, interactive=False))
            IOHandler(samples, folder, False)
        except Exception as e:
            sys.stderr.write('auto.py Exception: {0}\n'.format(str(e)))

        sys.stdout.write('=================================================\n')
        sys.stdout.write('=================================================\n')

if __name__ == '__main__':
    _main()
