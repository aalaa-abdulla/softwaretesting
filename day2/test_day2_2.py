# test_exercise.py

 

import pytest

import json

from myenv.day2.day2_2 import load_config, validate_config

 

 

# 1. Use tmp_path to create a config.json and verify load_config reads it

def test_load_config_reads_file(tmp_path):
    d = tmp_path / "config.json"
    data = {"port": 8080, "host": "localhost", "debug": True}
    d.write_text(json.dumps(data))
    
    config = load_config(str(d))
    assert config["port"] == 8080
    assert config["host"] == "localhost"
 

 

# 2. Use tmp_path + monkeypatch to verify ENV vars override the file values



def test_env_overrides(tmp_path, monkeypatch):
    d = tmp_path / "config.json"
    data = {"port": 80, "host": "localhost", "debug": False}
    d.write_text(json.dumps(data))
    
    # Use monkeypatch to simulate shell environment variables
    monkeypatch.setenv("APP_PORT", "9090")
    monkeypatch.setenv("APP_DEBUG", "true")
    
    config = load_config(str(d))
    assert config["port"] == 9090
    assert config["debug"] is True
 

 

# 3. Use parametrize to test validate_config with at least 4 different configs

# Hint: @pytest.mark.parametrize("config, expected_errors", [...])


@pytest.mark.parametrize("config, expected_errors", [
    ({"port": 8080, "host": "localhost", "debug": True}, []),           # Valid
    ({"port": 99999, "host": "localhost", "debug": True}, ["invalid port"]), # Invalid port
    ({"port": 80, "debug": True}, ["missing host"]),                    # Missing host
    ({"port": 80, "host": "localhost", "debug": "yes"}, ["debug must be bool"]), # Bad debug
])
def test_validate_config(config, expected_errors):
    assert validate_config(config) == expected_errors