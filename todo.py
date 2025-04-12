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
      
      
# 動作確認用
if __name__ == "__main__":
  tm = TaskManager()
  tm.add_task("牛乳を買う")
  tm.add_task("Pythonの勉強")
  tm.list_tasks()