from _typeshed import Incomplete
from senml.senml_base import SenmlBase as SenmlBase
from senml.senml_record import SenmlRecord as SenmlRecord

class SenmlPackIterator:
    _list: Incomplete
    _index: int
    def __init__(self, list) -> None: ...
    def __iter__(self): ...
    def __next__(self): ...

class SenmlPack(SenmlBase):
    json_mappings: Incomplete
    _data: Incomplete
    name: Incomplete
    _base_value: Incomplete
    _base_time: Incomplete
    _base_sum: Incomplete
    base_unit: Incomplete
    _parent: Incomplete
    actuate: Incomplete
    def __init__(self, name, callback: Incomplete | None = ...) -> None: ...
    def __iter__(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    @property
    def base_value(self): ...
    @base_value.setter
    def base_value(self, value) -> None: ...
    @property
    def base_sum(self): ...
    @base_sum.setter
    def base_sum(self, value) -> None: ...
    @property
    def base_time(self): ...
    @base_time.setter
    def base_time(self, value) -> None: ...
    def _check_value_type(self, value, field_name) -> None: ...
    def from_json(self, data) -> None: ...
    def _process_incomming_data(self, records, naming_map) -> None: ...
    def do_actuate(self, raw, naming_map, device: Incomplete | None = ...) -> None: ...
    def to_json(self): ...
    def _build_rec_dict(self, naming_map, appendTo) -> None: ...
    def from_cbor(self, data) -> None: ...
    def to_cbor(self): ...
    def add(self, item) -> None: ...
    def remove(self, item) -> None: ...
    def clear(self) -> None: ...
