class Task:
    def __init__(self, title, description, is_completed=False):
        self.title = title
        self.description = description
        self.is_completed = is_completed

    def complete(self):
        self.is_completed = True

    def undo_complete(self):
        self.is_completed = False

    def is_task_completed(self):
        return self.is_completed

class Tasks:

    def __init__(self):
        self.tasks_list = []

    # Lista de tareas
    def getList(self):
        return self.tasks_list

    # Crear tarea
    def createTask(self, title, description):
      task = Task(title, description)
      self.getList().append(task)
      return self.getList().index(task)

    # Leer una tarea
    def getTask(self, index):
        try:
            id = int(index)
            return self.getList()[id]
        except ValueError:
            raise TypeError("Por favor ingrese un ID válido.")

    # Editar una tarea
    def editTask(self, index, title, description):
        try:
            id = int(index)
            task = self.getTask(id)
            task.title = title
            task.description = description
            self.tasks_list[id] = task
            return task
        except ValueError:
            raise TypeError("El ID debe ser un número entero.")

    # Eliminar una tarea
    def removeTask(self, index):
        id = int(index)
        if not type(id) is int:
          raise TypeError("Only integers are allowed")
        return self.getList().pop(id)

    def isEmpty(self):
        return len(self.getList()) == 0

    def clear(self):
        self.getList().clear()

class Panel:

    def __init__(self):
        self.tasks = Tasks()

    def main(self):
        if self.tasks.isEmpty():
            print("\n\nNo tienes tareas.")
        else:
            self.showTasks()
        self.menu()

    def menu(self):
        print("\n\nPor favor, elige una acción:")
        print("0. Salir")
        print("1. Crear tarea")
        if not self.tasks.isEmpty():
            print("2. ver tarea")
            print("3. Marcar todas las tareas como: Tarea completada ✓")
            print("4. Eliminar tareas")
        while True:
            try:
                action = int(input("Selecciona una acción: "))
                if action == 1:
                    self.newTask()
                elif not self.tasks.isEmpty() and action == 2:
                    self.showTask()
                elif not self.tasks.isEmpty() and action == 3:
                    self.markAllTasksAsCompleted()
                elif not self.tasks.isEmpty() and action == 4:
                    self.clearTasks()
                elif action == 0:
                    self.exitApp()
                else:
                    print("\n\nAcción inválida")
                    self.menu()
                return action
            except ValueError:
                print("Error: Por favor, selecciona una acción válida.")

    def showTasks(self):
        print("\n\nTus tareas:")
        print("-----------------------------------------------------------------------------")
        taskList = self.tasks.getList()
        for index, task in enumerate(taskList):
            print(f"{task.title} (ID {index}) {'✓' if task.is_task_completed() else '✗'}")
            print("-----------------------------------------------------------------------------")

    def newTask(self):
        title = str(input("Ingresa el título de la tarea: "))
        description = str(input("Ingresa la descripción de la tarea: "))
        self.tasks.createTask(title, description)
        self.main()

    def showTask(self):
        while True:
            try:
                index = int(input("Ingresa el ID de la tarea: "))
                if 0 <= index < len(self.tasks.getList()):
                    task = self.tasks.getTask(index)
                    self.printTask(index, task)
                    return index
                else:
                    print(f"Error: No existe una tarea con el ID: {index}")
            except ValueError:
                print("Error: Por favor, ingresa un ID válido.")
                self.showTask()

    def printTask(self, index, task):
        print(f"\n\nID de la tarea: {index}")
        print("-----------------------------------------------------------------------------")
        print(f"Título de la tarea: {task.title}")
        print(f"Descripción de la tarea: {task.description}")
        print(f"Status: {'Tarea completada ✓' if task.is_task_completed() else 'Tarea sin completar ✗'}")
        print("-----------------------------------------------------------------------------")
        print("--------------------------- Opciones de tarea:-------------------------------")
        print("-----------------------------------------------------------------------------")
        print("0. Ver todas las tareas")
        print("1. Editar")
        if task.is_task_completed():
            print("2. Marcar como: Tarea sin completar")
        else:
            print("2. Marcar como: Tarea completada")
        print("3. Eliminar")
        print("-----------------------------------------------------------------------------")
        while True:
            try:
                option = int(input("Ingresa una opción (0/1/2/3): "))
                if option == 0:
                    self.main()
                elif option == 1:
                    self.editTask(index, task)
                elif option == 2:
                    if task.is_task_completed():
                        task.undo_complete()
                    else:
                        task.complete()
                        self.printTask(index, task)
                elif option == 3:
                    self.deleteTask(index)
                else:
                    print("\n\nAcción inválida")
                return option
            except ValueError:
                print("Error: Por favor, ingresa una opción válida.")

    def editTask(self, index, task=None):
        title = str(input("Ingresa el título de la tarea: "))
        description = str(input("Ingresa la descripción de la tarea: "))
        taskEdited = self.tasks.editTask(index, title, description)
        if not task:
            print("-----------------------------------------------------------------------------")
            print("--------------------------Tarea editada con éxito----------------------------")
            print("-----------------------------------------------------------------------------")
            self.printTask(index, taskEdited)
        else:
            self.main()

    def markAllTasksAsCompleted(self):
        taskList = self.tasks.getList()
        for task in taskList:
            task.complete()
        self.main()

    def deleteTask(self, index):
        self.tasks.removeTask(index)
        self.main()

    def clearTasks(self):
        self.tasks.clear()
        self.main()

    def exitApp(self):
        print("Gracias por probar :D. DE NADA, VUELVA PRONTO")


try:
    panel = Panel()
    panel.main()
except Exception as e:
    print(f"Error: {e}")







