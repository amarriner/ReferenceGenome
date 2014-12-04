#!/usr/bin/env python

import codecs
import gd
import keys
import os
import sys
import twitter

pwd = "/home/amarriner/python/genome/"

# Total number of acids
TOTAL = 248956422

# Number of acids we will process per run
max = 28419 # 28419.682876712328767123287671233

# Image size will be px * size
# px is the square root of max (above)
px = 168 # 168.57935816700691187858448062419
size = 5

# The iteration we're on. If we haven't iterated before it's zero,
# otherwise get it from a file
iter = 0
if os.path.exists(pwd + "iter"):
   f = codecs.open(pwd + "iter", "r", "utf-8")
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
   last = (iter * max + max)
   if last > TOTAL:
      last = TOTAL - 1

   f = codecs.open(pwd + "chromosome01.txt", "r", "utf-8")
   chromosome = f.read()[(iter * max):last]
   f.close()

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

   for c in chromosome:

      c = c.upper()

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
      
   # Write the resulting image
   img.writePng(pwd + "chrom.png")

def main():
   make_image()   

   title = "Chromosome 01 - Iteration " + str(iter + 1) + " - "
   acids = "Acids " + "{:,}".format(iter * max) + " through " + "{:,}".format(iter * max + max - 1) + "\n"

   tweet = ""
   tweet += title
   tweet += acids
   found = False
   for n in nucleic_acids.keys():
      if nucleic_acids[n]["count"]:
         tweet += n + ": " + "{:,}".format(nucleic_acids[n]["count"]) + "\n"
         found = True

   if found:
      print tweet, len(tweet)

      # Connect to Twitter
      api = twitter.Api(keys.consumer_key, keys.consumer_secret, keys.access_token, keys.access_token_secret)

      # Post tweet text and image
      status = api.PostMedia(tweet, pwd + 'chrom.png')

      # Increment and write the iteration number
      f = codecs.open(pwd + "iter", "w", "utf-8")
      f.write(str(iter + 1))
      f.close()

   else:
      print "Done!"

 
if __name__ == "__main__":
   sys.exit(main())
