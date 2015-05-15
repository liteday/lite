import Queue
import task
import threading

class Coordinator(object):
    
    def __init__(self):
        self.management_queue = Queue.Queue(10)        

    def run(self):
        self.run_worker()
        
    def check_system(sys_id=0):
        # validate ID?
        self.management_queue.put(task.CheckTask(sys_id))
        return system_response

    def deploy_system(self,config):
        if not True: #config.isValid():
            raise Exception()        
        self.management_queue.put(task.DeployTask(config))

    def run_worker(self):
        print "In run"
        self.worker_thread = threading.Thread(target=self.worker)
        self.worker_thread.daemon = True
        self.worker_thread.start()

    def process(self,item):
        print type(item)
        pass
        
    def worker(self):
        while True:
            try:
                self.process(self.management_queue.get(block=False))            
            except Exception as e:
                print "worker failed, ",str(e)
                return
            
    def end(self):
        self.worker_thread.exit()
        
if __name__ == '__main__':
    # test methods here
    coord = Coordinator()
    coord.deploy_system("This is my Config")
    coord.deploy_system("configuration")
    coord.run()
