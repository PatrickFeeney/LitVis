import atlas
import epidoc


# TODO test with 057-059
# dateline text from parsing EpiDocXML
epidoc_fname = "submodules/canonical-latinLit/data/phi0474/phi056/phi0474.phi056.perseus-lat1.xml"
geodetic_fname = "data/input/loc_to_geodetic.csv"
topo_fname = "data/input/loc_to_topo_id.csv"
parser = epidoc.EpiDocXMLParser(epidoc_fname, geodetic_fname, topo_fname)
parser.save_dataframe()

extractor = atlas.NamedEntityCollectionExtractor()
extractor.extract()
