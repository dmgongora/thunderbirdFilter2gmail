##########################################################
# - This script takes email directions from Thunderbird  #
#   database file and stores them in a file compatible   #
#   with Gmail XML format.                               #
# - The Gmail filter template receives two parameters:   #
#    1. List of emails                                   # 
#    2. Label                                            #
#   These parameters are extracted from the Thunderbird  #
#   dat file.                                            #
##########################################################
import re
db_name = 'msgFilterRules.dat'
filter_template = 'mailFilterTemplate.xml'

with open(db_name, "r") as f:
    for line in f:
        if folder:
            '''
            Identify label
            '''
            print '----------'
            filter_filename = 'mailFilters_{}.xml'.format(folder.group()[2:])
            filter_name = folder.group()[2:]
            print '{} ({})'.format(filter_name, filter_filename)
            print '----------'
            '''
            Extract email directions
            '''
            emails = re.findall(r',[\w.-]+@[\w.-]+', line)
            emails = ' OR '.join([email[1:] for email in emails])
            '''
            Save data in Google format (XML file)
            '''
            with open(filter_template, "r") as g:
                file_contents = g.read().format(emails, filter_name)
                with open(filter_filename, "w") as h:
                    print file_contents
                    h.write(file_contents)
                
        folder = re.search(r'\w/\w+', line)
