import sys
import os

from unipacker.core import Sample
from unipacker.io_handler import IOHandler

def usage():
    sys.stderr.write('usage: python single.py sample.exe\n')
    sys.exit(2)

def _main():
    if len(sys.argv) != 2:
        usage()

    fn = sys.argv[1]

    print(fn)

    # Get root folder
    folder = '/'.join(fn.split('/')[:-1])

    if not os.path.exists(fn):
        sys.stderr.write('{0} does not exist\n'.format(fn))
        exit(1)

    try:
        samples = list()
        samples.extend(Sample.get_samples(fn, interactive=False))
        IOHandler(samples, folder, False)
    except Exception as e:
        sys.stderr.write('singple.py Exception: {0}\n'.format(str(e)))

    sys.stdout.write('=================================================\n')
    sys.stdout.write('=================================================\n')

if __name__ == '__main__':
    _main()
