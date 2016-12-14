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

python app.py data-in/AHR.thesaurus.xml -o -p

Notes:

* AppName thesaurus xml: 
``` 
/endeca/apps/AppName/config/pipeline/AppName.thesaurus.xml
```
* To export thesaurus entires: 

``` 
runcommand[.sh|.bat] IFCR exportContent thesaurus /endeca/apps/AppName/config/import/thesaurus true
```
* To import thesaurus entries: 
```
runcommand[.sh|.bat] IFCR importContent thesaurus /endeca/apps/AppName/config/import/thesaurus.zip
```

* Old version
```
/PlatformServices/6.1.0/bin/emgr_update --host localhost:8006 --action get_ws_settings --prefix appPrefix --dir ../ --app_name AppName
```
