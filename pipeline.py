import multiprocessing
import time
import keyboard

FATIGUE_THRESH = 5


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
  
    while True:
        
        if keyboard.is_pressed('q'):
            print("Exiting the program.")
            break
        run_script('XgClassifier.py')
        run_script('fatigue.py')
        
        import fatigue
        fatigue_percentage = round(fatigue.cluster_1_percentage, 2)
        
        if (fatigue_percentage>FATIGUE_THRESH):
               
            import Alert
            Alert.send_email('karim akkari', 'karim ', 'mohammedkarim.akkari@esprit.tn',fatigue_percentage)
            
            i=3
            while(i>0):
                Alert.sound_alarm()
                i=i-1
                time.sleep(2)

            

        time.sleep(20) 
        
