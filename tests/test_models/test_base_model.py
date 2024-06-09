#!/usr/bin/python3
"""Base Model Test Module"""


import unittest
from models.base_model import BaseModel
import os
import json


class TestBaseModel(unittest.TestCase):
    """
    A set of unittests to validate the base model attributes and methods
    """
    model_1 = BaseModel()
    model_2 = BaseModel()
    model_3 = BaseModel()
    model_4 = BaseModel()
    model_5 = BaseModel()

    def test_initialization(self):
        self.assertEqual(self.model_1.__class__.__name__, "BaseModel")
        self.assertEqual(self.model_2.__class__.__name__, "BaseModel")
        self.assertEqual(self.model_3.__class__.__name__, "BaseModel",)
        self.assertEqual(self.model_1.created_at, self.model_1.updated_at)
        self.assertEqual(self.model_2.created_at, self.model_2.updated_at)
        self.assertEqual(self.model_3.created_at, self.model_3.updated_at)
        self.assertNotEqual(self.model_1.id, self.model_2.id)
        self.assertNotEqual(self.model_1.id, self.model_3.id)
        self.assertNotEqual(self.model_2.id, self.model_3.id)

    def test_to_dict(self):
        self.model_1.name = "AirBnB"
        self.model_1.price = 89
        self.info = self.model_1.to_dict()
        self.assertEqual(self.model_1.__dict__['name'], self.info['name'])
        self.assertEqual(self.model_1.__dict__['price'], self.info['price'])
        self.assertEqual(self.info['__class__'], "BaseModel")

    def test_save(self):
        self.model_2.save()
        self.assertNotEqual(self.model_2.created_at, self.model_2.updated_at)

    def test_string(self):
        self.assertEqual(type(self.model_3.__str__()), type("string"))
        self.assertEqual(self.model_3.__str__()[1:10], "BaseModel")
        self.assertRegex(self.model_3.__str__(), "created_at")
        self.assertRegex(self.model_3.__str__(), "updated_at")
        self.assertRegex(self.model_3.__str__(), "id")

    def test_to_class(self):
        self.model_4.name = "AirBnB"
        self.model_4.price = 89
        self.model_5 = BaseModel(**self.model_4.to_dict())

        self.assertEqual(self.model_5.name, self.model_4.__dict__['name'])
        self.assertEqual(self.model_4.price, self.model_4.price)
        self.assertEqual(self.model_4.created_at, self.model_4.created_at)
        self.assertEqual(self.model_4.updated_at, self.model_4.updated_at)
        self.assertEqual(self.model_4.id, self.model_5.id)

    def test_storage(self):
        b = BaseModel()
        b.save()
        key = "{}.{}".format(type(b).__name__, b.id)
        d = {key: b.to_dict()}
        self.assertTrue(os.path.isfile("file.json"))
        with open("file.json",
                  "r", encoding="utf-8") as f:
            self.assertEqual(len(f.read()), len(json.dumps(d)))
            f.seek(0)
            self.assertEqual(json.load(f), d)


if __name__ == "__main__":
    unittest.main()
