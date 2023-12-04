import multiprocessing
import time
import keyboard

def run_script(script_name):
    # Exécute le script donné
    process = multiprocessing.Process(target=execute_script, args=(script_name,))
    process.start()
    process.join()

def execute_script(script_name):
    exec(open(script_name).read())

def fiko_process():
    # Exécute FIKO.py
    run_script('FIKO.py')

def plot_process():
    # Exécute FIKO.py
    run_script('plot.py')

if __name__ == '__main__':
    # Crée un processus pour exécuter FIKO.py
    fiko_proc = multiprocessing.Process(target=fiko_process)
    fiko_proc.start()

    time.sleep(60)
    plot = multiprocessing.Process(target=plot_process)
    plot.start()
    
    time.sleep(60)
    # Exécute XgClassifier.py et plot.py toutes les 3 minutes
    while True:
        if keyboard.is_pressed('q'):
            print("Exiting the program.")
            break
        run_script('XgClassifier.py')
        run_script('fatigue.py')
        time.sleep(20)  # Délai de 3 minutes
        
