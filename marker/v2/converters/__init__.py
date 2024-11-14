from typing import Optional

from pydantic import BaseModel

from marker.v2.util import assign_config


class BaseConverter:
    def __init__(self, config: Optional[BaseModel | dict] = None):
        assign_config(self, config)

    def __call__(self, *args, **kwargs):
        raise NotImplementedError