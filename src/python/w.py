#!/usr/bin/env python
# -*- coding: utf-8 -*-
#------------------------------------------------
# author: junjiemars@gmail.com
# target: weather bot 
#------------------------------------------------

from bs4 import BeautifulSoup
import platform
import json, urllib
import sys
from os.path import basename
import locale, codecs

debug = 0
verbose = 0
sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)

def decode_text(s):
    if s: return s.decode('utf8')
    return s

def dump_json(j):
    return json.dumps(j,
                      indent=2,
                      separators=(',', ': '),
                      ensure_ascii=False,
                      encoding='utf-8')

def debug_output(msg):
    if debug:
        print(msg)
        print('------------')

def verbose_json(j):
    if verbose: return dump_json(j)
    return json.dumps(j)

def version(argv):
    print('%s %s (%s)' % (basename(argv[0]), '0.1.0', platform.platform()))
    sys.exit(0)

def usage(argv, xcode):
    print('usage: %s' % basename(argv[0]))
    print('\t[-c city]\t\t specify city')
    print('\t[-a area]\t\t specify the area of city')
    print('\t[-i input]\t\t input file or url, default @file')
    print('\t[-o output]\t\t output to @file, default stdout')
    print('\t[-r retry]\t\t retry times')
    print('\t[-d debug]\t\t debug')
    print('\t[-v verbose]\t\t verbosity')
    print('\t[-h help]\t\t help')

    return (xcode)

def main(argv):
    import getopt
    global debug, verbose
    city = 'nanjing'
    area = ''
    input_ = None
    output_ = None
    retry = 1

    if (1 == len(argv)): return (usage(argv, 0))
    
    try:
        (opts, args) = getopt.getopt(sys.argv[1:],
                                     ':c:a:i:o:rhdvV',
                                     ['city=','area=',
                                      'input=', 'output=', 'retry=',
                                      'help', 'debug','verbose','version'])
    except getopt.GetoptError, err:
        print(str(err)+'!')
        return (usage(100))

    for (k, v) in opts:
        if k in   ('-c', '--city'): city = v
        elif k in ('-a', '--area'): area = v
        elif k in ('-i', '--input'): input_ = v
	elif k in ('-o', '--output'): output_ = v
        elif k in ('-d', '--debug'): debug += 1
        elif k in ('-v', '--verbose'): verbose += 1
	elif k in ('-r', '--retry'): retry = int(v)
	elif k in ('-h', '--help'): return(usage(argv, 0))
	elif k in ('-V', '--version'): version(argv)
	else: return (200)

    for i in range(retry):
        r = 0 #post(url, arg, i)
        if 0 == r: break
	return (0)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
