from tinyrpc.proxy.rpcproxy import RPCProxy
from tinyrpc.transports.zmq import ZmqClientTransport
# from Tools import zmqports
import zmq
from tinyrpc.protocols.StateMachineRpc import StateMachineRPCProtocol


# from tinyrpc.protocols.smrpc import StateMachienRPCProtocol, StateMachineRPCRequest

class SMProxy(RPCProxy):

    #timeout in seconds
    def __init__(self, publisher, url='tcp://localhost', retries=2, ctx=None):
        if not ctx:
            ctx = zmq.Context()
        self.identity = 'SMProxy'
        super(SMProxy, self).__init__(ZmqClientTransport.create(ctx, url + ':' + str(zmqports.getZmqPortByModule("SM_PORT")),self.identity),
                                      StateMachineRPCProtocol(),
                                      publisher,
                                      retries)

        

    def send_cmd(self, event_name, event_data, timeout = 3000):
        req = self.protocol.create_request(event_name, event_data)
        response = self.send_request(req, timeout) 
        return response