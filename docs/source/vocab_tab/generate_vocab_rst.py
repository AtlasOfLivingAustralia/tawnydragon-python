import tawnydragon

### TODO: Check that all these are currently DwC compliant terms

# required terms
required_terms = {
    "Darwin Core": ["basisOfRecord","eventDate","scientificName","decimalLatitude","decimalLongitude",
                    "geodeticDatum","coordinateUncertaintyInMeters","occurrenceID","catalogNumber",
                    "recordNumber","taxonRank","kingdom","phylum","class","order","family","genus"]
}
# recommended terms
recommended_terms = {
    "Darwin Core": ["stateProvince","country","locality","coordinatePrecision","dataGeneralizations",
                    "identifiedBy","identifiedById","identificationVerificationStatus",
                    "identificationReferences","identificationQualifier", "informationWithheld",
                    "eventId","recordedBy","samplingProtocol","occurrenceStatus","individualCount"]
}

vocab_file = open("index.rst",mode="w")
vocab_file.write("Vocabulary List\n")
vocab_file.write("===========================\n\n")

vocab_file.write("\n")

standard_types_short = ["Darwin Core", "Audiovisual Core", "SDS", "VMS", "GUID", "TAPIR"]
### TODO: remove standard_type = None in future when other standards are fixed
standards = tawnydragon.show_dwc_information(infotype="standards",recommended=True,standard_type=None)
standard_types = list(standards['label'])

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
            terms = tawnydragon.show_dwc_information(infotype="terms",standard_type=standard,recommended=True)
            vocab_file.write("    ``Current Version:``\t\t" + version + "\n\n")
            vocab_file.write("    .. dropdown:: *Required:*\n\n")
            for i,row in terms.loc[terms['code'].isin(required_terms[standard])].iterrows():
                vocab_file.write("            .. dropdown:: " + row['code'] + "\n\n")
                vocab_file.write("                " + row['description'] + "\n\n")
                vocab_file.write("                examples: " + row['examples'] + "\n\n")
                vocab_file.write("\n\n")
            vocab_file.write("    .. dropdown:: *Recommended:*\n\n")
            for i,row in terms.loc[terms['code'].isin(recommended_terms[standard])].iterrows():
                vocab_file.write("            .. dropdown:: " + row['code'] + "\n\n")
                vocab_file.write("                " + row['description'] + "\n\n")
                vocab_file.write("                examples: " + row['examples'] + "\n\n")
            vocab_file.write("    .. dropdown:: *Rest:*\n\n")
            rest_terms = terms.loc[~terms['code'].isin(required_terms[standard] + recommended_terms[standard])]
            parent_classes = sorted(list(set(list(terms['parent_class']))))
            for parent in parent_classes:
                vocab_file.write("        .. dropdown:: " + parent + "\n\n")
                children = terms[terms['parent_class'] == parent]
                for k,row in children.iterrows():
                    vocab_file.write("            .. dropdown:: " + row['code'] + "\n\n")
                    vocab_file.write("                " + row['description'] + "\n\n")
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