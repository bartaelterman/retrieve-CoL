import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)) + "/src")
import fetch_taxonomy
from nose import with_setup
from nose.tools import assert_equals

class TestTaxonomyFetcher():
    def setup(self):
	self.tf = fetch_taxonomy.TaxonomyFetcher()

    def teardown(self):
	pass

    @with_setup(setup, teardown)
    def test_parse_classification_from_full_response_xml(self):
	xml_input = file("test/test_full_response_xml_result.xml").read()
	expected_classification = {"Kingdom": "Animalia", "Phylum": "Annelida", "Class": "Clitellata", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Genus": "Lumbricillus"}
	results = self.tf.parse_classification(xml_input)
	assert_equals(results, expected_classification)

    @with_setup(setup, teardown)
    def test_get_classification(self):
        taxon_name = "Lumbricillus lineatus"
	expected_classification = {"Kingdom": "Animalia", "Phylum": "Annelida", "Class": "Clitellata", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Genus": "Lumbricillus"}
	assert_equals(self.tf.get_classification(taxon_name), expected_classification)
