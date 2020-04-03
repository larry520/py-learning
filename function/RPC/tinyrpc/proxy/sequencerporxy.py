
import zmq

from .rpcproxy import RPCProxy
from tinyrpc.protocols.sequencerrpc import SequencerRPCProtocol
from tinyrpc.transports.zmq import ZmqClientTransport
# from Tools import zmqports
from tinyrpc.protocols.jsonrpc import JSONRPCTimeoutError

class SequencerProxy(RPCProxy):

    #timeout in seconds
    def __init__(self, site, publisher, url=None, retries=2, timeout=1, ctx=None):
        if not url:
            url = "tcp://127.0.0.1"
        if not ctx:
            ctx = zmq.Context.instance()
        super(SequencerProxy, self).__init__(ZmqClientTransport.create(ctx, url + ':' + str(zmqports.getZmqPortByModuleSlots("SEQUENCER_PORT") + site)),
                                      SequencerRPCProtocol(),
                                      publisher,
                                      retries)
        self.identity = 'SequencerProxy'
        # self.report_port = zmqports.get_zmq_port("SEQUENCER_PUB") + site
        # self.report_url = url
        # self.report = None
        # self.report_listener = None

    def send_cmd(self, function, params, timeout=3000):
        req = self.protocol.create_request(function, params)
        response = self.send_request(req, timeout)
        # if response is None:
        #     raise JSONRPCTimeoutError('time out calling ' + function + '('
        #                               + str(params) + ')')
        return response
