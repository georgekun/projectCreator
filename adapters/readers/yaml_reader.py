import yaml

from ports.reader import FileReader    
    
    
class YamlReader(FileReader):
    
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
    
    def read(self) -> dict:
        with open(self.file_path, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)
        return data
    
    def write(self) -> None:
        pass
    
    