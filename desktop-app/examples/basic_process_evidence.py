from __future__ import print_function
import argparse
import os
import pytsk3
import pyewf
import sys
from tabulate import tabulate

# if not admin.isUserAdmin():
#   admin.runAsAdmin()
#   sys.exit()

imagefile = "./resources/dfrws-2006-challenge.raw"
# imagefile = "./resources/ext-part-test-2.dd"
# imagefile = "./resources/fat-img-kw.dd"
# imagefile = "./resources/ID THEFT 2.E01"

imagehandle = pytsk3.Img_Info(imagefile)
print(imagehandle)
print(imagehandle.get_size())
partitionTable = pytsk3.Volume_Info(imagehandle)
print(partitionTable)
for partition in partitionTable:
  print (partition.addr)
  print (partition.desc)
  print ("%ss(%s)" , (partition.start, partition.start * 512), partition.len)