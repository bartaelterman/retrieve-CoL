import requests
from lxml import etree

class TaxonomyFetcher:
    def __init__(self):
	pass

    def parse_classification(self, full_response_xml_input):
	doc = etree.fromstring(full_response_xml_input)
	outdict = {}
	for result in doc.iterfind("result"):
	    classification = result.find("classification")
	    for taxon in classification.iterfind("taxon"):
		rank = taxon.find("rank").text
		name = taxon.find("name").text
		outdict[rank] = name
	return outdict

    def get_classification(self, taxon_name):
        names = {"name": taxon_name, "response": "full"}
        r = requests.get("http://www.catalogueoflife.org/col/webservice", params=names)
	return self.parse_classification(r.text.encode('utf-8'))
    
    def get_all_classifications(self, taxon_names_list):
        return [self.get_classification(x) for x in taxon_names_list]
