from .common_dictionaries import table_names, date_names, url_to_remove

def tidy_columns(dataframe=None,
                 tablename=None):

    # first, check for data frame
    if dataframe is None:
        raise ValueError("Please pass a dataframe to this function")
    
    # second, check for the table name
    if tablename is None:
        raise ValueError("Please provide a table name so the term in the table is correct")
    
    # add column denoting the code that goes with the version of DwC terms
    if tablename == "standards":
        dataframe['code'] = dataframe['version'].apply(lambda x: x.replace(url_to_remove[tablename],"").split("/")[0])
    elif tablename == "vocabularies":
        dataframe['code'] = dataframe['version'].apply(lambda x: x.replace(url_to_remove[tablename],"").split("/")[1])
    elif tablename == "termlists":
        dataframe['code'] = dataframe['version'].apply(lambda x: "/".join([x.replace(url_to_remove[tablename], "").split("/")[0],x.strip(url_to_remove[tablename]).split("/")[2]]))
    else:
        dataframe = dataframe.rename(
            columns={
                "term_localName": "code",
                "rdfs_comment": "description"
            }
        )

    # rename columns
    return dataframe.rename(
        columns={
            date_names[tablename]: "date",
            table_names[tablename]: "status",
            "version": "key"
        }
    )