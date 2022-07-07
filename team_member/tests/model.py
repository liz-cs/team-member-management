from unittest import TestCase

from team_member.models import TeamMember


class TestModels(TestCase):
    def test_model_str(self):
        people = TeamMember.objects.create(first_name="Liz", last_name="Ale", phone_number="778-879-1283",
                                           email="ba@gmail.com", status=False)
        self.assertEqual(str(people), "Liz Ale")

    def test_model_str_admin(self):
        people = TeamMember.objects.create(first_name="Liz", last_name="Ale", phone_number="778-879-1283",
                                           email="ba@gmail.com", status=True)
        self.assertEqual(str(people), "Liz Ale (admin)")
