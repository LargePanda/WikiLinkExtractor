# WikiLinkExtractor

Download wikiextractor from https://github.com/attardi/wikiextractor    
 
Navigate to the root folder, and run the following commands: 

sudo python setup.py install    
mkdir ../result    
python WikiExtractor.py ../../enwiki-20151201-pages-articles.xml --process 4 -o ../result --json -q -l
      
Put link_extractor under the same folder, and run the following commands:    
     
mkdir ../new_result     
python link_extractor.py ../result ../new_result     
