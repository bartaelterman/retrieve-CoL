import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)) + "/src")
import fetch_taxonomy
from nose.tools import assert_equals

def test_fetch_taxonomy():
    taxonomy_fetcher = fetch_taxonomy.TaxonomyFetcher()
    input_names = [
        "Enchytraeus albidus",
        "Henlea perpusilla",
        "Henlea ventriculosa",
        "Lumbricillus lineatus",
        "Lumbriculus variegatus"
    ]
    expected_output = [
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Class": "Clitellata", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Genus": "Enchytraeus"},
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Class": "Clitellata", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Genus": "Henlea"},
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Class": "Clitellata", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Genus": "Henlea"},
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Class": "Clitellata", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Genus": "Lumbricillus"},
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Class": "Clitellata", "Order": "Lumbriculida", "Family": "Lumbriculidae", "Genus": "Lumbriculus"}
    ]
    assert_equals(taxonomy_fetcher.get_all_classifications(input_names), expected_output)
