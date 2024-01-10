import pandas as pd
from .common_dictionaries import base_url,term_files, rdf_types
from .common_functions import tidy_columns

def show_dwc_information(infotype=None,
                         columns=None,
                         recommended=False):
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

    Returns
    -------

    An object of type `pandas.DataFrame` that includes information about Darwin Core Terms.

    Examples
    --------

    Get a list of all standards

    .. prompt:: python

        >>> import tawnydragon
        >>> tawnydragon.show_dwc_information(infotype="standards")

    .. program-output:: python -c "import tawnydragon;print(tawnydragon.show_dwc_information(infotype=\\\"standards\\\"))"

    Get only recommended Darwin Core Terms

    .. prompt:: python

        >>> import tawnydragon
        >>> tawnydragon.show_dwc_information(infotype="terms",recommended=True)

    .. program-output:: python -c "import tawnydragon;print(tawnydragon.show_dwc_information(infotype=\\\"terms\\\",recommended=True))"

    """

    # check for infotype
    if infotype not in ["standards","termlists","vocabularies","terms"]:
        raise ValueError("The only keywords we accept are:\n\nstandards\ntermlists\nvocabularies\nterms\n")

    if infotype == "terms" and columns is None:
        columns = ["code","date","parent_class","label","description","examples","type","status","key"]
        
    # check for user-specified columns
    elif infotype != "terms" and columns is None:
        columns=["code","date","label","description","status","key"]

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

    # get standards from TDWG Git repo
    dwc_information = pd.read_csv("{}{}".format(base_url,term_files[infotype]))

    # check for special terms case
    if infotype == "terms":

        # get the parent class
        dwc_information['parent_class'] = dwc_information['tdwgutility_organizedInClass'].apply(lambda x: (x.replace("http://purl.org/dc/terms/","") if "purl" in x else x.replace("http://rs.tdwg.org/dwc/terms/","")) if type(x) is str else "No Parent Class")

        # get the type_vector
        dwc_information['type'] = dwc_information['rdf_type'].apply(lambda x: rdf_types[x])
    
        # check if they only want recommended terms
        if recommended:
            new_dwc_information = tidy_columns(
                dataframe=dwc_information,
                tablename=infotype
                )[columns].sort_values(filters,ascending=ascending).reset_index(drop=True)
            return new_dwc_information[new_dwc_information["status"] == "recommended"].reset_index(drop=True)
        
        # return the terms correctly ordered
        return tidy_columns(
            dataframe=dwc_information,
            tablename=infotype
        )[columns].sort_values(filters,ascending=ascending).reset_index(drop=True)

    if recommended:
        new_dwc_information = tidy_columns(
            dataframe=dwc_information,
            tablename=infotype
            )[columns].sort_values(filters,ascending=ascending).reset_index(drop=True)
        return new_dwc_information[new_dwc_information["status"] == "recommended"].reset_index(drop=True)
    
    # get columns with all relevant data
    return tidy_columns(
        dataframe=dwc_information,
        tablename=infotype
    )[columns].sort_values("date",ascending=False).reset_index(drop=True)