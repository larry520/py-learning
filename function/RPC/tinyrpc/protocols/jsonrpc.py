#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import RPCBatchProtocol, RPCRequest, RPCResponse, RPCErrorResponse,\
               InvalidRequestError, MethodNotFoundError, ServerError,\
               InvalidReplyError, RPCError, RPCBatchRequest, RPCBatchResponse
               
from uuid import uuid1

import json

SERVER_READY = '_my_rpc_server_is_ready'

class FixedErrorMessageMixin(object):
    def __init__(self, *args, **kwargs):
        if not args:
            args = [self.message]
        super(FixedErrorMessageMixin, self).__init__(*args, **kwargs)

    def error_respond(self):
        response = JSONRPCResponse()

        response.result = self.message
        response.unique_id = None
        response.errorCode = self.jsonrpc_error_code
        return response

    
class JSONRPCParseError(FixedErrorMessageMixin, InvalidRequestError):
    jsonrpc_error_code = -32700
    message = 'Parse error'

class JSONRPCInvalidRequestError(FixedErrorMessageMixin, InvalidRequestError):

    jsonrpc_error_code = -32600
    message = 'Invalid Request: '
    def __init__(self, msg=''):
        super(JSONRPCInvalidRequestError, self).__init__()
        if msg:
            self.message = msg

class JSONRPCMethodNotFoundError(FixedErrorMessageMixin, MethodNotFoundError):
    jsonrpc_error_code = -32601
    message = 'Method not found'
    def __init__(self, msg=''):
        super(JSONRPCMethodNotFoundError, self).__init__()
        if msg:
            self.message = msg


class JSONRPCInvalidParamsError(FixedErrorMessageMixin, InvalidRequestError):
    jsonrpc_error_code = -32602
    message = 'Invalid params'
    def __init__(self, msg=''):
        super(JSONRPCInvalidParamsError, self).__init__()
        if msg:
            self.message = msg

class JSONRPCInternalError(FixedErrorMessageMixin, InvalidRequestError):
    jsonrpc_error_code = -32603
    message = 'Internal error'

class JSONRPCServerStopError(FixedErrorMessageMixin, ServerError):
    jsonrpc_error_code = -32604
    message = "Server Stop Requested"

class JSONRPCTimeoutError(FixedErrorMessageMixin, RPCError):
    jsonrpc_error_code = -32610
    message = 'Timed out'
    def __init__(self, msg=''):
        super(JSONRPCTimeoutError, self).__init__()
        if msg:
            self.message = msg

class JSONRPCServerError(FixedErrorMessageMixin, InvalidRequestError):
    jsonrpc_error_code = -32000
    message = ''
    def __init__(self, msg=''):
        super(JSONRPCServerError, self).__init__()
        if msg:
            self.message = msg

class JSONRPCPluginError(FixedErrorMessageMixin, InvalidRequestError):
    jsonrpc_error_code = -32620
    message = ''
    def __init__(self, msg=''):
        super(JSONRPCPluginError, self).__init__()
        if msg:
            self.message = msg

class JSONRPCResponse(RPCResponse):
    def _to_dict(self):
        return {
            'method' : self.method,
            'jsonrpc' : JSONRPCProtocol.JSON_RPC_VERSION,
            'id': self.unique_id,
            'result': self.result,
            'errorCode':self.errorCode
        }

    def serialize(self):
        return json.dumps(self._to_dict()).encode("utf-8")

def _get_code_and_message(error):
    assert isinstance(error, (Exception, str))
    if isinstance(error, Exception):
        if hasattr(error, 'jsonrpc_error_code'):
            code = error.jsonrpc_error_code
            msg = str(error)
        elif isinstance(error, InvalidRequestError):
            code = JSONRPCInvalidRequestError.jsonrpc_error_code
            msg = JSONRPCInvalidRequestError.message
        elif isinstance(error, MethodNotFoundError):
            code = JSONRPCMethodNotFoundError.jsonrpc_error_code
            msg = JSONRPCMethodNotFoundError.message
        else:
            # allow exception message to propagate
            code = JSONRPCServerError.jsonrpc_error_code
            msg = str(error)
    else:
        code = -32000
        msg = error

    return code, msg

class JSONRPCRequest(RPCRequest):
    def error_respond(self, error):
        if not self.unique_id:
            return None

        response = JSONRPCResponse()

        response.errorCode = error.jsonrpc_error_code

        response.result = error.message
        response.unique_id = self.unique_id
        #response._jsonrpc_error_code = error.jsonrpc_error_code
        response.method = self.method
        
        return response

    def respond(self, result):
        response = JSONRPCResponse()

        if not self.unique_id:
            return None
        response.errorCode = result[0]
        response.result = result[1]
        response.unique_id = self.unique_id
        response.method = self.method

        return response

    def __eq__(self, other):
        if self.method != other.method:
            return False

        if self.args != other.args:
            return False

        if self.kwargs != other.kwargs:
            return False

        if self.version != other.version:
            return False

        return True

    def serialize(self):
        return json.dumps(self._to_dict())


class JSONRPCProtocol(RPCBatchProtocol):
    JSON_RPC_VERSION = "2.0.01"

    _ALLOWED_REPLY_KEYS = sorted(['id', 'jsonrpc', 'method', 'errorCode', 'result'])
    _ALLOWED_REQUEST_KEYS = sorted(['id', 'jsonrpc', 'method', 'args', 'kwargs'])

    #change all unicode data back to ascii data
    def load_json(self, data):
        val = json.loads(data)
        return_val = {}
        for k, v in val.items():
            return_val[str(k)] = str(v)
        return return_val

    def _get_unique_id(self):
        return uuid1().hex
    
    def parse_request(self, data):
        try:
            req = json.loads(data.decode('utf-8'))
        except Exception as e:
            raise JSONRPCParseError()

        if isinstance(req, list):
            # batch request
            requests = None
            for subreq in req:
                try:
                    requests.append(self._parse_subrequest(subreq))
                except RPCError as e:
                    requests.append(e)
                except Exception as e:
                    requests.append(JSONRPCInvalidRequestError())

            if not requests:
                raise JSONRPCInvalidRequestError()
            return requests
        else:
            return self._parse_subrequest(req)


        return request

    def stop_respond(self):
        response = JSONRPCResponse()
        response.version = self.JSON_RPC_VERSION
        response.unique_id = '0'
        response.result = 'PASS'
        return response
