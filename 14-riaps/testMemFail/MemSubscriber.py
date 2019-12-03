# riaps:keep_import:begin
from riaps.run.comp import Component
import logging
# import capnp
# import memfail_capnp

# riaps:keep_import:end

class MemSubscriber(Component):

# riaps:keep_constr:begin
    def __init__(self):
        super(MemSubscriber, self).__init__()
# riaps:keep_constr:end

# riaps:keep_subport:begin
    def on_subport(self):
        msg = self.subport.recv_pyobj()
        self.logger.info("\n\n-----received subscribed message : %s-----\n" % msg)
# riaps:keep_subport:end

# riaps:keep_impl:begin
    def handlePeerStateChange(self, state, uuid):
        self.logger.info("\n\n----------peer %s state changed to %s----------\n" % (uuid, state))
# riaps:keep_impl:end