import unittest
from app.models import Pitch

class PitchModelTest(unittest.TestCase):
    ef setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_pitch = Pitch(id=2,data='I am Manasseh' )

def tearDown(self):
    Pitch.query.delete()
    User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,2)
        self.assertEquals(self.new_pitch.data,'I am Manasseh')

def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

def test_get_pitch_by_id(self):

        self.new_pitch.save_review()
        got_pitches = Pitch.get_pitches(12345)
        self.assertTrue(len(got_pitches) == 1)
