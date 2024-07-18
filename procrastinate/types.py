from __future__ import annotations

import typing as t

from typing_extensions import NotRequired

JSONValue = t.Union[str, int, float, bool, None, t.Dict[str, t.Any], t.List[t.Any]]
JSONDict = t.Dict[str, JSONValue]


class TimeDeltaParams(t.TypedDict):
    weeks: NotRequired[int]
    days: NotRequired[int]
    hours: NotRequired[int]
    minutes: NotRequired[int]
    seconds: NotRequired[int]
    milliseconds: NotRequired[int]
    microseconds: NotRequired[int]
