from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views import generic

from .models import TeamMember


# Create your views here.

class IndexView(generic.ListView):
    template_name = 'team_member/index.html'
    context_object_name = 'member_list'

    def get_queryset(self):
        return TeamMember.objects.all().order_by('id')


class EditView(generic.DetailView):
    model = TeamMember
    template_name = 'team_member/edit.html'
    context_object_name = 'member'


def edit(request, member_id):
    member = get_object_or_404(TeamMember, pk=member_id)
    return render(request, 'team_member/edit.html', {'member': member})


def edit_save(request, member_id):
    member = get_object_or_404(TeamMember, pk=member_id)
    save(member, request)
    return HttpResponseRedirect(reverse('team_member:index'))


def delete(request, member_id):
    member = get_object_or_404(TeamMember, pk=member_id)
    member.delete()
    return HttpResponseRedirect(reverse('team_member:index'))


def add(request):
    member = TeamMember()
    return render(request, 'team_member/add.html', {'member': member})


def add_save(request):
    member = TeamMember()
    save(member, request)
    return HttpResponseRedirect(reverse('team_member:index'))


def save(member, request):
    member.first_name = request.POST['first_name']
    member.last_name = request.POST['last_name']
    member.email = request.POST['email']
    member.phone_number = request.POST['phone_number']
    if request.POST['status'] == 'true':
        member.status = True
    else:
        member.status = False
    member.save()
