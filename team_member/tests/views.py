import os

from django.db.models import QuerySet
from django.http import request
from django.test import TestCase, Client

from django.urls import reverse

from team_member.models import TeamMember
from team_member.views import IndexView, edit

client = Client()


def create_team_member(first_name, last_name, phone_number, email, status):
    return TeamMember.objects.create(first_name=first_name, last_name=last_name, phone_number=phone_number,
                                     email=email, status=status)


class TeamMemberIndexViewTests(TestCase):

    def test_no_team_member(self):
        response = self.client.get(reverse('team_member:index'))
        self.assertEqual(response.status_code, 200)

    def test_one_team_member(self):
        member = create_team_member('liz', 'Mi', '878-920-1927', '23@gmail.com', True)
        self.assertEquals(IndexView.get_queryset(self)[0], QuerySet(member)[0])


class TeamEditViewTests(TestCase):
    def test_edit_page(self):
        response = self.client.get(reverse('team_member:edit', args={1}))
        self.assertFalse(response.status_code == 200)
        member = create_team_member('liz', 'Mi', '878-920-1927', '23@gmail.com', True)
        response = self.client.get(reverse('team_member:edit', args={1}))
        self.assertEqual(response.status_code, 200)


def test_add_team_member(self):
    member1 = create_team_member('liz', 'Mi', '878-920-1927', '23@gmail.com', True)
    member1.save()
    member2 = create_team_member('Mary', 'Gu', '878-920-1927', '23@gmail.com', False)
    member2.save()
    response = self.client.get(reverse('team_member:index'))
    self.assertQuerysetEqual(
        response.context['member_list'],
        ['<TeamMember: liz Mi (admin)>', '<TeamMember: Mary Gu>'],
    )


def test_remove_team_member(self):
    member1 = create_team_member('liz', 'Mi', '878-920-1927', '23@gmail.com', True)
    member1.save()
    member2 = create_team_member('Mary', 'Gu', '878-920-1927', '23@gmail.com', False)
    member2.save()
    member2.delete()
    response = self.client.get(reverse('team_member:index'))
    self.assertQuerysetEqual(
        response.context['member_list'],
        ['<TeamMember: liz Mi (admin)>'],
    )
