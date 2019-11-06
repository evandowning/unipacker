import sys

def process(content):
    if 'Error: ' in content:
        return False
    if 'Exception: ' in content:
        return False

    return True

def usage():
    sys.stderr.write('usage: python scan_output.py output.txt\n')
    sys.exit(2)

def _main():
    if len(sys.argv) != 2:
        usage()

    fn = sys.argv[1]

    sample = ''
    content = ''

    sys.stderr.write('Samples (likely) unpacked:\n')

    with open(fn,'r') as fr:
        for line in fr:
            if 'Emulation of ' in line:
                sample = line.split(' ')[2]

            # Process and reset contents
            if line == '=================================================\n':
                if (content != '') and (process(content) == True):
                    sys.stdout.write('{0}\n'.format(sample))
                content = ''
            else:
                content += line

if __name__ == '__main__':
    _main()
