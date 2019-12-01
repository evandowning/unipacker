import sys
import os
from hashlib import sha256

def usage():
    sys.stderr.write('usage: python deduplicate.py binaries/\n')
    sys.exit(2)

def _main():
    if len(sys.argv) != 2:
        usage()

    folder = sys.argv[1]

    # Get SHA256 values for each sample
    for root,dirs,files in os.walk(folder):
        for fn in files:
            f = root.split('/')[-1]

            path = os.path.join(root,fn)

            # Get sha256 value
            val = sha256(open(path,'rb').read()).hexdigest()

            newpath = os.path.join(root,val)

            # Replace filename with new sha256 value
            os.replace(path,newpath)

            print(path,newpath)

if __name__ == '__main__':
    _main()
