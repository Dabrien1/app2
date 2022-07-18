import libratom, sqlite3, time

def email_digest(): 
    '''function to scan target pst every hour and output a digest of recent activity'''
    
    #TODO: 
    #TODO: connect to database -> con = sqlite3.connect('example.db') OR maybe use special path name ':memory:' to create a temporary database in RAM
    #TODO: parse pst 
    #TODO: identify new emails (received in last 45 minutes, ref system time; time format in sqlite3 database = '2022-07-16 09:02:27.000000')
    #TODO: deliver digest (how? via system notification?, create and display .txt?)
    #TODO: delete database if necessary
    #TODO: run code every 60 minutes