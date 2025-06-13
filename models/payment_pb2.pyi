from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PayRequest(_message.Message):
    __slots__ = ("card_number", "event_id", "user_id", "amount")
    CARD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    card_number: int
    event_id: int
    user_id: int
    amount: float
    def __init__(self, card_number: _Optional[int] = ..., event_id: _Optional[int] = ..., user_id: _Optional[int] = ..., amount: _Optional[float] = ...) -> None: ...

class PayReply(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: bool
    def __init__(self, status: bool = ...) -> None: ...
