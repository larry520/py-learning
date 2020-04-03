import zmq
import logging
from tinyrpc.proxy.rpcproxy import RPCProxy
from tinyrpc.protocols.jsonrpc import JSONRPCTimeoutError
from tinyrpc.protocols.terpc import TERPCProtocol
from tinyrpc.transports.zmq import ZmqClientTransport
# from Tools import zmqports


class dotProxy(RPCProxy):

    #timeout in seconds
    def __init__(self,reqPort,identity, site, reporters, url='tcp://localhost', retries=2, timeout=1, ctx=None):
        if not ctx:
            ctx = zmq.Context.instance()
        super(dotProxy, self).__init__(ZmqClientTransport.create(ctx, url + ':' + str(reqPort + site),identity),
                                      TERPCProtocol(),
                                       reporters,
                                      retries)
        self.identity = identity
        self.debugMode = True if timeout == -1 else False

    def send_REQ(self, func, params, unit='', timeout=3000):
        req = self.protocol.create_request(func, params, unit, timeout)
#         logging.info("send msg to engine is " + str(req.serialize()))

        # Debug mode
        if self.debugMode:
            response = self.send_request(req, -1)
        else:
            response = self.send_request(req, timeout)

        if response is None:
            raise JSONRPCTimeoutError('time out calling ' + func + '('
                                      + str(params) + ')')
        return response
