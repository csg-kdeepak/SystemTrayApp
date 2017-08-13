# -*- coding: utf-8 -*-
def read_ini_file():
    """
    Read the toolsetup.ini file which has the location of
    the data file. ini file is always kept in the
    application location
    error handling will be in the main program to display
    a error dialog box

    Parameters:
    ln - String object to get the datafile path
    """

    fh = open('toolsetup.ini', 'r')
    # init return variables
    lrt = {}
    for ln in fh:
        ln = ln.strip()
        ln = ln.split('>')
        lrt[ln[0]] = ln[1]

    fh.close()

    return lrt


def get_login_data():
    """
    get the login data from the data csv file
    file path has been specified in the ini
    file
    """
    data_files = read_ini_file()

    df = open(data_files['DATA'], 'r')

    env_list = []
    for line in df:
        line = line.strip().split(',')
        env_list.append(line)

    return env_list, data_files['BILLING']
