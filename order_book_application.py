#Task class, has description, est of hors req'd, name of programmer assigned, field for keeping track of whether task is finished, unique id
class Task:
  #create class variable that changes with each instance made
  uuid = 0
  
  def __init__(self, description:str, programmer:str, workload:str):
    Task.uuid += 1
    self.description = description
    self.programmer = programmer
    self.workload = workload
    self.is_completed = False
    self.id = Task.uuid
  
  #return the state of completion of task
  def is_finished(self):
    return self.is_completed
  
  #mark task as completed
  def mark_finished(self):
    self.is_completed = True
  
  #printing method that changes based off completion state
  def __str__(self):
    completion_state = "NOT FINISHED"
    if self.is_completed == True:
      completion_state = "FINISHED"
    return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {completion_state}"


##Class orderbook collects all tasks ordered 
class OrderBook:
  def __init__(self):
    self.orders = []
  
  def add_order(self, description, programmer, workload):
    self.orders.append(Task(description, programmer, workload))

  def all_orders(self):
    return self.orders
  
  def programmers(self):
    new_list = [i.programmer for i in self.orders]
    new_list2 = list(set(new_list))
    return new_list2
  
  def mark_finished(self, id:int):
    for i in self.orders:
      if i.id == id:
        i.mark_finished()
        return
    raise ValueError()
  
  def finished_orders(self):
    return [orders for orders in self.orders if orders.is_completed == True]

  def unfinished_orders(self):
    return [orders for orders in self.orders if orders.is_completed == False]

  def status_of_programmer(self, programmer:str):
    finished = 0
    unfinished = 0
    hoursfin = 0
    hoursunfin = 0
    for i in self.orders:
      if i.programmer == programmer:
        if i.is_completed == True:
          finished += 1
          hoursfin += int(i.workload)
        else:
          unfinished += 1
          hoursunfin += int(i.workload)
    if int(finished) == 0 and int(unfinished) == 0:
      raise ValueError()
    return (finished, unfinished, hoursfin, hoursunfin)

class OrderApplication():
  def __init__(self):
    self.__order = OrderBook()
  
  
  #List of commands
  def commands(self):
    print('commands:')
    print("0 exit")
    print("1 add order")
    print("2 list finished tasks")
    print("3 list unfinished tasks")
    print("4 mark task as finished")
    print("5 programmers")
    print("6 status of programmers")
  
  
  #add order to list description, programmer, workload
  def add_order(self):
    desc = input("Description: ")
    prog_wl = input("programmer and workload estimate: ").split(" ")
    #error handling
    ## If workload is not able to be converted to type int, or only 1 entry is found, return error
    try:
      int(prog_wl[1])
    except (ValueError, IndexError):
      print('erroneous input')
      return
    
    print("added!")
    #Add order to list
    self.__order.add_order(desc, prog_wl[0], prog_wl[1])
  
  #lists finished tasks
  def finished_tasks(self):
    if len(self.__order.finished_orders()) == 0:
      print('no finished tasks')
    else:
      for i in self.__order.finished_orders():
        print(i)
  
  #lists unfinished tasks
  def unfinished_tasks(self):
    if len(self.__order.unfinished_orders()) == 0:
      print('no unfinished tasks')
    else:
      for i in self.__order.unfinished_orders():
        print(i)
  
  #marks a task as finished using ID
  def mark_finished(self):
    #error handling, if id is found, mark as finished
    try:
      id = int(input("id: "))
      self.__order.mark_finished(id)
      print("marked as finished")
    except ValueError:
      print('erroneous input')

  #returns all programmers within data set
  def programmers(self):
    programmers = self.__order.programmers()
    for i in programmers:
      print(i)
      
  #returns programmers status
  def programmers_status(self):
    progr = input("programmer: ")
    #Error handling, if programmer does not reflect any within data set, print error
    try:
      finished, unfinished, hoursfin, hoursunfin = self.__order.status_of_programmer(progr)
      print(f"tasks: finished {finished} not finished {unfinished}, hours: done {hoursfin} scheduled {hoursunfin}")
    except ValueError:
      print('erroneous input')

  #Start while loop for commands
  def execute(self):
    while True:
      self.commands()
      print("")
      command = input("command: ")
      if command == "0":
        break
      elif command == "1":
        self.add_order()
      elif command == "2":
        self.finished_tasks()
      elif command == "3":
        self.unfinished_tasks()
      elif command == "4":
        self.mark_finished()
      elif command == "5":
        self.programmers()
      elif command == "6":
        self.programmers_status()
      print("")

#run program
application = OrderApplication()
application.execute()
