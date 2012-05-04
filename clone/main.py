from pprint import pprint
DIGITS = {
    0 : (
    ' _ ', 
    '| |', 
    '|_|'),
    1 : (
    '   ', 
    '  |', 
    '  |'),
    2 : (
    ' _ ', 
    ' _|', 
    '|_ '),
    3 : (
    ' _ ', 
    ' _|', 
    ' _|'),
    4 : (
    '   ',
    '|_|',
    '  |'),
    5 : (
    ' _ ', 
    '|_ ', 
    ' _|'),
    6 : (
    ' _ ', 
    '|_ ', 
    '|_|'),
    7 : (
    ' _ ', 
    '  |',
    '  |'),
    8 : (
    ' _ ', 
    '|_|', 
    '|_|'),
    9 : (
    ' _ ', 
    '|_|', 
    ' _|')
    }

inverted = dict((v,k) for (k,v) in DIGITS.items())


def parse_lines(lines):
    ocred_digits = list()
    number_of_digits = len(lines[0])/3
    for digit in range(0,number_of_digits):
        a_digit =  (lines[0][digit*3:((digit+1)*3)],
                             lines[1][digit*3:((digit+1)*3)],
                             lines[2][digit*3:((digit+1)*3)])

        try:
            ocred_digits.append(inverted[a_digit])
        except Exception, e:
            print e
            ocred_digits.append(None)
    return ocred_digits


if __name__ == '__main__':
    print "start"
    all_lines = open("input.txt").readlines()
    line = 0
    while True:
        print parse_lines([all_lines[line], all_lines[line + 1], all_lines[line + 2]])
        line += 4
        
        


