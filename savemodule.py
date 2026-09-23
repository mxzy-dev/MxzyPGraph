import sqlite3
import MxzyAdds as adds
from datetime import date, timedelta

db = sqlite3.connect('Graph.db')
c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS Task (
ID INTEGER PRIMARY KEY AUTOINCREMENT,
Name text,
Description text,
Status text,
Priority integer,
Created text,
DeadLine text
)
""")
db.close()
def Create_Task():
    print('-------TASK CREATING-------\n')
    try:
        Task_Name = input('Task name:')
        Task_Description = input('Task description:')
        Task_Status = 'Uncomplete'
        Task_Priority = int(input('Task priority(1-2-3):'))
        Task_Created = (date.today()).strftime("%Y-%m-%d")
        Task_DeadLine = (date.today() + timedelta(days=(int(input('Days to complete:'))))).strftime("%Y-%m-%d")
        Adapted_Task_Priority = 'Medium'
        if Task_Priority in (1,2,3):
            if Task_Priority == 1:
                Adapted_Task_Priority = 'Low'
            elif Task_Priority == 2:
                Adapted_Task_Priority = 'Medium'
            elif Task_Priority == 3:
                Adapted_Task_Priority = 'High'
            else:
                print('-'*25,'\nWrong Priority...')
                adds.Enter()
                pass
        else:
            print('-'*25,'\nWrong Priority...')
            adds.Enter()
            pass
        db = sqlite3.connect('Graph.db')
        c = db.cursor()
        c.execute("SELECT rowid FROM Task")
        row = c.fetchone()
        ID = row[0] if row else 1
        c.execute(
        "INSERT INTO Task VALUES (?, ?, ?, ? ,? ,? ,?)",
        (None, Task_Name, Task_Description, Task_Status, Adapted_Task_Priority, Task_Created, Task_DeadLine),
        )
        db.commit()
        db.close()
        print('-'*25,'\nSucessfull')
    except ValueError:
        print('-'*25,'\nWrong')
        adds.Enter()
    except OverflowError:
        print('-'*25,'\nDeadline out of range...')
        adds.Enter()