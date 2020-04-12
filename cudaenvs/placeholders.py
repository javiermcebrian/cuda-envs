from pathlib import Path
import click
import json
import os
import ast
from typing import List, Tuple


class User(object):

    def __init__(self, user_name: str, user_id: str, group_name: str, group_id: str):
        self.user_name = user_name
        self.user_id = user_id
        self.group_name = group_name
        self.group_id = group_id


class Volume(object):

    def __init__(self, host: str, container: str):
        self.host = host
        self.container = container


class Environment(object):

    def __init__(self, user: User, image_name: str, volumes: List[Volume], context: Path, cuda_tag: str):
        self.user = user
        self.image_name = image_name
        self.volumes = volumes
        self.context = context
        self.cuda_tag = cuda_tag


class Zoo(object):

    def __init__(self):
        self.cudaenvs_fn = Path(__file__).parent / 'resources/cudaenvs.cfg'
    
    def __read_cudaenvs(self):
        with self.cudaenvs_fn.open('r') as f:
            return json.load(f)
    
    def __write_cudaenvs(self, cudaenvs):
        with self.cudaenvs_fn.open('w') as f:
            json.dump(cudaenvs, f, indent=4)
    
    @staticmethod
    def get_config_type(is_default: bool):
        if isinstance:
            return 'default'
        else:
            return 'environments'

    def remove(self, is_default: bool, keys: Tuple[str]):
        cudaenvs = self.__read_cudaenvs()
        config_type = self.get_config_type(is_default=is_default)
        keys = list(keys)
        if not len(keys):
            keys = cudaenvs[config_type].keys()
        removed = [cudaenvs[config_type].pop(k, None) for k in keys]
        removed = list(filter(None, removed))
        self.__write_cudaenvs(cudaenvs=cudaenvs)
        return removed
    
    def dump(self):
        return json.dumps(self.__read_cudaenvs(), indent=4)
