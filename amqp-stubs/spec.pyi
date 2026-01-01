from typing import NamedTuple

class method_t(NamedTuple):
    method_sig: tuple[int, int]
    args: str | None
    content: bool

def method(
    method_sig: tuple[int, int], args: str | None = ..., content: bool = ...
) -> method_t: ...

class Connection:
    CLASS_ID: int
    Start: tuple[int, int]
    StartOk: tuple[int, int]
    Secure: tuple[int, int]
    SecureOk: tuple[int, int]
    Tune: tuple[int, int]
    TuneOk: tuple[int, int]
    Open: tuple[int, int]
    OpenOk: tuple[int, int]
    Close: tuple[int, int]
    CloseOk: tuple[int, int]
    Blocked: tuple[int, int]
    Unblocked: tuple[int, int]

class Channel:
    CLASS_ID: int
    Open: tuple[int, int]
    OpenOk: tuple[int, int]
    Flow: tuple[int, int]
    FlowOk: tuple[int, int]
    Close: tuple[int, int]
    CloseOk: tuple[int, int]

class Exchange:
    CLASS_ID: int
    Declare: tuple[int, int]
    DeclareOk: tuple[int, int]
    Delete: tuple[int, int]
    DeleteOk: tuple[int, int]
    Bind: tuple[int, int]
    BindOk: tuple[int, int]
    Unbind: tuple[int, int]
    UnbindOk: tuple[int, int]

class Queue:
    CLASS_ID: int
    Declare: tuple[int, int]
    DeclareOk: tuple[int, int]
    Bind: tuple[int, int]
    BindOk: tuple[int, int]
    Unbind: tuple[int, int]
    UnbindOk: tuple[int, int]
    Purge: tuple[int, int]
    PurgeOk: tuple[int, int]
    Delete: tuple[int, int]
    DeleteOk: tuple[int, int]

class Basic:
    CLASS_ID: int
    Qos: tuple[int, int]
    QosOk: tuple[int, int]
    Consume: tuple[int, int]
    ConsumeOk: tuple[int, int]
    Cancel: tuple[int, int]
    CancelOk: tuple[int, int]
    Publish: tuple[int, int]
    Return: tuple[int, int]
    Deliver: tuple[int, int]
    Get: tuple[int, int]
    GetOk: tuple[int, int]
    GetEmpty: tuple[int, int]
    Ack: tuple[int, int]
    Reject: tuple[int, int]
    RecoverAsync: tuple[int, int]
    Recover: tuple[int, int]
    RecoverOk: tuple[int, int]
    Nack: tuple[int, int]

class Tx:
    CLASS_ID: int
    Select: tuple[int, int]
    SelectOk: tuple[int, int]
    Commit: tuple[int, int]
    CommitOk: tuple[int, int]
    Rollback: tuple[int, int]
    RollbackOk: tuple[int, int]

class Confirm:
    CLASS_ID: int
    Select: tuple[int, int]
    SelectOk: tuple[int, int]
