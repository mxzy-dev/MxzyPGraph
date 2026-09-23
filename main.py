#MxzyPGraph
import MxzyAdds as adds
import savemodule as save
import taskrender as rend
import deleter as deltask
import taskcomplete as comp
import stats


def main():
    try:
        adds.Clear()
        print('$    MxzyPGraph    $')
        print('''------------------
1.Create Task
2.Task List
3.Complete Task
4.Delete Task
5.Statistic
6.Quit
------------------\n
        ''')
        Select = input('Select action:')dd8
        if Select == '1':
            save.Create_Task()
        elif Select == '2':
            rend.Render_Tasks()
        elif Select == '3':
            comp.Complete_Task()
        elif Select == '4':
            deltask.Delete_Task()
        elif Select == '5':
            stats.Statistic()
        elif Select == '6':
            quit()
        else:
            print('\nWrong Select...')
    except ValueError:
        print('-'*30,'Invalid Action...')
        adds.Enter()


if __name__ == "__main__":
    while True:
        main()