import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)) + "/src")
import fetch_taxonomy
from nose.tools import assert_equals

def test_fetch_taxonomy():
    taxonomy_fetcher = fetch_taxonomy.TaxonomyFetcher()
    input_names = [
        "Aelosoma travancorense",
        "Cognettia sp.",
        "Enchytraeus albidus",
        "Henlea perpusilla",
        "Henlea ventriculosa",
        "Lumbricillus lineatus",
        "Lumbriculus variegatus"
    ]
    expected_output = [
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Subphylum": "", "Class": "Aphanoneura", "Subclass": "", "Order": "Naidomorpha", "Family": "Aeolosomatidae", "Subfamily": "", "Genus": "Aeolosoma", "Species": "Aelosoma travancorense"},
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Subphylum": "", "Class": "Clitellata", "Subclass": "Oligochaeta", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Subfamily": "", "Genus": "Cognettia", "Species": "Cognettia sp."},
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Subphylum": "", "Class": "Clitellata", "Subclass": "Oligochaeta", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Subfamily": "", "Genus": "Enchytraeus", "Species": "Enchytraeus albidus"},
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Subphylum": "", "Class": "Clitellata", "Subclass": "Oligochaeta", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Subfamily": "", "Genus": "Henlea", "Species": "Henlea perpusilla"},
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Subphylum": "", "Class": "Clitellata", "Subclass": "Oligochaeta", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Subfamily": "", "Genus": "Henlea", "Species": "Henlea ventriculosa"},
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Subphylum": "", "Class": "Clitellata", "Subclass": "Oligochaeta", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Subfamily": "", "Genus": "Lumbricillus", "Species": "Lumbricillus lineatus"},
        {"Kingdom": "Animalia", "Phylum": "Annelida", "Subphylum": "", "Class": "Clitellata", "Subclass": "Oligochaeta", "Order": "Enchytraeida", "Family": "Enchytraeidae", "Subfamily": "", "Genus": "Lumbricillus", "Species": "Lumbricillus variegatus"}
    ]
    assert_equals(taxonomy_fetcher.get_all_classifications(input_names), expected_output)
