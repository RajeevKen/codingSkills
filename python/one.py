import random
import os
import logging
class rm:

    def generate_pass():
        '''
        Password Generator
        '''
        logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
        
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        strng = random.randint(2,2)
        logging.Logger.info(logger,msg=strng)
        print(strng)

rm.generate_pass()