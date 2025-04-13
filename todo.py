class Task:
  def __init__(self, id, title):
    self.id = id
    self.title = title
    self.completed = False
    
  def mark_done(self):
    self.completed = True
    
  def __str__(self):
    status = "✓" if self.completed else "✗"
    return f"[{self.id}] {self.title} ({status})"


class TaskManager:
  def __init__(self):
    self.tasks = []
    self.next_id = 1
    
  def add_task(self, title):
    task =Task(self.next_id, title)
    self.tasks.append(task)
    self.next_id += 1
    
  def list_tasks(self):
    for task in self.tasks:
      print(task)
      
      
# 差し替え
if __name__ == "__main__":
  tm = TaskManager()

  while True:
      command =input("> ").strip()
      
      if command.startswith("add "):
        title = command[4:]
        tm.add_task(title)
        
      elif command == "list":
        tm.list_tasks()
        
      elif command.startswith("done "):
        try:
          id = int(command[5:])
          for task in tm.tasks:
            if task.id == id:
              task.mark_done()
              break
        except ValueError:
          print("番号がただしくありません")
          
      elif command.startswith("delete "):
        try:
          id = int(command[7:])
          tm.tasks = [task for task in tm.tasks if task.id != id]
        except ValueError:
          print("番号がただしくありません")
          
      elif command == "exit":
        print("終了します。")
        break
      
      else:
        print("不正なコマンドです。")