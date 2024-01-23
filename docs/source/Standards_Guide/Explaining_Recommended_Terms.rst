Explaining Recommended Darwin Core Terms In the Context of Data
================================================================

This is an extension/companion to the `Required Terms <Required_Terms.html>`.

recommended_terms = {
    "Darwin Core":  {
        "No parent class": ["dataGeneralizations","informationWithheld"],
        "Further Identification": ["identificationQualifier","identificationReferences",
                                   "identificationVerificationStatus","identifiedBy","identifiedByID"],
        "Further Occurrence Information": ["individualCount","occurrenceStatus","recordedBy"],
        "Event Information": ["eventID","samplingProtocol"]
    }   
}

Can I geographically obscure my data? (``dataGeneralizations``)
---------------------------------------------------------------

The short answer is yes.  We won't show you how to obscure your GPS coordinates here, but know that when 
you do, you should add a note in your data titled ``dataGeneralizations`` to explain how you obscured 
your data.  An example is from the TDWG explanation of ``dataGeneralizations``: *Coordinates generalized 
from original GPS coordinates to the nearest half degree grid cell.*  This is particularly useful for 
those working with endangered, threatened, sensitive or culturally significant species.


Can I anonymize information about this occurrence? (``informationWithheld``)
-----------------------------------------------------------------------------

In short, yes, and you can specify which information was withheld and why in the ``informationWithheld`` 
section.  The example from the TDWG website for ``informationWithheld`` is: *location information not given 
for endangered species; collector identities withheld | ask about tissue samples*.  As with the above term, 
this is particularly useful for those working with endangered, threatened, sensitive or culturally significant 
species, to protect not only the species, but the individuals making the observations as well.


Can I add more spatial information?
-------------------------------------------------------

Yes.  If you want to add your precision as a decimal, rather than a whole number for ``coordinateUncertaintyInMeters``,
you can add it as ``coordinatePrecision``.  This is a decimal representing the error of the instrument you were using to 
record in degrees.

If you want to add more contextual information about the area of observation, you can add ``country``,``locality``, and 
``stateProvince`` to your data, rather than just the latitude and longitude.


Can I add further identification information?
----------------------------------------------------

Yes.  For example, if you're unsure about your identification of your species, you can add a brief phrase or a standard 
term to express your doubts under the heading ``identificationQualifier``.  These are things like ``cf.``, and ``aff``, 
which mean ... what?

To strengthen your identification of the individual observed, you can use the term ``identificationReferences`` 
to show references you used in your identification.

To further strengthen your identification, you can add ``identificationVerificationStatus``, which is a "categorical 
indicator of the extent to which the taxonomic identification has been verified".

Need to add your name, as well as others that helped you in the identification of the individual?  Add this information 
under ``identifiedBy``.

If you're an academic with an ORCID, you can add your ORCID to the occurrence record under ``identifiedByID``, which 
could then be visible on your ORCID page.


Can I add information on multiple individuals?
-------------------------------------------------------

Yes, put the number of individuals observed under the column ``individualCount``.


What other information on my occurrence data might be useful?
---------------------------------------------------------------

You can record the presence or absence of an individual at a site by indicating "present" or "absent" under 
``occurrenceStatus``.  You can also use the term ``recordedBy``, to delineate between individuals that observed 
the species and individuals that identified it.

What are events? What information do I need for recording these?
-------------------------------------------------------------------

"Events" are referring to regular or one-off organised ... events ... such as bio blitzes and surveys.  This is 
meant to capture data over time, and is especially useful when recording information via surveys, as then you can 
see how the area you observe changes over time.  For these types of data, adding an ``eventID`` will help you 
separate the observations by a particular "event" (i.e. a survey), rather than dates as times, as surveys might be 
conducted over days or weeks.  

Recording what methods or protocols are used to record the data in these events is especially important for comparison 
between similar events, to eliminate possible variables for change.  The term ``samplingProtocol`` is used here, to 
describe the methods or protocols used during an event.