import sqlite3
import MxzyAdds as adds

def Statistic():
    adds.Clear()
    print('$       Statistic       $')
    db = sqlite3.connect('Graph.db')
    c = db.cursor()
    c.execute('SELECT COUNT(*) FROM Task ')
    Total = c.fetchone()
    c.execute('SELECT COUNT(*) FROM Task WHERE Status = "Uncomplete" ')
    Active = c.fetchone()
    c.execute('SELECT COUNT(*) FROM Task WHERE Status = "Complete" ')
    Completed = c.fetchone()
    c.execute('SELECT COUNT(*) FROM Task WHERE Status = "Complete" AND Priority = "Low" ')
    Low = c.fetchone()
    c.execute('SELECT COUNT(*) FROM Task WHERE Status = "Complete" AND Priority = "Medium" ')
    Medium = c.fetchone()
    c.execute('SELECT COUNT(*) FROM Task WHERE Status = "Complete" AND Priority = "High" ')
    High = c.fetchone()
    print('-'*25,f'\nTotal: {Total}\nActive: {Active}\nComplete: {Completed}\n\nLow: {Low}\nMedium: {Medium}\nHigh: {High}\n','-'*25)
    adds.Enter()