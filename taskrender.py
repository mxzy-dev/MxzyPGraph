import sqlite3
import MxzyAdds as adds

def Render_Tasks():
    adds.Clear()
    print('$---------------Task List---------------$')
    db = sqlite3.connect('Graph.db')
    db.row_factory = sqlite3.Row
    c = db.cursor()
    c.execute('SELECT * FROM Task WHERE Status = "Uncomplete" ')
    Tasks = c.fetchall()
    for Task in Tasks:
        Task_Banner = f''' 
___________________________________________
|      {Task['Name']}
|----------------------------------------
|Descriprion: {Task['Description']}
|Priority: {Task['Priority']}
|Created: {Task['Created']}
|Deadline: {Task['DeadLine']}
|
|Status: {Task['Status']}
|ID: {Task['ID']}
|__________________________________________
'''
        print(Task_Banner)
    print('-'*25)
    adds.Enter()