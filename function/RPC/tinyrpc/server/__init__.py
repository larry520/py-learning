
import zmq
import os
import traceback
import time
import logging
import ast
# from Tools import zmqports
from tinyrpc.exc import RPCError
from tinyrpc.transports.zmq import ZmqServerTransport
import tinyrpc
from loggers import events
from loggers import levels

class RPCServer(object):
    """High level RPC server.

    :param transport: The :py:class:`~tinyrpc.transports.RPCTransport` to use.
    :param protocol: The :py:class:`~tinyrpc.RPCProtocol` to use.
    :param dispatcher: The :py:class:`~tinyrpc.dispatch.RPCDispatcher` to use.
    """

    heartbeat_at = 0 # When to send HEARTBEAT (relative to time.time(), so in seconds)

    def __init__(self, port, protocol, dispatcher, reporters):
        self.protocol = protocol
        self.dispatcher = dispatcher

        self.ctx = zmq.Context()
        self.frontend = self.ctx.socket(zmq.ROUTER)
        self.reporters = reporters
        self.frontend.bind("tcp://*:" + str(port))
        self.transport = ZmqServerTransport(self.frontend)
        print("Create zmq ROUTER at: " + "tcp://*:" + str(port))
        self.poller = zmq.Poller()
        self.poller.register(self.frontend, zmq.POLLIN)
        self.serving = True

        
    def shutdown(self):
        if not self.frontend.closed:
            self.frontend.setsockopt(zmq.LINGER, 0)
            self.frontend.close()

    def broadcast(self, msg):
        self.reporters.publisher.publish(msg,level=levels.REPORTER)
        self.heartbeat_at = time.time() + tinyrpc.HEARTBEAT_INTERVAL

    def handle_message(self, context, msg):
        request = None
        try:
            request = self.protocol.parse_request(msg)
            if request.method=='::stop::':
                response = self.protocol.stop_respond()
                self.reporters.publisher.publish('STOPPING','server_loop')
                self.serving = False
                return response
            response = self.dispatcher.dispatch(request)
        except RPCError as e:
            print(e.message, os.linesep, traceback.format_exc())
            response = request.error_respond(e)
        return response

    def serve_forever(self):
        self.heartbeat_at = time.time() + tinyrpc.HEARTBEAT_INTERVAL
        while self.serving:
            socks = dict(self.poller.poll(tinyrpc.HEARTBEAT_INTERVAL * 1000))
            if socks.get(self.frontend) == zmq.POLLIN:
                context, r_req = self.transport.receive_message()
                msg = str(ast.literal_eval(str(r_req, encoding="utf-8")))
                self.reporters.logReporter.opt_report(events.SYS_LOG, data="< REQ > " + str(msg))

                response = self.handle_message(context, r_req)
                s_rep = response.serialize()
                msg = str(ast.literal_eval(str(s_rep, encoding="utf-8")))
                self.reporters.logReporter.opt_report(events.SYS_LOG, data="< REP > " + str(msg))
                self.transport.send_reply(context, s_rep)
            t_now = time.time()
            if t_now >= self.heartbeat_at:
                self.broadcast(tinyrpc.FCT_HEARTBEAT)

        self.shutdown()



