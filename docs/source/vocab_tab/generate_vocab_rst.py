import tawnydragon

terms = tawnydragon.show_dwc_information(infotype="terms")

vocab_file = open("index.rst",mode="w")
vocab_file.write("Vocabulary List\n")
vocab_file.write("===============\n\n")

parent_classes = sorted(list(set(terms['parent_class'])))

n=0
for parent in parent_classes:
    children = terms[terms["parent_class"] == parent]
    vocab_file.write(".. dropdown:: " + parent + "\n\n")
    for i,row in children.iterrows():
        vocab_file.write("    .. dropdown:: " + row['code'] + "\n\n")
        vocab_file.write("        *status: " + row['status'] + "*\n\n")
        vocab_file.write("        " + row['description'] + "\n\n")
    vocab_file.write("\n\n")

vocab_file.close()