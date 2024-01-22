Explaining Recommended Darwin Core Terms In the Context of Data
================================================================

This is an extension to Required Terms, and is meant as a companion to that.

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

How is an occurrence recorded? (``basisOfRecord``)
---------------------------------------------------

When is an occurrence recorded? (``eventDate``)
---------------------------------------------------

Where is an occurrence recorded? (Spatial Information)
-------------------------------------------------------

What species was recorded? (Taxonomic Information)
-------------------------------------------------------

How Can I Make Every Observation Unique? (Unique Identifiers)
----------------------------------------------------------------