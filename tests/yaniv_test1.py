import pytest

# https://stackoverflow.com/questions/63292928/add-pytest-fixtures-to-a-test-class-using-dependency-injection
# /63436993#63436993
from utils.excel_parser import ExcelParser
from utils.json_parser import JsonParser


def test1():
    print("666")
