import os
import argparse

from core.make_project import MakeProject
from adapters.readers.yaml_reader import YamlReader


def main():
    parser = argparse.ArgumentParser(description='Create project from YAML file.')

    parser.add_argument('action', choices=['createproject'], help='Action to perform')
    parser.add_argument('--plaintext', dest='yaml_path', required=True, help='Path to the YAML file')
    parser.add_argument('--dest', dest='dest_path', required=True, help='Destination path')

    args = parser.parse_args()

    if args.action == 'createproject':
        if str(args.yaml_path).startswith("~"):
            abs_yaml_path = os.path.expanduser(args.yaml_path)
        else:
            abs_yaml_path = os.path.abspath(args.yaml_path)
            
        if str(args.dest_path).startswith("~"):
            abs_dest_path = os.path.abspath(args.dest_path)
        else:
            abs_dest_path = os.path.abspath(args.dest_path)
            
        reader = YamlReader(abs_yaml_path)
        data = reader.read()
        creator = MakeProject(abs_dest_path)
        path = creator.create_project(data)
        
        print(f"project created: {path}")
