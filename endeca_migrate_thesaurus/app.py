#!/usr/bin/python
import xml.etree.ElementTree
import json
import datetime
import sys, getopt

def convert_xml2json(inputf, outputf):
    input_file = inputf #"data-in/AHR.thesaurus.xml"
    output_file = outputf if outputf is not None else 'thesaurus.json' #"data-out/thesaurus.json"
    root_tag = "THESAURUS"
    multiway_tag = "THESAURUS_ENTRY"
    oneway_tag = "THESAURUS_ENTRY_ONEWAY"
    multiway_thesaurus_entry_tag = "THESAURUS_FORM"
    oneway_thesaurus_entry_tag = "THESAURUS_ENTRY_ONEWAY"
    oneway_thesaurus_search_terms_tag = "THESAURUS_FORM_FROM"
    oneway_thesaurus_synonyms_tag = "THESAURUS_FORM_TO"
    
    today = datetime.date.today()
    data = {}
    
    print "Reading file: " + input_file 
    root = xml.etree.ElementTree.parse(input_file).getroot()
    
    if root is not None and root.tag == root_tag:
        thesaurus_entries = []
        count = 0
        
        print "Processing..."
        
        # One way
        for entries in root.findall(oneway_tag):
            synonyms_array = []
            
            searchTerms = entries.find(oneway_thesaurus_search_terms_tag).text
                
            for synonym in entries.findall(oneway_thesaurus_synonyms_tag):
                synonyms_array.append( synonym.text )
            
            thesaurus_entries.append({
                "searchTerms" : searchTerms,
                "synonyms" : synonyms_array,
                "type" : "one-way"
            })
                
            count += 1
        
        # Multiway
        for entries in root.findall(multiway_tag):
            synonyms_array = []
            for synonym in entries.findall(multiway_thesaurus_entry_tag):
                synonyms_array.append( synonym.text )
            
            thesaurus_entries.append({
                "synonyms" : synonyms_array,
                "type" : "multi-way"
            })
            
            count += 1
        
        if thesaurus_entries is not None:
            data = {
                "ecr:type" : "thesaurus",
                "thesaurus-entries" : thesaurus_entries, 
                 "ecr:createDate" : today.strftime("%Y-%m-%dT%H:%M:%S.%f")
            }
            
            with open(output_file, 'w') as outfile:
                json.dump(data, outfile)
        
        print "Complete!"
        print str(count) + " thesaurus entires migrated"
        print "Outfile file: " + output_file
    else:
        print "Invalid THESAURUS xml file"
    
def main(argv):
    try:
        if len(sys.argv) == 2:
            convert_xml2json(sys.argv[1], None)
        elif len(sys.argv) == 3:
            convert_xml2json(sys.argv[1], sys.argv[2])
        else:
            print 'app.py <inputfile> <outputfile>'
            sys.exit(2)
    except:
        print "Error:", sys.exc_info()[0]
        print "Error:", sys.exc_info()[1]
        # raise
        
if __name__ == "__main__":
   main(sys.argv[1:])