import sys

args = sys.argv[1:]
if args:
   tmp = ' '.join(args[::1])
   swap  = tmp.swapcase()
   print(swap[::-1])
else:
   exit