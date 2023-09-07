from configparser import ConfigParser

def config(filename='./endpoints/database/database.ini', section='postgresql'):
    #create parser
    parser = ConfigParser()

    #read database.ini file
    parser.read(filename)

    #save database parameters to dictionary
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} is not found in the {1} file.'.format(section, filename))
    
    return db