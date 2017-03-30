import json
import re
import sys
import urllib
from os import listdir
from os.path import isfile, join

def extract(mypath, newpath):
    folders = [f for f in listdir(mypath)]


    for folder in folders:
        g = open(newpath+"/"+folder, 'w')
        print "[INFO]", "Extracting", folder

        files = [f for f in listdir(mypath+folder) if isfile(join(mypath+folder, f))]
        
        for wikifile in files:
            with open(mypath+folder +"/"+wikifile) as f:
                
                for line in f:
                    line = line.strip().decode('utf-8')
                    entity = json.loads(line)
                    url = entity['url']
                    text = entity['text']
                    wid = entity['id']
                    title = entity['title']
                    
                    entity['annotations'] = []
                    ms = re.finditer('<a href="([^"]+)">([^>]+)</a>', text)
                    deltaStringLength = 0
                    for m in ms:              
                        if urllib.quote("#") not in m.group(1):
                            entity['annotations'].append({
                                "uri"    :   urllib.unquote(m.group(1)), 
                                "surface_form" :   m.group(2), 
                                "offset"  :   m.start() - deltaStringLength
                            })
                        deltaStringLength += len(m.group(0)) - len(m.group(2))
                    entity['text'] = re.sub('<a href="([^"]+)">([^>]+)</a>', lambda m: m.group(2), text)
                    g.write(json.dumps(entity).encode('utf-8') +"\n")
        g.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Expect an input: wikiextractor_output_folder, export_folder"
        print "Please give the files in that order."
        print "For example, python link_extractor.py ./we_result ./link_result"

    old_folder = sys.argv[1]
    new_folder = sys.argv[2]   
    extract(old_folder, new_folder)