Explaining Required Darwin Core Terms In the Context of Data
=============================================================

Those of you reading this have probably guessed that "Required Terms" are terms that you need to include in 
your data.  But what do they actually mean when they are in a dataset?

Take the following example (visualised using the Python library ``pandas`` - example data :download:`here <data-clean.csv>`)

.. program-output:: python -c "import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);print(pd.read_csv('Standards_Guide/data-clean.csv').head())"

If you scroll to the right, you can see that there are a lot of columns, but why are there so many?  
And why are there so many that are required?

How is an occurrence recorded? (``basisOfRecord``)
---------------------------------------------------

Let's now look at the column titled ``basisOfRecord`` (in the dataset visualised above, it is the column all the 
way to the right.)

.. program-output:: python -c "import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);print(pd.read_csv('Standards_Guide/data-clean.csv')['basisOfRecord'].head())"

The term ``basisOfRecord`` is not an obvious one, but it is required for all data that fits within the Darwin 
Core Standard.  It is a description of how someone recorded their observation.  For those of you who read the 
`Introduction To The Available Standards <Introduction_to_Standards.html>`_, under "Darwin Core" it mentions 
you can specify whether the observation is via a human spotting it, if it's a museum specimen, a sample, etc.  
For this example dataset, it is set to ``HumanObservation``.  Other terms include ``PreservedSpecimen`` and 
``MaterialSample``.  For a full list of possible values go to the Vocabulary List and look under the "Darwin 
Core" tab.  ``basisOfRecord`` will be under the *Required* section, and will include examples.

When is an occurrence recorded? (``eventDate``)
---------------------------------------------------

Now that we know how the observation was recorded, when was it recorded?  This is specified by the ``eventDate``
column.

.. program-output:: python -c "import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);print(pd.read_csv('Standards_Guide/data-clean.csv')['eventDate'].head())"

The ``eventDate`` is relatively self-explanatory, where it refers to the date on which the occurrence occurred.  
This is usually in the format ``YYYY-MM-DD``, or ``YYYY-MM-DDTHH:MM:SS`` where the ``T`` splits the date and 
the time.  Including the time can be particularly useful for species that are noctural.

Where is an occurrence recorded? (Spatial Information)
-------------------------------------------------------

Knowing where an occurrence was recorded follows describing how and when it was recorded.  However, there are a 
few extra pieces of information you need to included to make your data richer and more meaningful:

.. program-output:: python -c "import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);print(pd.read_csv('Standards_Guide/data-clean.csv')[['decimalLatitude','decimalLongitude','geodeticDatum','coordinateUncertaintyInMeters']].head())"

``decimalLatitude`` and ``decimlLongitude`` are pretty self-explanatory, in that they represent degrees latitude 
and degrees longitude of where the species was recorded.  Along with this is something called ``coordinateUncertaintyInMeters``.  
This is the error on your latitude and longitude measurement.  For example, if you are recording a sighting using 
the GPS on your phone, this has an inherent measurement uncertainty.  The error that is most common, or most likely, 
is 100 meters, which is why that is the value in this dataset.

``geodeticDatum`` is a term that describes a Coordinate Reference System (CRS).  A CRS is a specific way to represent 
data from a 3D spherical object (in this case, planet Earth) onto a two-dimensional surface.  As you can imagine, there 
are many ways to do this, and knowing which way you are representing these points prevents confusion between two datsets, 
as knowing the CRS could explain potential discrepancies in the data.  The Atlas of Living Australia uses the World Geodetic 
System 84, or WGS84, as shown in the dataset.  `This standard <https://en.wikipedia.org/wiki/World_Geodetic_System>`_ is 
used in satellite navigation and GPS.

What species was recorded? (Taxonomic Information)
-------------------------------------------------------

Now that we've answered the "When" and "Where", we will answer the "What".  Specifically, what species was observed?

The ALA requires the following information from users, shown below in the example dataset:

- ``scientificName``
- ``taxonRank``
- ``kingdom``
- ``phylum``
- ``class``
- ``order``
- ``family``
- ``genus``

.. program-output:: python -c "import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);print(pd.read_csv('Standards_Guide/data-clean.csv')[['scientificName','taxonRank','kingdom','phylum','class','order','family','genus']].head())"

This is to ensure that the species you have seen has been correctly identified according to the taxonomic backbone you 
are using.  Here, we are using the ALA backbone.  This will also help disambiguate things like homonyms, or other 
identification mistakes and errors.  Adding higher order taxa is straightforward with the ``galaxias-python`` package, 
though it is always a good idea to double-check your taxonomy before submitting data.  If you are concerned about any 
taxonomy suggestions/recommendations the ALA has made for your species, please email `contact us <mailto:support@ala.org.au>`_.

How Can I Make Every Observation Unique? (Unique Identifiers)
----------------------------------------------------------------

The final requirement for every observation is a way to make your observation unique, especially in a large data repository.  
The easiest way to do this is to generate a Globally Unique Identifier (GUID) or a Universally Unique Identifier (UUID).  
There are ways to do this in ``Python`` or ``galaxias-python``, but they should look like this:

.. program-output:: python -c "import pandas as pd;pd.set_option('display.max_columns', None);pd.set_option('display.expand_frame_repr', False);pd.set_option('max_colwidth', None);print(pd.read_csv('Standards_Guide/data-clean.csv')[['occurrenceID']].head())"