#!/usr/bin/python
import xml.etree.ElementTree
import json
import datetime
import sys, getopt

def convert_xml2json(inputf, outputf, options):
    input_file = inputf #"data-in/SAMPLE.thesaurus.xml"
    output_file = outputf if outputf is not None else 'thesaurus.json' #"data-out/thesaurus.json"
    
    # Options
    if options is None:
        options = options[False, False]
        
    pretty_print_enabled = options [0]
    output_thesaurus_enabled = options [1]
    
    root_tag = "THESAURUS"
    multiway_tag = "THESAURUS_ENTRY"
    oneway_tag = "THESAURUS_ENTRY_ONEWAY"
    multiway_thesaurus_entry_tag = "THESAURUS_FORM"
    oneway_thesaurus_entry_tag = "THESAURUS_ENTRY_ONEWAY"
    oneway_thesaurus_search_terms_tag = "THESAURUS_FORM_FROM"
    oneway_thesaurus_synonyms_tag = "THESAURUS_FORM_TO"

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
                 "ecr:createDate" : str(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"))
            }
            
            if pretty_print_enabled:
                data = json.dumps(data, indent=4, sort_keys=True)
            
            with open(output_file, 'w') as outfile:
                json.dump(data, outfile)
        
        print "Complete!"
        print str(count) + " thesaurus entires migrated"
        print "Outfile file: " + output_file
        
        if output_thesaurus_enabled:
            print data
    else:
        print "Invalid THESAURUS xml file"
    
def main(argv):
    try:
        print sys.argv
        
        # Options
        pretty_print_enabled = True if sys.argv is not None and "-p" in sys.argv else False
        output_thesaurus_enabled = True if  sys.argv is not None and "-o" in sys.argv else False
        
        options = [pretty_print_enabled, output_thesaurus_enabled]
        
        if sys.argv is not None and "-p" in sys.argv:
            sys.argv.remove('-p')
        
        if sys.argv is not None and "-o" in sys.argv:
            sys.argv.remove("-o")
        
        print sys.argv
        
        if len(sys.argv) == 2:
            convert_xml2json(sys.argv[1], None, options)
        elif len(sys.argv) == 3:
            convert_xml2json(sys.argv[1], sys.argv[2], options)
        elif len(sys.argv) == 3: # Options
            convert_xml2json(sys.argv[1], sys.argv[2], options)
        else:
            print 'app.py <inputfile> <outputfile> OPTIONAL: -p (pretty print) -o (outputs entries in console)'
            sys.exit(2)
    except:
        print "Error:", sys.exc_info()[0]
        print "Error:", sys.exc_info()[1]
        #raise
        
if __name__ == "__main__":
   main(sys.argv[1:])