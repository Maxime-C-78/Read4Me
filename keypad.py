from logger import logger
from constantes import CB
from sshkeyboard import listen_keyboard

class keypad:
    
    def __init__(self, dict_callback):
        self.dict_callback=dict_callback
        self.callbacks=[None]*len(CB)

    def start(self):
        print("start") 

    def listen(self):
        print("attente appuye")
        listen_keyboard(on_press=self.press)
        
    def find_index_cb(self, v): 
        for k, val in self.dict_callback.items(): 
            if v == val: 
                return k 
        
    def links(self, callbacks):
        self.callbacks=callbacks
        for key in self.dict_callback:
            callback=callbacks[key.value]
            logger.info("Link keyboard %d %s->%s" % (key.value, self.dict_callback[key], callback))
            self.callbacks[key.value]=callback
    
    def press(self,key):
        print("touche : ", key)
        if key in self.dict_callback.values():
            idx=self.find_index_cb(key)
            #print('call', idx, idx.value, str(len(self.callbacks)))
            print(key)
            self.callbacks[idx.value]()
