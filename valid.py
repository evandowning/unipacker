# Scans unipacker samples to see if they are likely valid or not

import sys
import os
import lief
from collections import Counter

def usage():
    sys.stderr.write('python valid.py unpacked_sample\n')
    sys.exit(2)

def _main():
    if len(sys.argv) != 2:
        usage()

    fn = sys.argv[1]

    pe = lief.parse(fn)

    ep = pe.optional_header.addressof_entrypoint

    it = pe.data_directory(lief.PE.DATA_DIRECTORY.IMPORT_TABLE)

    sys.stdout.write('{0}: {1} {2} {3}\n'.format(fn,hex(ep),hex(it.rva),it.size))

    flag = False

    try:
        pe.section_from_rva(ep)
    except lief.not_found:
        sys.stdout.write('Error EP not in a section\n')

    if it.size == 0:
        sys.stdout.write('Error IT\n')

if __name__ == '__main__':
    _main()
