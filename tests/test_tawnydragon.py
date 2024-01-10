import tawnydragon

### standards

def test_show_dwc_functions_standards():
    # check that standards is working
    standards = tawnydragon.show_dwc_information(infotype="standards")
    assert standards.shape[0] > 1
    assert standards.shape[1] > 1
    assert list(standards.columns) == ["code","date","label","description","status","key"]

def test_show_dwc_functions_standards_recommended():
    # check that the recommended option is working with standards
    standards = tawnydragon.show_dwc_information(infotype="standards")
    standards_rec = tawnydragon.show_dwc_information(infotype="standards",recommended=True)
    assert standards.shape[0] > standards_rec.shape[0]

def test_show_dwc_functions_standards_select_columns():
    # check that selecting columns works with the standards function
    standards = tawnydragon.show_dwc_information(infotype="standards")
    standards_selcol = tawnydragon.show_dwc_information(infotype="standards",columns=["date","label","description","status"])
    assert standards.shape[1] > standards_selcol.shape[1]
    assert list(standards_selcol.columns) == ["date","label","description","status"]

def test_show_dwc_functions_standards_select_columns_recommended():
    # check that selecting columns and only recommended items works
    standards = tawnydragon.show_dwc_information(infotype="standards")
    standards_selcol_rec = tawnydragon.show_dwc_information(infotype="standards",columns=["date","label","description","status"],recommended=True)
    assert standards.shape[0] > standards_selcol_rec.shape[0]
    assert list(standards_selcol_rec.columns) == ["date","label","description","status"]

### termlists

def test_show_dwc_functions_termlists():
    # check that termlists is working
    termlists = tawnydragon.show_dwc_information(infotype="termlists")
    assert termlists.shape[0] > 1
    assert termlists.shape[1] > 1
    assert list(termlists.columns) == ["code","date","label","description","status","key"]

def test_show_dwc_functions_termlists_recommended():
    # check that the recommended option is working with termlists
    termlists = tawnydragon.show_dwc_information(infotype="termlists")
    termlists_rec = tawnydragon.show_dwc_information(infotype="termlists",recommended=True)
    assert termlists.shape[0] > termlists_rec.shape[0]

def test_show_dwc_functions_termlists_select_columns():
    # check that selecting columns works with termlists
    termlists = tawnydragon.show_dwc_information(infotype="termlists")
    termlists_selcol = tawnydragon.show_dwc_information(infotype="termlists",columns=["date","label","description","status"])
    assert termlists.shape[1] > termlists_selcol.shape[1]
    assert list(termlists_selcol.columns) == ["date","label","description","status"]

def test_show_dwc_functions_termlists_select_columns_recommended():
    # check that selecting columns and only recommended items works with termlists
    termlists = tawnydragon.show_dwc_information(infotype="termlists")
    termlists_selcol_rec = tawnydragon.show_dwc_information(infotype="termlists",columns=["date","label","description","status"],recommended=True)
    assert termlists.shape[0] > termlists_selcol_rec.shape[0]
    assert list(termlists_selcol_rec.columns) == ["date","label","description","status"]

### vocabularies

def test_show_dwc_functions_vocabularies():
    # check that vocabularies is working
    vocabularies = tawnydragon.show_dwc_information(infotype="vocabularies")
    assert vocabularies.shape[0] > 1
    assert vocabularies.shape[1] > 1
    assert list(vocabularies.columns) == ["code","date","label","description","status","key"]

def test_show_dwc_functions_vocabularies_recommended():
    # check that the recommended option is working with vocabularies
    vocabularies = tawnydragon.show_dwc_information(infotype="vocabularies")
    vocabularies_rec = tawnydragon.show_dwc_information(infotype="vocabularies",recommended=True)
    assert vocabularies.shape[0] > vocabularies_rec.shape[0]

def test_show_dwc_functions_vocabularies_select_columns():
    # check that selecting columns works with termlists
    vocabularies = tawnydragon.show_dwc_information(infotype="vocabularies")
    vocabularies_selcol = tawnydragon.show_dwc_information(infotype="vocabularies",columns=["date","label","description","status"])
    assert vocabularies.shape[1] > vocabularies_selcol.shape[1]
    assert list(vocabularies_selcol.columns) == ["date","label","description","status"]

def test_show_dwc_functions_vocabularies_select_columns_recommended():
    # check that selecting columns and only recommended items works with termlists
    vocabularies = tawnydragon.show_dwc_information(infotype="vocabularies")
    vocabularies_selcol_rec = tawnydragon.show_dwc_information(infotype="vocabularies",columns=["date","label","description","status"],recommended=True)
    assert vocabularies.shape[0] > vocabularies_selcol_rec.shape[0]
    assert list(vocabularies_selcol_rec.columns) == ["date","label","description","status"]

### terms

def test_show_dwc_functions_terms():
    # check that termlists is working
    terms = tawnydragon.show_dwc_information(infotype="terms")
    assert terms.shape[0] > 1
    assert terms.shape[1] > 1
    assert list(terms.columns) == ["code","date","parent_class","label","description","examples","type","status","key"]

def test_show_dwc_functions_terms_recommended():
    # check that the recommended option is working with termlists
    terms = tawnydragon.show_dwc_information(infotype="terms")
    terms_rec = tawnydragon.show_dwc_information(infotype="terms",recommended=True)
    assert terms.shape[0] > terms_rec.shape[0]

def test_show_dwc_functions_terms_select_columns():
    # check that selecting columns works with termlists
    terms = tawnydragon.show_dwc_information(infotype="terms")
    terms_selcol = tawnydragon.show_dwc_information(infotype="terms",columns=["date","label","description","status"])
    assert terms.shape[1] > terms_selcol.shape[1]
    assert list(terms_selcol.columns) == ["date","label","description","status"]

def test_show_dwc_functions_terms_select_columns_recommended():
    # check that selecting columns and only recommended items works with termlists
    terms = tawnydragon.show_dwc_information(infotype="terms")
    terms_selcol_rec = tawnydragon.show_dwc_information(infotype="terms",columns=["date","label","description","status"],recommended=True)
    assert terms.shape[0] > terms_selcol_rec.shape[0]
    assert list(terms_selcol_rec.columns) == ["date","label","description","status"]