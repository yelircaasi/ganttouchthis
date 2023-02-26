import json
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Tuple, Union

from more_itertools import batched

from ganttouchthis.utils.date import Date


class Priority(Enum):
    UNDEFINED = -1
    FINISHED = 0
    BOTTOM = 1
    LOW = 2
    MEDIUM = 3
    HIGH = 4
    TOP = 5

    def __repr__(self) -> str:
        return f"{self.name} ({self.value}/5)"

    def __str__(self) -> str:
        return self.__repr__()


class Color(Enum):
    GRAY = -1
    BLUE = 0
    PURPLE = 1
    YELLOW = 2
    RED = 3
    GREEN = 4

    def __repr__(self) -> str:
        return f"{self.name}"

    def __str__(self) -> str:
        return self.__repr__()


@dataclass
class Task:
    name: str = ""
    subtasks: list = field(default_factory=list)
    duration_min: int = 30
    priority: Priority = Priority.UNDEFINED
    color: Color = Color.GRAY
    description: str = ""

    def __repr__(self) -> str:
        task_str = "\n    ".join(
            (
                f"    Name:        {self.name}",
                f"Subtasks:    {', '.join(self.subtasks)}",
                f"Duration:    {str(self.duration_min)} min",
                f"Priority:    {str(self.priority)}",
                f"Color:       {str(self.color)}",
                f"Description: {self.description}",
            )
        )
        return task_str

    def serialize(self, indent: Union[int, None] = None) -> str:
        return json.dumps(
            {k: str(v) if not isinstance(v, list) else v for k, v in self.__dict__.items()},
            indent=indent,
            ensure_ascii=False,
        )

    @classmethod
    def deserialize(cls, json_str: str) -> "Task":
        _dict = json.loads(json_str)
        _dict["duration_min"] = int(_dict["duration_min"])
        _dict["priority"] = Priority[_dict["priority"].split()[0]]
        _dict["color"] = Color[_dict["color"]]
        return cls(**_dict)


@dataclass
class DayTasks:
    tasks: List[Task]

    def __repr__(self) -> str:
        return "\n\n".join(map(str, self.tasks))

    def __str__(self) -> str:
        return self.__repr__()

    def serialize(self, indent: Union[int, None] = None) -> str:
        return "[\n\n\n" + "\n\n".join(map(lambda x: x.serialize(indent=indent), self.tasks)) + "\n\n\n]\n"

    @classmethod
    def deserialize(cls, json_str: str) -> "DayTasks":
        task_strings = json_str.split("\n\n\n")[1].split("\n\n")
        tasks = list(map(lambda x: Task.deserialize(x), task_strings))
        return cls(tasks=tasks)


def schedule_tasks(
    task_list: list,
    start: Date,
    end: Date,
    cluster: int,
    interval: Union[int, None],
    name: str,
    priority: Priority = Priority.UNDEFINED,
) -> dict:

    start = start if start else Date.today() + 1
    task_chunks = list(batched(task_list, cluster))
    nchunks = len(task_chunks)
    if end:
        ndays = int(end) - int(start)
        gap = int((ndays - nchunks) / (nchunks - 1))
    elif interval:
        gap = interval - 1
    else:
        raise ValueError("Invalid parameter configuration. Either `end` or `interval` must be specified.")

    def make_pair(enum_task_chunk: Tuple[int, list]) -> Tuple[Date, Task]:
        i, task_chunk = enum_task_chunk
        return (start + (i + i * gap), Task(name=name, subtasks=task_chunk, priority=priority))

    return dict(map(make_pair, enumerate(task_chunks)))
