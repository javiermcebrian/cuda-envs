from pathlib import Path
import click
import json
import os
import ast
from typing import List, Tuple


class Environment(object):

    def __init__(self):
        self.cudaenvs_fn = Path(__file__).parent / 'resources/cudaenvs.cfg'
        self.__keys_main = ['user', 'image_name', 'cuda_tag', 'context', 'volumes']
        self.__keys_user = ['user_name', 'user_id', 'group_name', 'group_id']
        self.__keys_volume = ['host', 'container']
    
    def __read_cudaenvs(self):
        with self.cudaenvs_fn.open('r') as f:
            return json.load(f)
    
    def __write_cudaenvs(self, cudaenvs):
        with self.cudaenvs_fn.open('w') as f:
            json.dump(cudaenvs, f, indent=4)
    
    def __validate_params(self, env: dict):
        assert all([k in self.__keys_main for k in env.keys()]), f'Bad keys in main level of {env}'
        assert all([k in self.__keys_user for k in env.get('user', {}).keys()]), f'Bad keys in user level of {env}'
        assert all([k in self.__keys_volume for volume in env.get('volumes', []) for k in volume.keys()]), f'Bad keys in volumes level of {env}'
    
    @staticmethod
    def __get_config_type(is_default: bool):
        if isinstance:
            return 'default'
        else:
            return 'environments'
    
    def __merge_volumes(self, environment: dict, default: dict):
        volumes = environment.get('volumes', [])
        for vd in default.get('volumes', []):
            if all([vd['container'] != vh['container'] for vh in volumes]):
                volumes.append(vd)
        return volumes
    
    def update(self, updates_fn):
        # Read files
        cudaenvs = self.__read_cudaenvs()
        with updates_fn.open('r') as f:
            updates = json.load(f)
        # Check default and envs keys
        # Only check correctness, completeness will be checked when an environment is required
        default = updates.pop('default', {})
        environments = updates.pop('environments', {})
        self.__validate_params(env=default)
        [self.__validate_params(env=env) for env in environments.values()]
        # Update
        cudaenvs['default'].update(default)
        cudaenvs['environments'].update(environments)
        # Update file
        self.__write_cudaenvs(cudaenvs=cudaenvs)

    def remove(self, is_default: bool, keys: Tuple[str]):
        cudaenvs = self.__read_cudaenvs()
        config_type = self.__get_config_type(is_default=is_default)
        keys = list(keys)
        if not len(keys):
            keys = cudaenvs[config_type].keys()
        removed = [cudaenvs[config_type].pop(k, None) for k in keys]
        removed = list(filter(None, removed))
        self.__write_cudaenvs(cudaenvs=cudaenvs)
        return removed
    
    def list(self):
        return ' '.join(self.__read_cudaenvs()['environments'].keys())

    def dump(self):
        return json.dumps(self.__read_cudaenvs(), indent=4)

    def get_config(self, env_name: str):
        cudaenvs = self.__read_cudaenvs()
        assert env_name in cudaenvs['environments'].keys(), 'Bad environment name provided'
        environment = cudaenvs['environments'][env_name]
        default = cudaenvs['default']
        config = {
            'user': {**default.get('user', {}), **environment.get('user', {})},
            'image_name': environment.get('image_name', default.get('image_name', None)),
            'cuda_tag': environment.get('cuda_tag', default.get('cuda_tag', None)),
            'context': environment.get('context', default.get('context', None)),
            'volumes': self.__merge_volumes(environment=environment, default=default)
        }
        # Check config completenes
        assert config['user'].keys() == self.__keys_user, 'Missing user params'
        assert config['image_name'] is not None, 'Missing image_name'
        assert config['cuda_tag'] is not None, 'Missing cuda_tag'
        assert config['context'] is not None, 'Missing context'
        return config
