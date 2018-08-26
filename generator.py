#!/usr/bin/python
import sys
from numpy import ndarray

charactersCount = 16
length = 4
symbols = [ "A", "B", "C", "D", "E", "F", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
arr =  ndarray((length,),int)
combinations = set()

TOTAL = 0
SSID = ''

result = []
def increment():
    global TOTAL
    TOTAL = TOTAL + 1

def main():
    syslen = len(sys.argv)
    if syslen != 2:
        print("usage: python generator.py NAME")
    else:
        global SSID
        SSID = sys.argv[1]    
        generate(0)
        outfile = open(SSID + '.txt', 'w')
        global result
        outfile.write("\n".join(result)) 
        outfile.close()
        print "Generated: " + SSID + ".txt"

def generate(index):
    if index >= length:
        save()
    else:
        for x in range(0, charactersCount):
            arr[index] = x
            generate(index + 1)

def save():
    global SSID
    tmp = str(48575443) + str(symbols[arr[0]]) + str(symbols[arr[1]]) + SSID + str(symbols[arr[2]]) + str(symbols[arr[3]])
    global result
    result.append(tmp)

if __name__ == "__main__":
    main()