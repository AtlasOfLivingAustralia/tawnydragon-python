base_url = "https://raw.githubusercontent.com/tdwg/rs.tdwg.org/master/"

term_files = {
    # level 1: standards
    "standards": "standards-versions/standards-versions.csv",
    "standards_vocabularies_keys": "standards-versions/standards-versions-parts.csv",
    # level 2: documents and vocabularies 
    "vocabularies": "vocabularies-versions/vocabularies-versions.csv",
    "vocabularies_termlists_keys": "vocabularies-versions/vocabularies-versions-members.csv",
    # "documents": "docs-versions/docs-versions.csv", # unimplemented yet
    # level 3: term lists
    "termlists": "term-lists-versions/term-lists-versions.csv",
    "termlists_terms_keys": "term-lists-versions/term-lists-versions-members.csv",
    # level 4: terms
    "terms": "terms-versions/terms-versions.csv" 
}

# audiovisual has acorient and acpart
audiovisual = {
    # maybe to link it to other things
    "acorient-versions": "acorient-versions/acorient-versions.csv",
    ### DEFINITELY
    "acorient": "acorient/acorient.csv",
    # Maybe
    "acpart-versions": "acpart-versions/acpart-versions.csv",
    ### DEFINITELY
    "acpart": "acpart/acpart.csv",
}

# SDS

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

column_names_merge = {
    "vocabularies": ['version','version']
}

columns_to_drop = {
    "standards": ['label_x','description_x','version_issued_x','document_modified_x','version_x'],
    "vocabularies": ['label_x','description_x','version_issued_x','document_modified_x','version_x'],
    "termlists": ['label_x','description_x','document_modified_x','version_x'], #version_issued_x
    "terms": ['label_x','description','version_issued_x','document_modified_x','version_x','dcterms_description'] 
}

columns_to_rename = {
    "standards": {'label_y': 'label',
                  'description_y': 'description',
                  'version_issued_y': 'version_issued', 
                  'document_modified_y': 'document_modified',
                  'version_y': 'version'},
    "vocabularies": {'label_y': 'label',
                     'description_y': 'description',
                     'version_issued_y': 'version_issued', 
                     'document_modified_y': 'document_modified',
                  'version_y': 'version'},
    "termlists": {'label_y': 'label',
                  'description_y': 'description', 
                  'document_modified_y': 'document_modified',
                  'version_y': 'version'},
    "terms": {'label_y': 'label', 
              'document_modified_y': 'document_modified',
              'version_y': 'version',
              'version_issued_y': 'version_issued'}
}