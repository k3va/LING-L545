line = sys.stdin.readline()
while line != '':
    for token in line.split(' '):
        if token.strip() == '':
            continue
        if token[-1] == '.':
            if token in ['']:
                sys.stdout.write(token + ' ')
            else:
                sys.stdout.write(token + '\n')
        else:
            sys.stdout.write(token + ' ')
    line = sys.stdin.readline()
