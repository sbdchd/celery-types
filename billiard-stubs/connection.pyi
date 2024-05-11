from _typeshed import Incomplete

__all__ = ['Client', 'Listener', 'Pipe', 'wait']

class _SocketContainer:
    sock: Incomplete
    def __init__(self, sock) -> None: ...

class _ConnectionBase:
    def __init__(self, handle, readable: bool = True, writable: bool = True) -> None: ...
    def __del__(self) -> None: ...
    @property
    def closed(self): ...
    @property
    def readable(self): ...
    @property
    def writable(self): ...
    def fileno(self): ...
    def close(self) -> None: ...
    def send_bytes(self, buf, offset: int = 0, size: Incomplete | None = None) -> None: ...
    def send(self, obj) -> None: ...
    def recv_bytes(self, maxlength: Incomplete | None = None): ...
    def recv_bytes_into(self, buf, offset: int = 0): ...
    def recv(self): ...
    def poll(self, timeout: float = 0.0): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...
    def send_offset(self, buf, offset): ...
    def setblocking(self, blocking) -> None: ...

class PipeConnection(_ConnectionBase): ...
class Connection(_ConnectionBase): ...

class Listener:
    def __init__(self, address: Incomplete | None = None, family: Incomplete | None = None, backlog: int = 1, authkey: Incomplete | None = None) -> None: ...
    def accept(self): ...
    def close(self) -> None: ...
    address: Incomplete
    last_accepted: Incomplete
    def __enter__(self): ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: types.TracebackType | None) -> None: ...

def Client(address, family: Incomplete | None = None, authkey: Incomplete | None = None): ...
def Pipe(duplex: bool = True, rnonblock: bool = False, wnonblock: bool = False): ...

class SocketListener:
    def __init__(self, address, family, backlog: int = 1) -> None: ...
    def accept(self): ...
    def close(self) -> None: ...

class ConnectionWrapper:
    def __init__(self, conn, dumps, loads) -> None: ...
    def send(self, obj) -> None: ...
    def recv(self): ...

class XmlListener(Listener):
    def accept(self): ...

def wait(object_list, timeout: Incomplete | None = None): ...
