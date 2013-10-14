#!/usr/bin/python
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)) + "/src")
import fetch_taxonomy

if len(sys.argv) != 2:
    print "usage: ./fetch_taxonomy_from_file.py <inputfile>"
    print "   This inputfile should be a text file, containing taxon names. One name per line."
    sys.exit(-1)

infile = sys.argv[1]
tf = fetch_taxonomy.TaxonomyFetcher()
taxon_names = file(infile).read().strip().split("\n")
all_classification = tf.get_all_classifications(taxon_names)
print "\t".join(["kingdom", "phylum", "class", "order", "family", "genus", "query_taxon"])
for i in range(len(taxon_names)):
    taxon = taxon_names[i]
    classification = all_classification[i]
    try:
        kingdom = classification["Kingdom"]
    except:
	kingdom = ""
    try:
        phylum = classification["Phylum"]
    except:
	phylum = ""
    try:
        clazz = classification["Class"]
    except:
	clazz = ""
    try:
        order = classification["Order"]
    except:
	order = ""
    try:
        family = classification["Family"]
    except:
	family = ""
    try:
        genus = classification["Genus"]
    except:
	genus = ""
    print "\t".join([kingdom, phylum, clazz, order, family, genus, taxon])
