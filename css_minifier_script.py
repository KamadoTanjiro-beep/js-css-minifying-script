import requests
import logging


try:
    def js_minifier(file_name):
        """js_minifier(file_name) : requires a valid file name or address\n
        Returns : a new file with "-min.js" format in the same directory"""

        temp = file_name.split('.')
        new_file_name = temp[0]+"-min."+temp[1]
        url = 'https://cssminifier.com/raw'
        data = {'input': open(file_name, 'r').read()}
        response = requests.post(url, data=data)
        f = open(new_file_name, "w")
        f.write(response.text)
        f.close()

    # Create and configure logger
    logging.basicConfig(filename="log.txt",
                        format='\n%(asctime)s %(message)s',
                        filemode='a')

    # Creating an object
    logger = logging.getLogger()

    file_name = 'style.css'  # SET THE INPUT FILE NAME HERE

    js_minifier(file_name)

except Exception as Argument:
    print("An error. Check log.txt")
    logging.exception("Error Message:")
