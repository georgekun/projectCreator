import os
import shutil
import pytest

from core.make_project import MakeProject


test_data_from_yaml_file = {
    'src': {
        'domains': {
            'entities': {'entity_1.py': None}
        },
        'use_cases': {'entity_create_use_case.py': None},
        'drivers': {
            'fastapi': {
                'app.py': None,
                'main.py': None,
                'routers': {
                    'v1': {'handlers': None, 'routes': None, 'all_routes.py': None},
                    'v2': {'handlers': None, 'routes': None, 'all_routes.py': None}
                }
            }
        },
        ".dockerfile": None,
        'adapters': {
            'repo': {
                'abstract_repo': {'non_abstract_repo.py': None}
            }
        },
        'ports': {'abstract_repo.py': None},
        'tests': {'conf_test.py': None}
    },
    'docker-compose.yml': None,
    'requirements.txt': None
}


@pytest.fixture(scope="module")
def setup_project():
    temp_dir = 'tmp'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.mkdir(temp_dir)
    
    yield temp_dir 
    shutil.rmtree(temp_dir)


def test_create_project(setup_project):
  
    project_dir = 'tmp'
    mp = MakeProject(project_dir)
    mp.create_project(test_data_from_yaml_file)
    
    assert os.path.exists(os.path.join(project_dir, 'src', 'domains', 'entities', 'entity_1.py'))
    assert os.path.exists(os.path.join(project_dir, 'src', 'use_cases', 'entity_create_use_case.py'))
    assert os.path.exists(os.path.join(project_dir, 'src', 'drivers', 'fastapi', 'app.py'))
    assert os.path.exists(os.path.join(project_dir, 'src', 'drivers', 'fastapi', 'main.py'))
    assert os.path.exists(os.path.join(project_dir, 'src', 'drivers', 'fastapi', 'routers', 'v1', 'all_routes.py'))
    assert os.path.exists(os.path.join(project_dir, 'src', 'drivers', 'fastapi', 'routers', 'v2', 'all_routes.py'))
    assert os.path.exists(os.path.join(project_dir, 'src', 'adapters', 'repo', 'abstract_repo', 'non_abstract_repo.py'))
    assert os.path.exists(os.path.join(project_dir, 'src', 'ports', 'abstract_repo.py'))
    assert os.path.exists(os.path.join(project_dir, 'src', 'tests', 'conf_test.py'))
    assert os.path.exists(os.path.join(project_dir, 'docker-compose.yml'))
    assert os.path.exists(os.path.join(project_dir, 'requirements.txt'))
    assert os.path.isfile(os.path.join(project_dir, "src", ".dockerfile"))

