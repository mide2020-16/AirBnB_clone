import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.city import City
from models.state import State

class TestModels(unittest.TestCase):
    """Test cases for the models."""

    def test_base_model(self):
        """Test cases for BaseModel."""
        model1 = BaseModel()
        model2 = BaseModel()

        # Test if ids are unique
        self.assertNotEqual(model1.id, model2.id)

        # Test if BaseModel saves correctly
        model1.save()
        self.assertIsInstance(model1.updated_at, datetime)

        # Test serialization and deserialization
        model_dict = model1.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(model1.to_dict(), new_model.to_dict())

    # Add test methods for other models

if __name__ == '__main__':
    unittest.main()
