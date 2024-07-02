from adapters.readers.yaml_reader import YamlReader

output_data = {
    "src": {
        "domains": None, 
        "tests": {
            "entity.py": None
        },
        "main.py": None
    }
}

def test_yaml_reader():
    reader = YamlReader('./tests/test.yml')
    result_data = reader.read()
    assert output_data == result_data
    