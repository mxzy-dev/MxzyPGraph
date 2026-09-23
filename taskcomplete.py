import sqlite3
import MxzyAdds as adds

def Complete_Task():
    adds.Clear()
    print('-------Complete Task-------\n')
    try:
        Task_To_Complete = int(input('Task ID: '))
        db = sqlite3.connect('Graph.db')
        db.row_factory = sqlite3.Row
        c = db.cursor()
        c.execute('SELECT Name FROM Task WHERE ID = ? AND Status = "Uncomplete" ', (Task_To_Complete,))
        task = c.fetchone()
        if task is None:
            print(f"\n[!] Task with ID {Task_To_Complete} does not exist!")
            db.close()
            adds.Enter()
            return
        c.execute('UPDATE Task SET Status = "Complete" WHERE ID = ?',(Task_To_Complete,))
        print(f"\n-- Task '{task['Name']}' (ID: {Task_To_Complete}) Successfully Completed --")
        db.commit()
        db.close()
        adds.Enter()
    except ValueError:
        print('-'*25,'\nWrong ID')