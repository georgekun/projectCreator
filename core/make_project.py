import os
import re


class MakeProject:

    def __init__(self, destination_path: str = '.') -> None:
        self.destination_path = destination_path
        
    def create_project(self, data: dict, current_path: str | None = None):
        if not current_path:
            current_path = self.destination_path
            
        for key, value in data.items():
            path = os.path.join(current_path, key)
            if not value:
                self.create_file_object(path)
            else:
                self.create_file_object(path)
                self.create_project(value, path)
        return os.path.abspath(self.destination_path)
    
    def create_file_object(self, file_object_name: str):
        if self.match_file(file_object_name):
            self.create_file(file_object_name)
        else:
            self.create_dir(file_object_name)
                
    def match_file(self, file_name: str) -> bool :
        base_name = os.path.basename(file_name)
        if base_name.startswith("."):
            return True
        if re.match(r'^[A-Za-z0-9_-]+\.[A-Za-z]{1,10}$', base_name):
            return True
        return False
    
    def create_dir(self, name: str):
        os.makedirs(name, exist_ok=True)
    
    def create_file(self, name: str):
        with open(name, 'w'): pass
