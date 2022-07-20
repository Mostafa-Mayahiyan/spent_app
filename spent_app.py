#import api.py and import any functions from api for spent_app.py
from api import *
# import docopt framwork and import docopt function for making command and calling the functions of  the script 
from docopt import docopt
#import tabulate framwork and import tabulate for showing results to table style
from tabulate import tabulate
print('''
                       |                      
  __| __ \   _ \ __ \  __|   _` | __ \  __ \  
\__ \ |   |  __/ |   | |    (   | |   | |   | 
____/ .__/ \___|_|  _|\__| \__,_| .__/  .__/  
     _|                 _____|   _|    _|     

''')




# make a value and insert commands for docopt and show on command line and for making commands for calling functions

usage = '''
Usage:
   spend_app.py --init
   spend_app.py --insert <name> <price> [<massage>]
   spend_app.py --delete <name> 
   spend_app.py --show [<name>]
   spend_app.py --aboutme
'''

#make a value then insert docopt function and give usage value to docopt 
args = docopt(usage)

# in this line we say if args was --init call init function from api.py
if args['--init']:
    init()
    print('you made a Table..!')


if args['--show']:
    #give name to name value 
    name = args['<name>']
    #total is trsult from show function in api.py  and result is write value from show function too then we give show function to them
    total,result = show(name)
    print('Total : ', total)
    #we give result value to tabulate as it can show reslut to table style
    print(tabulate(result))

if args['--aboutme']:
     print(aboutme())
    
if args['--insert']:
    try:
        #give name to name value
       name = args['<name>']
       #then give massage to massage value too
       massage = args['<massage>']
       #give all of values to insert function except name and massage as i gave them before then that
       insert(name,float(args['<price>']),massage)
       print('your item added')
    except:
        # if user insert wrong data to script or  any error from this command print usage value and show all of commands 
        print(usage)



if args['--delete']:
    try: 
        #give name to delete function for removing chosen data
        delete(args['<name>'])
        print('your item deleted')
    except:
        print(usage)

    


