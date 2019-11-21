# riaps:keep_import:begin
from riaps.run.comp import Component
import logging
import ctypes
import time
# import capnp
# import memfail_capnp

# riaps:keep_import:end

class MemPublisher(Component):

# riaps:keep_constr:begin
    def __init__(self):
        super(MemPublisher, self).__init__()
        self.val = 0
        self.logger.info("-----init publishier-----")
        
    def handleActivate(self):
        self.logger.info("starting seg fault timer")
        self.clock.setDelay(20.0)
        self.clock.launch()
# riaps:keep_constr:end

# riaps:keep_trigger:begin
    def on_trigger(self):
        if self.val < 10:            
            now = self.trigger.recv_pyobj()
            self.logger.info("on_trigger(): %s" % now)
            self.logger.info("-----publishing value-----")
            self.val = self.val + 1
            self.pubport.send_pyobj(self.val)
# riaps:keep_trigger:end

# riaps:keep_clock:begin
    def on_clock(self):
        now = self.clock.recv_pyobj()
        self.logger.info("on_clock(): %s" % now)
        try:
            f = open("check_seg.txt", "x")
            f.close()
            self.clock.halt()
            self.logger.info("\n\n-----causing segmentation fault-----\n")
            time.sleep(2)
            ctypes.string_at(0)
        except FileExistsError as e:
            self.logger.info("file exists, actor restarted")
        except:
            self.logger.info("could not create file")
# riaps:keep_clock:end

# riaps:keep_impl:begin

# riaps:keep_impl:end