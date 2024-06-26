__all__ = ["BaseProcess", "Process"]

class BaseProcess:
    def __init__(
        self,
    ) -> None: ...
    def run(self) -> None: ...
    def start(self) -> None: ...
    def close(self) -> None: ...
    def terminate(self) -> None: ...
    def terminate_controlled(self) -> None: ...

class AuthenticationString(bytes): ...

class _MainProcess(BaseProcess):
    def __init__(self) -> None: ...

Process = BaseProcess
