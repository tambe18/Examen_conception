import datetime

import time


class Pump:
    def __init__(self,q_prod):
        self.q_prod = q_prod
    
    def extract_oil(self,tank):
        time.sleep(self.tmp_exe)
        tank.remplir_tank(self.q_prod)

        
        
        
class Machine:
    def __init__(self,q_oil,q_product,name):
        self.q_oil= q_oil
        self.q_product = q_product
        self.name=name
        self.stock = 0


    def production(self,tank):
        if tank.q_courante >= self.q_oil:
            tank.q_courante -= self.q_oil
            
            self.stock += self.q_product
            print("Le stock de {} est = {}\n".format(self.name,self.stock))
                
            
    
class Tank:
    def __init__(self,q_max, q_courante):
        self.q_max = q_max
        self.q_courante = q_courante
        
    def remplir_tank(self,q_oil_to_add):
        if self.q_courante < self.q_max:
            new_quantite = self.q_courante + q_oil_to_add
            if new_quantite <= self.q_max:
                self.q_courante = new_quantite
            else:
                self.q_courante = tank.q_max
                print("vous avez débordé...\n")

                

                
Pump1 = Pump(10)
Pump2 = Pump(20)

machine1= Machine(25,1,"motor")
machine2= Machine(5,1,"wheel")

tank= Tank(50,0)


class my_task():

    name = None
    priority = -1
    period = -1
    execution_time = -1
    last_deadline = -1
    last_execution_time = None


    ############################################################################
    def __init__(self, name, priority, period, execution_time, last_execution):

        self.name = name
        self.priority = priority
        self.period = period
        self.execution_time = execution_time
        self.last_execution_time = last_execution


    ############################################################################
    def run(self):

        if self.name == "pump1":
            self.last_execution_time = datetime.datetime.now()
            time.sleep(self.execution_time)
            tank.remplir_tank(Pump1.q_prod)

        if self.name == "pump2":
            self.last_execution_time = datetime.datetime.now()
            time.sleep(self.execution_time)
            tank.remplir_tank(Pump2.q_prod)

        if self.name == "machine1":
            self.last_execution_time = datetime.datetime.now()
            time.sleep(self.execution_time)
            machine1.production(tank)

        if self.name == "machine2":
            self.last_execution_time = datetime.datetime.now()
            time.sleep(self.execution_time)
            machine2.production(tank)


####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':


    last_execution = datetime.datetime.now()


    # Instanciation of task objects
    task_list = []
    
    task_pump_1 = my_task(name="pump1", priority = -1, period = 5, execution_time = 2, last_execution = last_execution)
    task_pump_2 = my_task(name="pump2", priority = -1, period = 15, execution_time = 3, last_execution = last_execution)
    task_machine_1 = my_task(name="machine1", priority = -1, period = 5, execution_time = 5, last_execution = last_execution)
    task_machine_2 = my_task(name="machine2", priority = -1, period = 5, execution_time = 3, last_execution = last_execution)
    
    task_list.append(task_pump_1)
    task_list.append(task_pump_2)
    task_list.append(task_machine_1)
    task_list.append(task_machine_2)

    t = time.time()
    while(time.time()-t<120):

        time_now = datetime.datetime.now()
        
        #print("\nScheduler tick : " + time_now.strftime("%H:%M:%S"))

        # Find the task with Earliest deadline

        task_to_run = task_pump_1
        earliest_deadline = time_now + datetime.timedelta(hours=1)	# Init ... not perfect but will do the job

        for current_task in task_list:
            
            if tank.q_courante>=20:
                task_machine_1.priority = 1
                task_machine_2.priority  = 1
                
                task_pump_1.priority = -1
                task_pump_2.priority = -1
                
                if machine2.stock > 4*machine1.stock:
                    task_machine_1.priority += 1
                else :
                    task_machine_2.priority += 1
            else:
                task_pump_1.priority = 1
                task_pump_2.priority = 1
                
                task_machine_1.priority = -1
                task_machine_2.priority  = -1
            
                
                if tank.q_courante < 10:
                    task_pump_1.priority += 1
                else:
                    task_pump_2.priority += 1

    
            current_task_next_deadline = current_task.last_execution_time + datetime.timedelta(seconds=current_task.period)
            #print("\tDeadline for task " + current_task.name + " : " + current_task_next_deadline.strftime("%H:%M:%S"))
            
            #idx_max = np.argmax(task_pump_1.priority,task_pump_2.priority,task_machine_1.priority,task_machine_2.priority)
            #max_task_priority = task_list[idx_max]
            

            if (current_task_next_deadline < earliest_deadline and current_task.priority >1):              
                    earliest_deadline = current_task_next_deadline
                    task_to_run = current_task
                    


        # Start task
        task_to_run.run()


#En 2 min on a produit 19 wheels et 5 motors ce qui est très bien 
#sans les priorité on a beaucoup de perte d'huile et aussi le nombre de wheel est desiquilibré
#L'optimisation finale est optimale à mon avis car
#Je n'attends pas que le tank se remplir pour changer les priorités, car avec 20 on peut déja se concentrer sur la production
#De même lorsque le niveau est très bas c'est mieux d'acctionner pump1 qui à une periode faible