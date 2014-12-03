# Nucleotide Sequences

*Script(s)/bots that do something with the [Human Genome Project's](http://www.genome.gov/) nucleotide sequences*

I've downloaded *Genome Reference Consortium Human Build 38 patch release 1* from the [National Center for 
Biotechnical Information](http://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.27/) (thanks 
[@vogon](https://twitter.com/vogon) for pointing me to this!). I was using the one from [Project 
Gutenberg](https://www.gutenberg.org/), but that was only build 34. This is in the [FASTA 
format](http://en.wikipedia.org/wiki/FASTA_format).

~~I know very little about [DNA](http://en.wikipedia.org/wiki/DNA) and the [Human Genome 
Project's](http://www.genome.gov/), but since [Project Gutenberg](https://www.gutenberg.org/) has [nucleotide 
sequences from the Genome Project](http://www.gutenberg.org/ebooks/subject/15882) I thought I'd try to come up with 
interesting ways to look at them.~~

~~As best I can tell, they're in the [FASTA format](http://en.wikipedia.org/wiki/FASTA_format). I've taken a file 
(started with [Chromosome 1](http://www.gutenberg.org/ebooks/11775)) and stripped the top Project Gutenberg text out 
of it as well as the first identification line so that I'm left with only the nucleic acids. There are large 
sections that have only the letter N which seems (according to the FASTA format) be unknown nucleic acids. The other 
characters map to [Adenine](http://en.wikipedia.org/wiki/Adenine), 
[Cytosine](http://en.wikipedia.org/wiki/Cytosine), (Guanine)[http://en.wikipedia.org/wiki/Guanine], and 
(Thymine)[http://en.wikipedia.org/wiki/Thymine].~~

~~All of the sequences can be downloaded from [Project Gutenberg](http://www.gutenberg.org/ebooks/subject/15882) so 
I'm excluding them from this repository since they're rather large.~~

## Twitter Image Bot 

The first thing I've tried to do is to build an [Twitter bot](https://twitter.com/) that tweets images of portions 
of the DNA sequence. It takes 28,419 acids at a time and builds an image that is 840x840. Each acid it finds, maps to 
a color 5x5 square. This bot will tweet a section every hour. At that rate it will take about a year to finish all 
248,564,422 acids (8,760 images).

This is the [image.py](image.py) script.

