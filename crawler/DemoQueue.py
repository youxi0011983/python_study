import queue

if __name__ == '__main__':
    a = queue.Queue()
    a.put("hello")
    a.task_done()
    print(a.get())
    a.put("Python")
    a.task_done()
    a.put("php")
    a.task_done()
    a.put("JAVA")
    a.task_done()
    print(a.get())
    print(a.get())
    print(a.get())