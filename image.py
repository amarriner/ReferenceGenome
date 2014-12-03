#!/usr/bin/env python

import codecs
import gd
import os
import sys

TOTAL = 252663704
max = 692229 # 692229.32602739726027397260273973
max = 28842 # 28842.888584474885844748858447489
px = 832 # 832.00300480226632412277248531337
px = 169 # 169.82932608945959071873423565385
size = 5

iter = 0
if os.path.exists("iter"):
   f = codecs.open("iter", "r", "utf-8")
   iter = int(f.read().replace("\n",""))
   f.close()

nucleic_acids = {
   "A": {"name": "Adenine" , "count": 0, "color": (240, 0, 0)},
   "C": {"name": "Cytosine", "count": 0, "color": (0, 240, 0)},
   "G": {"name": "Guanine" , "count": 0, "color": (0, 0, 240)},
   "T": {"name": "Thymine" , "count": 0, "color": (210, 145, 0)},
   "N": {"name": "Unknown" , "count": 0, "color": (80, 80, 80)}
}

def make_image():

   global nucleic_acids

   with codecs.open("chromosome01.txt", "r", "utf-8") as f:

      img = gd.image((px * size, px * size))

      bg = img.colorAllocate((255, 255, 255))
      img.fill((0, 0), bg)

      colors = {}
      for n in nucleic_acids.keys():
         colors[n] = img.colorAllocate(nucleic_acids[n]["color"])

      i = 0
      j = 0
      k = 0

      #f.seek(iter * max)
      print "From " + str(iter * max + 1) + " to " + str(iter * max + max)

      while True:
         c = f.read(1).upper()

         if (iter * max + 1) <= k and k <= (iter * max + max) and k <= TOTAL:

            if not c:
               break
            else:

               if i >= px:
                  i = 0
                  j += 1

                  if j >= px:
                     break

               nucleic_acids[c]["count"] = nucleic_acids[c]["count"] + 1
               # img.setPixel((i, j), colors[c])
               img.filledRectangle((i * size, j * size), (i * size + size - 1, j * size + size - 1), colors[c])

               i += 1
 
         k += 1

      
      img.writePng("chrom.png")

      f.close()


def check_math():
   i = 0
   while (i * max) < TOTAL:
      print str(i) + " :: From " + str(i * max + 1) + " to " + str(i * max + max) + \
                     " of " + str(TOTAL) + ", diff: " + str((i * max + max) - (i * max + 1))
      i += 1

def main():
   make_image()   

   for n in nucleic_acids.keys():
      print nucleic_acids[n]["name"] + ": " + str(nucleic_acids[n]["count"])

 
if __name__ == "__main__":
   sys.exit(main())
