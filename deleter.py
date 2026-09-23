import sqlite3
import MxzyAdds as adds

def Delete_Task():
    try:
        adds.Clear()
        print('-------Deleting Task-------\n')
        To_Be_Deleted = int(input('ID to Delete: '))
        db = sqlite3.connect('Graph.db')
        c = db.cursor()
        c.execute("SELECT Name FROM Task WHERE ID = ?", (To_Be_Deleted,))
        task = c.fetchone()
        if task is None:
            print(f"\n[!] Task with ID {To_Be_Deleted} does not exist!")
            db.close()
            adds.Enter()
            return
        c.execute('DELETE FROM Task WHERE ID = ?',(To_Be_Deleted,))
        print(
            f"\n-- Task '{task['Name']}' (ID: {To_Be_Deleted}) Successfully Deleted --"
        )
        db.commit()
        db.close()
        adds.Enter()
    except ValueError:
        print('-'*25,'\nWrong ID')