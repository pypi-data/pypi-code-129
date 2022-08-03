__author__    = "$Author: wfv20 $"
___revision__ = "$Revision: 1.1 $"
___date__     = "$Date: 2003-07-01 12:56:12 $"

"""
Goal of these routines are to provide a Python interface to writting, reading,
analyzing, and modifying NMR-STAR files and objects.

NOTES:
* Not supported STAR features:
    - Nested loops
    - Global block
* Limitations to content:
    - STAR file should have one and only one data_ tag and that should
        be the first thing in the file
* Limitations to the lay out (for fast parsing) these can all be
    taken care of by first running the STAR file through formatNMRSTAR
    - Save frames should start and end with save_ at the beginning of
        the line
    - Perhaps some unknown;-(

SPEED ISSUES:
* There's a good Python API written by Jens Linge and Lutz Ehrlig (EMBL).
    It can handle much more STAR features and variations to content
    and lay out. The current API was written to handle NMR-STAR files in
    the order of several Mb for which the EMBL API demanded a lot of
    resources. Parsing a 1 Mb STAR file with a huge table of mostly numeric
    values required a peak 50 Mb in memory and about 2 hours with StarFormat.
    My guess was that this could be much faster if at least the lowest level
    of the dataNode value (where it is a string or number) would use native
    Python objects in stead.
    Another issue is that a large text object when parsed by the
    EMBL API got copied over and over resulting in loss of speed and a
    significant increase in memory use.
* This API uses native Python objects for a list of tags (looped or free)
    with user defined objects above that where speed and memory are less of an
    issue. It parses a 10 Mb STAR file in 25 seconds with a peak memory
    usage of 55 Mb. The average value in the file is 3 chars long. A Python
    string object has a reference count (4), type pointer (4), malloc overhead
    (4), trailing \0 (1) and the content (rounded up to multiples of 4).
    Ignoring the content rounding we go from 3 bytes to 20 bytes (factor 7)
    in total for the average string in the example file. Considering some
    overhead for the objects on top of the string objects the 55 Mb doesn't
    look that bad.
* Compare this with the C STARLIB2 from Steve Mading (BMRB) which takes 12
    cpu seconds and 18 Mb peak memory usage. For STARLIBJ (java) Steve
    got 40 Mb peak memory usage and 57 seconds. Memory usage is slightly
    better but speed is a factor 2 slower. This was using the best Java
    engine we had. Another one we tested was a factor 3 slower.
* Summary:

Test on Linux using a dual CPU 700 MHz Pentium III (urchin.bmrb.wisc.edu)
Language STAR file size (Mb) Time (s)  RAM (Mb) Notes
###############################################################################
C        10                  12        18       Using Steve's STARlib2.
Java     10                  57        40       Tested by Steve 
Python   10                  25        55       Written at BMRB
Python*  1*                  7200*     50*      Written at EMBL
###############################################################################
Labeled with asterisk because the size of test file had to be truncated.
The API was developed for small files (< 100 kb).

Test on Windows using a single CPU 500 MHz Pentium III (sepia2.bmrb.wisc.edu)
In this case not only cpu seconds were counted but also I/O etc.
Language STAR file size (Mb) Time (s)  RAM (Mb) Notes
###############################################################################
C        10                  -         -        No compiled version available
Java     10                  74        31       Tested by Jurgen using Sun's Java 1.3.1
Python   10                  45        59       Written at BMRB
###############################################################################


* References:
S. R. Hall and A. P. F. Cook. STAR dictionary definition language: initial specification.
    J.Chem.Inf.Comput.Sci. 35:819-825, 1995.
S. R. Hall and N. Spadacinni. The STAR file: detailed specifications.
    J.Chem.Inf.Comput.Sci. 34:505-508, 1994.
J. P. Linge, M. Nilges, and Ehrlich L. StarDOM: from STAR format to XML.
    J Biomol NMR, 1999.
N. Spadacinni and C. B. Hall. Star_base: accessing STAR file data.
    J.Chem.Inf.Comput.Sci. 34:509-516, 1994.
J. Westbrook and P. E. Bourne. STAR/mmCIF: An ontologoy for macromolecular structure.
    Bioinformatics. 16 (2):159-168, 2000.
"""

## Public attributes
verbosity               = 2
