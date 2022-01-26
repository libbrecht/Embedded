# maxime libbrecht
import time
import datetime

class my_task():
    #variables 
    name = None
    priority = -1
    period = -1
    execution_time = -1
    last_deadline = -1
    last_execution_time = None
    following_execution = None
    state = "SLEEPING"

    def __init__(self, name, priority, period, execution_time, last_execution, following_period):
        self.name = name
        self.priority = priority
        self.period = period
        self.execution_time = execution_time
        self.last_execution_time = last_execution
        self.following_period = following_period
        self.state = "READY"

    def update_state(self):
        if self.last_execution_time  < datetime.datetime.now():
            current_task.state = "READY"
        print("\t" + self.name + " : " + self.state + "\t(Deadline = " + self.last_execution_time.strftime("%H:%M:%S") + ", Priority = " + str(self.priority) + ")")


    def run(self):
        self.last_execution_time = datetime.datetime.now()
        print("\t" + self.name + " : Starting task (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
        self.state = "RUNNING"
        time.sleep(self.execution_time)
        self.state = "SLEEPING"
        print("\t" + self.name + " : Ending task (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")


if __name__ == '__main__':

    last_execution = datetime.datetime.now()

    task_list = []
    task_list.append(my_task(name="Pump 1", priority=2, period=5, execution_time=2, last_execution=last_execution, following_period = last_execution))
    task_list.append(my_task(name="Pump 2", priority=1, period=15, execution_time=3, last_execution=last_execution, following_period = last_execution))
    task_list.append(my_task(name="Machine 1", priority=4, period=5, execution_time=5, last_execution=last_execution, following_period = last_execution))
    task_list.append(my_task(name="Machine 2", priority=3, period=5, execution_time=3, last_execution=last_execution, following_period = last_execution))

    #sstock motor 
    global stock1
    stock1 = 0
    #stock wheel
    global stock2 
    stock2 = 0
    #global stock tank
    global tank
    tank = 0

    while (1):

        time_now = datetime.datetime.now()

        print("\nScheduler tick : " + time_now.strftime("%H:%M:%S"))

        for current_task in task_list:
            current_task.update_state()

        print('Stock tank:', tank)
        print('Stock 1:', stock1)
        print('Stock 2:', stock2)

        # pump runtime
        if tank <= 5:
            task_list[0].priority = 1
            task_list[1].priority = 2
        elif tank >= 40:
            task_list[0].priority = 50
            task_list[1].priority = 60
        elif tank > 5 & tank < 25:
            task_list[0].priority = 2
            task_list[1].priority = 3


        # Management of ressources & machines
        if stock2 <= 3 and stock1 >= 1:
            task_list[2].priority = 4
            task_list[3].priority = 3

        if stock1 == 0 and stock2 >=4:
            task_list[2].priority = 3
            task_list[3].priority = 4

        if tank < 20 :
            task_list[2].priority = 7
            task_list[3].priority = 6

        if stock1 > 0:
            if stock2/stock1 > 4:
                task_list[2].priority = 3
                task_list[3].priority = 4
            else:
                task_list[2].priority = 4
                task_list[3].priority = 3
                task_list[2].priority = 1
                task_list[3].priority = 2

        # which task 
        task_to_run = None
        priority = 100 


        for current_task in task_list:
            date = datetime.datetime.now()
            if current_task.following_period <= date:
                if current_task.priority < priority:
                    task_to_run = current_task
                    priority = current_task.priority


        #Update values
        if task_to_run.name == "Pump 1":
            tank=tank + 10
        elif task_to_run.name == "Pump 2":
            tank=tank + 20
        elif task_to_run.name == "Machine 1":
            tank=tank- 25
            stock1 = stock1 + 1
        elif task_to_run.name == "Machine 2":
            tank=tank-5
            stock2= stock2 +1
        task_to_run.run()
            