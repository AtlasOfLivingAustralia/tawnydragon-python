import tawnydragon

# 

vocab_file = open("index.rst",mode="w")
vocab_file.write("Vocabulary List\n")
vocab_file.write("===========================\n\n")

vocab_file.write("\n")

standard_types_short = ["Darwin Core"] #, "Audiovisual Core", "SDS", "VMS", "GUID", "TAPIR"]
standards = tawnydragon.show_dwc_information(infotype="standards",recommended=True)
standard_types = list(standards['label'])

for i,standard in enumerate(standard_types_short):
    
    # get all terms
    terms = tawnydragon.show_dwc_information(infotype="terms",recommended=True)
    
    # start a menu for the standards terms
    vocab_file.write(".. dropdown:: " + standard_types[i] + "\n\n")

    # get a list of all possible versions
    versions = list(reversed(sorted(set(list(terms['date'])))))

    # iterate over available versions
    for j,version in enumerate(versions):

        # ensure "recommended" version is available for the users
        if j == 0:
            terms = tawnydragon.show_dwc_information(infotype="terms",standard_type=standard,recommended=True)
            vocab_file.write("    .. dropdown:: **Current Version:**    {}\n\n".format(version))
            parent_classes = sorted(list(set(list(terms['parent_class']))))
            for parent in parent_classes:
                vocab_file.write("        .. dropdown:: " + parent + "\n\n")
                children = terms[terms['parent_class'] == parent]
                for k,row in children.iterrows():
                    vocab_file.write("            .. dropdown:: " + row['code'] + "\n\n")
                    # vocab_file.write("                *status: " + row['status'] + "*\n\n")
                    vocab_file.write("                " + row['description'] + "\n\n")
                vocab_file.write("\n\n")

        # separate superseded from main
        elif j == 1:
            vocab_file.write("    .. dropdown:: **Superseded Versions:**\n\n")
            
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