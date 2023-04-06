import os
import configparser
import base64
import json

from script import get_params


def test_get_params_with_args():
    args = ['-u', 'testuser', '-v', 'testvault', '-k', 'testkey', '-b', 'eyJ0ZXN0MSI6InRlc3R1c2VyMSIsInRlc3QyIjoidGVzdHZhdWx0MiJ9', '-f', 'testfile']
    parsed_args = get_params(args)
    assert parsed_args.username == 'testuser'
    assert parsed_args.vault_env == 'testvault'
    assert parsed_args.vault_key == 'testkey'
    assert parsed_args.b64_string == 'eyJ0ZXN0MSI6InRlc3R1c2VyMSIsInRlc3QyIjoidGVzdHZhdWx0MiJ9'
    assert parsed_args.filename == 'testfile'


def test_get_params_with_config_file():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {
        'APP_ENV': 'testapp',
        'FILENAME': 'testfile',
        'FILE_PATH': '/test/path'
    }
    with open('config.cfg', 'w') as configfile:
        config.write(configfile)

    args = ['-u', 'testuser', '-v', 'testvault', '-k', 'testkey', '-b', 'eyJ0ZXN0MSI6InRlc3R1c2VyMSIsInRlc3QyIjoidGVzdHZhdWx0MiJ9']
    parsed_args = get_params(args)
    assert parsed_args.username == 'testuser'
    assert parsed_args.vault_env == 'testvault'
    assert parsed_args.vault_key == 'testkey'
    assert parsed_args.b64_string == 'eyJ0ZXN0MSI6InRlc3R1c2VyMSIsInRlc3QyIjoidGVzdHZhdWx0MiJ9'
    assert parsed_args.filename == 'testfile'
    assert parsed_args.file_path == '/test/path'
    assert parsed_args.app_env == 'testapp'

    os.remove('config.cfg')


def test_get_params_with_env_vars():
    os.environ['USERNAME'] = 'testuser'
    os.environ['VAULT_ENV'] = 'testvault'
    os.environ['VAULT_KEY'] = 'testkey'
    os.environ['B64_STRING'] = 'eyJ0ZXN0MSI6InRlc3R1c2VyMSIsInRlc3QyIjoidGVzdHZhdWx0MiJ9'
    os.environ['FILENAME'] = 'testfile'
    os.environ['FILE_PATH'] = '/test/path'
    os.environ['APP_ENV'] = 'testapp'

    parsed_args = get_params([])
    assert parsed_args.username == 'testuser'
    assert parsed_args.vault_env == 'testvault'
    assert parsed_args.vault_key == 'testkey'
    assert parsed_args.b64_string == 'eyJ0ZXN0MSI6InRlc3R1c2VyMSIsInRlc3QyIjoidGVzdHZhdWx0MiJ9'
    assert parsed_args.filename == 'testfile'
    assert parsed_args.file_path == '/test/path'
    assert parsed_args.app_env == 'testapp'

    os.environ.pop('USERNAME')
    os.environ.pop('VAULT_ENV')
    os.environ.pop('VAULT_KEY')
    os.environ.pop('B64_STRING
