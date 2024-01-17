from .common_dictionaries import table_names, date_names, url_to_remove, base_url, term_files
import pandas as pd

def tidy_columns(dataframe=None,
                 tablename=None,
                 version=None):

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
        dataframe['code'] = dataframe['version'].apply(lambda x: x.replace(url_to_remove[tablename],"").split("/")[0])
    elif tablename == "termlists":
        dataframe['code'] = dataframe['version'].apply(lambda x: "/".join([x.replace(url_to_remove[tablename], "").split("/")[0],x.strip(url_to_remove[tablename]).split("/")[2]]))
    else:
        dataframe = dataframe.rename(
            columns={
                "term_localName": "code",
                "rdfs_comment": "description"
            }
        )
        return dataframe.rename(
        columns={
            date_names[tablename]: "date",
        }
    )

    # rename columns
    if version is not None:
        dataframe = dataframe.rename(
            columns={
                date_names[tablename]: "date",
                table_names[tablename]: "status",
            }
        )
        return dataframe[dataframe['date'] == version]
    
    # otherwise, return dataframe as is
    return dataframe.rename(
        columns={
            date_names[tablename]: "date",
            table_names[tablename]: "status",
        }
    )

def check_recommended(recommended=False,
                      dataframe=None,
                      tablename=None,
                      columns=None,
                      filters=None,
                      ascending=None,
                      version=None):

        # return only recommended terms ordered correctly
        if recommended:
            new_dwc_information = tidy_columns(
                    dataframe=dataframe,
                    tablename=tablename,
                    version=version
                    )[columns].sort_values(filters,ascending=ascending).reset_index(drop=True)
            return new_dwc_information[new_dwc_information["status"] == "recommended"].reset_index(drop=True)
        
        # return the terms correctly ordered
        return tidy_columns(
            dataframe=dataframe,
            tablename=tablename,
            version=version
        )[columns].sort_values(filters,ascending=ascending).reset_index(drop=True)