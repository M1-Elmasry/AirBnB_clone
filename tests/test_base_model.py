#/usr/bin/python3
import unittest
import models
import os
from models.base_model import BaseModel
from time import sleep
from datetime import datetime

class test_inistaitiation(unittest.TestCase):
    """In case args = None
    """
    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_storing_new_instance(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_object_id_is_string(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_datetime_type(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_datetime_type(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_models_unique_id(self):
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_different_time_created_at(self):
        base_model_1 = BaseModel()
        sleep(0.06)
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.created_at, base_model_2.created_at)

    def test_different_time_updated_at(self):
        base_model_1 = BaseModel()
        sleep(0.06)
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.updated_at, base_model_2.updated_at)

    def test_unused_args(self):
        base_model = BaseModel(None)
        self.assertNotIn(None, base_model.__dict__.values())

    def test_str_repr(self):
        date_time = datetime.today() # As example
        date_time_repr = repr(date_time) # Date representation
        model = BaseModel() # Make an object
        model.id = "885520" # init an id
        model.created_at = date_time # init created at
        model.updated_at = date_time #init updated at
        model_string_rep = model.__str__() # string represetaion of model

        self.assertIn("[BaseModel] (885520)", model_string_rep)
        self.assertIn("'id': '885520'", model_string_rep)
        self.assertIn("'created_at': " + date_time_repr, model_string_rep)
        self.assertIn("'updated_at': " + date_time_repr, model_string_rep)

    """
    In case passed args are not non
    """



if __name__ == "__main__":
    unittest.main()