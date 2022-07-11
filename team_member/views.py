from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from django.views import generic

from .form import TeamMemberForm
from .models import TeamMember


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'team_member/index.html'
    context_object_name = 'member_list'

    def get_queryset(self):
        return TeamMember.objects.all().order_by('id')


def edit(request, member_id):
    member = get_object_or_404(TeamMember, id=member_id)
    if request.method == 'POST':
        team_member_form = TeamMemberForm(request.POST, instance=member)
        if team_member_form.is_valid():
            team_member_form.save()
            return HttpResponseRedirect(reverse('team_member:index'))
        else:
            return render(request, 'team_member/edit.html', {'form': team_member_form})
    else:
        team_member_form = TeamMemberForm(instance=member)
        return render(request, 'team_member/edit.html', {'form': team_member_form, 'member_id': member_id})


def delete(request, member_id):
    member = get_object_or_404(TeamMember, id=member_id)
    member.delete()
    return HttpResponseRedirect(reverse('team_member:index'))


def add(request):
    if request.method == 'POST':
        team_member_form = TeamMemberForm(request.POST)
        if team_member_form.is_valid():
            team_member_form.save()
            return HttpResponseRedirect(reverse('team_member:index'))
        else:
            return render(request, 'team_member/add.html', {'form': team_member_form})
    else:
        team_member_form = TeamMemberForm()
        return render(request, 'team_member/add.html', {'form': team_member_form})