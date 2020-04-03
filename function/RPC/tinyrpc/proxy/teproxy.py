__author__ = 'wei'

import zmq
import logging

from .rpcproxy import RPCProxy
from tinyrpc.protocols.jsonrpc import JSONRPCTimeoutError
from tinyrpc.protocols.terpc import TERPCProtocol
from tinyrpc.transports.zmq import ZmqClientTransport
#from config import zmqports


class TEProxy(RPCProxy):

    #timeout in seconds
    def __init__(self, port,site, reporters, url='tcp://localhost', retries=2, timeout=1, ctx=None):
        if not ctx:
            ctx = zmq.Context.instance()
        self.identity = 'TEProxy'
        super(TEProxy, self).__init__(ZmqClientTransport.create(ctx, url + ':' + str(port + site),self.identity),
                                      TERPCProtocol(),
                                      reporters,
                                      retries)

        self.debugMode = True if timeout == -1 else False


    def send_test(self, test_item):
        test_dict = test_item._to_dict()
        req = self.protocol.create_request(test_dict['function'], test_dict['params'], test_item.unit, test_item.timeout)

        # Debug mode
        if self.debugMode:
            response = self.send_request(req, -1)
        else:
            response = self.send_request(req, test_item.timeout)
        if response is None:
            raise JSONRPCTimeoutError('time out calling ' + test_item.function + '('
                                      + str(test_dict['params']) + ')')
        return response

    def send_cmd(self, func, params, unit='', timeout=3000):
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