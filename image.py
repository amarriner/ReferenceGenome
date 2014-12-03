#!/usr/bin/env python

import codecs
import gd
import os
import sys

# Total number of acids
TOTAL = 252663704

# Number of acids we will process per run
max = 28842 # 28842.888584474885844748858447489

# Image size will be px * size
# px is the square root of max (above)
px = 169 # 169.82932608945959071873423565385
size = 5

# The iteration we're on. If we haven't iterated before it's zero,
# otherwise get it from a file
iter = 0
if os.path.exists("iter"):
   f = codecs.open("iter", "r", "utf-8")
   iter = int(f.read().replace("\n",""))
   f.close()

# Information on each possible acid: name, count in this iteration, and color to use
nucleic_acids = {
   "A": {"name": "Adenine" , "count": 0, "color": (240, 0, 0)},
   "C": {"name": "Cytosine", "count": 0, "color": (0, 240, 0)},
   "G": {"name": "Guanine" , "count": 0, "color": (0, 0, 240)},
   "T": {"name": "Thymine" , "count": 0, "color": (210, 145, 0)},
   "N": {"name": "Unknown" , "count": 0, "color": (80, 80, 80)}
}

def make_image():
   """Builds an image from a sequence of nucleic acids"""

   global nucleic_acids

   # Chromosome from Project Gutenberg's Human Genome Project files:
   # http://www.gutenberg.org/ebooks/subject/15882
   # See README.md for details
   with codecs.open("chromosome01.txt", "r", "utf-8") as f:

      # Create new image
      img = gd.image((px * size, px * size))

      # Fill it with a background color
      bg = img.colorAllocate((255, 255, 255))
      img.fill((0, 0), bg)

      # Assign colors from nucleic_acids hash to image colors
      # Apparently can't do this on the fly for each acid because
      # there seems to be a limit on the number of times one can
      # do this per image?
      colors = {}
      for n in nucleic_acids.keys():
         colors[n] = img.colorAllocate(nucleic_acids[n]["color"])

      # Counters
      i = 0
      j = 0
      k = 0

      # Seek past undeeded bytes
      f.seek(iter * max)

      while True:
         # Read bytes until we're at the end of the file or until we're out
         # of the range of acids for this iteration
         c = f.read(1).upper()

         if (iter * max) <= k and k < (iter * max + max) and k <= TOTAL:

            # We're at the end of the file
            if not c:
               break

            # Otherwise process the byte
            else:

               # Increment rows if we're at the end of one
               if i >= px:
                  i = 0
                  j += 1

                  # If we're past the max number of rows, quit
                  if j >= px:
                     break

               # Increment acid count and place rectangle on the image
               nucleic_acids[c]["count"] = nucleic_acids[c]["count"] + 1
               img.filledRectangle((i * size, j * size), (i * size + size - 1, j * size + size - 1), colors[c])

               i += 1
 
         k += 1
      
      # Write the resulting image
      img.writePng("chrom.png")

      f.close()

   # Increment and write the iteration number
   f = codecs.open("iter", "w", "utf-8")
   f.write(str(iter + 1))
   f.close()


def main():
   make_image()   

   print "From " + str(iter * max) + " to " + str(iter * max + max - 1)
   for n in nucleic_acids.keys():
      print nucleic_acids[n]["name"] + ": " + str(nucleic_acids[n]["count"])

 
if __name__ == "__main__":
   sys.exit(main())
