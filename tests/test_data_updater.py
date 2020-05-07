import os
import shutil
import json
import pytest
from src.data_updater import DataUpdater
from src.lib.json_checker import JsonChecker


@pytest.fixture(scope="function", autouse=True)
def du_object():
    target_path = os.path.join(
        os.getcwd(), "tests", "data", "update_check.json")
    jc = JsonChecker()
    new_obj = jc.read_json(target_path)
    du = DataUpdater(target_path)
    yield du, new_obj, target_path
    text = json.dumps(new_obj, indent=4, ensure_ascii=False)
    with open(target_path, "wb") as f:
        f.write(text.encode('utf-8', "ignore"))


class TestDataUpdater:
    def test_update_data(self, capsys, du_object):
        new_obj = du_object[1].copy()
        du_object[0].update_data(new_obj)
        captured = capsys.readouterr()
        assert captured.out == "not updated\n"

    def test_update_data_create(self, capsys, du_object):
        new_obj = du_object[1].copy()
        new_obj['patients']['data'] = list(new_obj['patients']['data'][0])
        du_object[0].update_data(new_obj)
        captured = capsys.readouterr()
        assert captured.out == "create new data\n"

    # def test_update_data_create_new(self, capsys, du_object):
    #     new_obj = du_object[1].copy()
    #     os.remove(du_object[2])
    #     du_object[0].update_data(new_obj)
    #     captured = capsys.readouterr()
    #     assert captured.out == "create new data\n"
