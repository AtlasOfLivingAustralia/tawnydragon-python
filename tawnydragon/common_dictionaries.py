base_url = "https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/"

term_files = {
    # level 1: standards
    "standards": "standards-versions/standards-versions.csv",
    "standards_vocabularies_keys": "standards-versions/standards-versions-parts.csv",
    # level 2: documents and vocabularies 
    "vocabularies": "vocabularies-versions/vocabularies-versions.csv",
    "vocabularies_termlists_keys": "vocabularies-versions/vocabularies-versions-members.csv",
    "documents": "docs-versions/docs-versions.csv", # unimplemented yet
    # level 3: term lists
    "termlists": "term-lists-versions/term-lists-versions.csv",
    "termlists_terms_keys": "term-lists-versions/term-lists-versions-members.csv",
    # level 4: terms
    "terms": "terms-versions/terms-versions.csv" 
}

table_names = {
    "standards": "standard_status",
    "vocabularies": "vocabulary_status",
    "termlists": "status",
    "terms": "version_status"
}

date_names = {
    "standards": "version_issued",
    "vocabularies": "version_issued",
    "termlists": "version_modified",
    "terms": "version_issued"
}

url_to_remove = {
    "standards": "http://www.tdwg.org/standards/",
    "vocabularies": "http://rs.tdwg.org/version/",
    "termlists": "http://rs.tdwg.org/",
    "terms": "http://rs.tdwg.org/dwc/terms/version/"
}

rdf_types = {
    "http://www.w3.org/1999/02/22-rdf-syntax-ns#Property": "term",
    "http://www.w3.org/2000/01/rdf-schema#Class": "class",
    "http://purl.org/dc/dcam/VocabularyEncodingScheme": "vocabulary_scheme"
}