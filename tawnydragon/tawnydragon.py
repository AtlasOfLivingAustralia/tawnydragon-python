import pandas as pd
from .common_dictionaries import base_url,term_files, rdf_types, columns_to_drop, columns_to_rename, column_names_merge
from .common_functions import check_recommended

def show_dwc_information(infotype=None,
                         columns=None,
                         recommended=False,
                         standard_type="Darwin Core",
                         version = None):
    """
    This function is a one-stop-shop for all of the Darwin Core standards, terms, and vocabulary
    information you need.

    Parameters
    ----------
        infotype: str
            Determines what info you are after.  Only takes the following arguments:
                - `standards`: A list of all possible Darwin Core Standards
                - `terms`: All possible Darwin Core terms you can use
                - `termlists`: something
                - `vocabularies`: something
        columns: list
            Something.  Defaults to
                - for `terms`: `["code","date","parent_class","label","description","examples","type","status","key"]`
                - all others: `["code","date","label","description","status","key"]`
        recommended: logical
            A flag that, when `True`, will only return recommended Darwin Core terms.  Defaults to `False`.
        standard_type: str
            You can choose what data standard you want.  Defaults now to Darwin Core.
        version: str
            Denotes which version of the standards you want.  Default is ``None``.

    Returns
    -------

    An object of type `pandas.DataFrame` that includes information about Darwin Core Terms.

    Examples
    --------

    Get a list of all standards

    .. prompt:: python

        >>> import tawnydragon
        >>> tawnydragon.show_dwc_information(infotype="standards")

    .. program-output:: python -c "import tawnydragon;import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);print(tawnydragon.show_dwc_information(infotype=\\\"standards\\\"))"

    Get only recommended Darwin Core Terms

    .. prompt:: python

        >>> import tawnydragon
        >>> tawnydragon.show_dwc_information(infotype="terms",recommended=True)

    .. program-output:: python -c "import tawnydragon;import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);print(tawnydragon.show_dwc_information(infotype=\\\"terms\\\",recommended=True))"

    """

    # check for infotype
    if infotype not in ["standards","termlists","vocabularies","terms"]:
        raise ValueError("The only keywords we accept are:\n\nstandards\ntermlists\nvocabularies\nterms\n")

    # check if infotype is terms, because terms has different columns than the others
    if infotype == "terms" and columns is None:
        columns = ["code","date","parent_class","label","description","examples","type","status","version"]
        
    # check for user-specified columns
    elif infotype != "terms" and columns is None:
        columns=["code","date","label","description","status","version"]

    # change how to filter data coming out
    if infotype == "terms":
        if "date" not in columns:
            filters=["code"]
            ascending=[True]
        elif "code" not in columns:
            filters=["date"]
            ascending=[False]
        else:
            filters=["date","code"]
            ascending=[False,True]
    else:
        filters=["date"]
        ascending=[False]

    # prepare to loop over all levels
    term_files_infotypes = list(term_files.keys())
    index_terms = term_files_infotypes.index(infotype)
    dwc_information = None

    # loop over all levels
    for i in range(0,index_terms+1,2):

        if i == 0:

            # get standards first, as no merging necessary
            dwc_information = pd.read_csv("{}{}".format(base_url,term_files[term_files_infotypes[i]]))

            # filter by standard_type if need be
            if standard_type is not None:
                # dwc_information.loc[dwc_information['label] == standard_type]
                dwc_information = dwc_information.loc[dwc_information['label'].astype(str).str.contains(standard_type, case=False, na=False)]

        else:
            
            # get new information to merge
            new_information = pd.read_csv("{}{}".format(base_url,term_files[term_files_infotypes[i]]))

            # get keys to connect previous and current information
            connecting_keys = pd.read_csv("{}{}".format(base_url,term_files[term_files_infotypes[i-1]]))

            # get column names of connecting keys
            connecting_columns = list(connecting_keys.columns)

            # merge previous information with first column name of connecting_keys
            temp = pd.merge(dwc_information, connecting_keys,left_on='version', 
                            right_on = connecting_columns[0]).reset_index(drop=True)
            
            # merge above temporary dataframe with the current information on the second column name
            # of connecting_keys
            dwc_information = pd.merge(temp, new_information,left_on=connecting_columns[1], 
                                       right_on='version').reset_index(drop=True)

            # check if user wants terms, and if so, and add parent_class and type 
            if i == 6:

                # get the parent class
                dwc_information['parent_class'] = dwc_information['tdwgutility_organizedInClass'].apply(lambda x: (x.replace("http://purl.org/dc/terms/","") if "purl" in x else x.replace("http://rs.tdwg.org/dwc/terms/","")) if type(x) is str else "No Parent Class")

                # get the type_vector
                dwc_information['type'] = dwc_information['rdf_type'].apply(lambda x: rdf_types[x])
                
            # drop previous, duplicate names
            dwc_information = dwc_information.drop(columns=columns_to_drop[term_files_infotypes[i]])

            # rename current columns to names without '_y' 
            dwc_information = dwc_information.rename(columns=columns_to_rename[term_files_infotypes[i]])

    # return your table
    return check_recommended(recommended=recommended,dataframe=dwc_information,
                                     tablename=infotype,columns=columns,filters=filters,
                                     ascending=ascending,version=version).drop_duplicates()