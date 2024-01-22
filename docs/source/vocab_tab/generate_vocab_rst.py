import tawnydragon

### TODO: Check that all these are currently DwC compliant terms

# required terms
required_terms = {
    "Darwin Core": {
        "No parent class": ["basisOfRecord","eventDate"],
        "Spatial Information": ["decimalLatitude","decimalLongitude","geodeticDatum","coordinateUncertaintyInMeters"],
        "Unique Identifiers": ["occurrenceID","catalogNumber","recordNumber"],
        "Taxonomic Information": ["scientificName","taxonRank","kingdom","phylum","class","order","family","genus"]
    }
}

# recommended terms
recommended_terms = {
    "Darwin Core":  {
        "No parent class": ["dataGeneralizations","informationWithheld"],
        "Spatial Information": ["coordinatePrecision","country","locality","stateProvince"],
        "Further Identification": ["identificationQualifier","identificationReferences",
                                   "identificationVerificationStatus","identifiedBy","identifiedByID"],
        "Further Occurrence Information": ["individualCount","occurrenceStatus","recordedBy"],
        "Event Information": ["eventID","samplingProtocol"]
    }   
}

# create a list of required and recommended terms
required_recommended_terms = sum([
    required_terms["Darwin Core"][key] for key in required_terms["Darwin Core"]
    ] + [
    recommended_terms["Darwin Core"][key] for key in recommended_terms["Darwin Core"]
    ],
    []
)

# start writing the vocab file
vocab_file = open("index.rst",mode="w")
vocab_file.write("Vocabulary List\n")
vocab_file.write("===========================\n\n")
vocab_file.write("\n")

# make sure we have all the standards
standard_types_short = ["Darwin Core", "Audiovisual Core", "SDS", "VMS", "GUID", "TAPIR"]
### TODO: remove standard_type = None in future when other standards are fixed
standards = tawnydragon.show_dwc_information(infotype="standards",recommended=True,standard_type=None)
standard_types = list(standards['label'])

# loop over all the standards
for i,standard in enumerate(standard_types_short):
    
    # get all terms
    terms = tawnydragon.show_dwc_information(infotype="terms",recommended=True)
    
    # start a menu for the standards terms
    if i >= 1:

        # start a menu for the standards terms
        vocab_file.write(".. dropdown:: " + standard_types[i] + "\n\n")
        vocab_file.write("    Coming soon!\n\n")
        continue

    else:
    
        vocab_file.write(".. dropdown:: " + standard_types[i] + "\n\n")

    # get a list of all possible versions
    versions = list(reversed(sorted(set(list(terms['date'])))))

    # iterate over available versions
    for j,version in enumerate(versions):

        # ensure "recommended" version is available for the users
        if j == 0:

            # get terms
            terms = tawnydragon.show_dwc_information(infotype="terms",standard_type=standard,recommended=True)
            
            # start writing files for the current version
            vocab_file.write("    ``Current Version:``\t\t" + version + "\n\n")
            vocab_file.write("    *Required:*\n\n")

            # loop over required terms
            for key in required_terms[standard]:
                if key != "No parent class":
                    vocab_file.write("    * .. dropdown:: " + key + "\n\n")
                if key == "Unique Identifiers":
                    vocab_file.write("         *NOTE: CHOOSE ONLY ONE*\n\n")
                for item in required_terms[standard][key]:
                    item_info = terms.loc[terms['code'].astype(str).str.contains(item,case=True, na=False)]
                    index = item_info.index[0]
                    if key == "No parent class":
                        vocab_file.write("    * .. dropdown:: ``" + item + "``\n\n")
                        vocab_file.write("        " + item_info['description'][index] + "\n\n")
                        vocab_file.write("        examples: " + item_info['examples'][index] + "\n\n") 
                    else:   
                        vocab_file.write("        * .. dropdown:: ``" + item + "``\n\n")
                        vocab_file.write("            " + item_info['description'][index] + "\n\n")
                        vocab_file.write("            examples: " + item_info['examples'][index] + "\n\n") 
            vocab_file.write("    *Recommended:*\n\n")
            for key in recommended_terms[standard]:
                if key != "No parent class":
                    vocab_file.write("    * .. dropdown:: " + key + "\n\n")
                if key == "Unique Identifiers":
                    vocab_file.write("         *NOTE: CHOOSE ONLY ONE*\n\n")
                for item in recommended_terms[standard][key]:
                    item_info = terms.loc[terms['code'].astype(str).str.contains(item,case=True, na=False)]
                    index = item_info.index[0]
                    if key == "No parent class":
                        vocab_file.write("    * .. dropdown:: ``" + item + "``\n\n")
                        vocab_file.write("        " + item_info['description'][index] + "\n\n")
                        vocab_file.write("        examples: " + item_info['examples'][index] + "\n\n") 
                    else:   
                        vocab_file.write("        * .. dropdown:: ``" + item + "``\n\n")
                        vocab_file.write("            " + item_info['description'][index] + "\n\n")
                        vocab_file.write("            examples: " + item_info['examples'][index] + "\n\n") 
            vocab_file.write("    *Rest:*\n\n")
            rest_terms = terms.loc[~terms['code'].isin(required_recommended_terms)]
            parent_classes = sorted(list(set(list(terms['parent_class']))))
            for parent in parent_classes:
                vocab_file.write("    * .. dropdown:: " + parent + "\n\n")
                children = terms[terms['parent_class'] == parent]
                for k,row in children.iterrows():
                    vocab_file.write("        .. dropdown:: " + row['code'] + "\n\n")
                    vocab_file.write("            " + row['description'] + "\n\n")
                vocab_file.write("\n\n")

        # separate superseded from main
        elif j == 1:
            vocab_file.write("    .. dropdown:: *Superseded Versions:*\n\n")
            
        # write superseded versions here
        if j >=1 and j != 0:
            terms = tawnydragon.show_dwc_information(infotype="terms",standard_type=standard,version=version)
            vocab_file.write("        .. dropdown:: " + version + "\n\n")
            terms = terms[terms['status'] == 'superseded']
            parent_classes = sorted(list(set(list(terms['parent_class']))))
            for parent in parent_classes:
                vocab_file.write("            .. dropdown:: " + parent + "\n\n")
                children = terms[terms['parent_class'] == parent]
                for k,row in children.iterrows():
                    vocab_file.write("                .. dropdown:: " + row['code'] + "\n\n")
                    vocab_file.write("                        " + row['description'] + "\n\n")
                vocab_file.write("\n\n")    

vocab_file.close()