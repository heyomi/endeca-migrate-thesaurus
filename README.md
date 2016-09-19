Brandon Plamondon's task

I need the thesaurus, stop words, phrases and redirects from the previous system transferred over to the new one.
Instead of taking the manual approach, we decided to create a script to do the following:

**Sample one way:**

```
#!xml

<THESAURUS_ENTRY_ONEWAY>
	<THESAURUS_FORM_FROM>bed bugs</THESAURUS_FORM_FROM>
	<THESAURUS_FORM_TO>insect spray</THESAURUS_FORM_TO>
	<THESAURUS_FORM_TO>mattress covers</THESAURUS_FORM_TO>
</THESAURUS_ENTRY_ONEWAY>
```

```
#!json

{
    "searchTerms": "bed bugs",
    "synonyms": [
    	"insect spray", 
    	"mattress covers"
	],
    "type": "one-way"
}
```


**Sample two way:**

```
#!xml

<THESAURUS_ENTRY>
	<THESAURUS_FORM>television</THESAURUS_FORM>
	<THESAURUS_FORM>tv</THESAURUS_FORM>
</THESAURUS_ENTRY>
```



```
#!json

{
    "synonyms": [
        "television",
        "tv"
    ],
    "type": "multi-way"
}
```


**Final output:**

```
#!json

{
    "ecr:createDate": "2016-08-26T10:52:18.211-05:00",
    "thesaurus-entries": [
	    {
		    "searchTerms": "bed bugs",
		    "synonyms": [
		    	"insect spray", 
		    	"mattress covers"
			],
		    "type": "one-way"
		},
		{
		    "synonyms": [
		        "television",
		        "tv"
		    ],
		    "type": "multi-way"
		}
    ],	
    "ecr:type": "thesaurus"
}
```

**TEST:**

python app.py data-in/AHR.thesaurus.xml