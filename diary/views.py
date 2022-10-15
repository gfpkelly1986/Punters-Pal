from django.shortcuts import render, redirect
from .models import DiaryEntry
from diary.forms import NewEntryForm
from django.views import View


# Create your views here.
def get_landing_page(request):
    return render(request, 'index.html')


def get_sign_up_page(request):
    return render(request, 'sign-up.html')


def create_entry(request):
    return render(request, 'create_new_entry.html')


class NoteDetail(View):

    def get(self, request, *args, **kwargs):
        entry_form = NewEntryForm()
        return render(
            request,
            'create_new_entry.html',
            {
                'entry_form': entry_form,
            }
        )

    def post(self, request, *args, **kwargs):
        new_entry = NewEntryForm(data=request.POST)

        if new_entry.is_valid():
            new_entry.save()

        return render(request, 'diary_display.html')


class ShowDiaryEntries(View):

    def get(self, request, *args, **kwargs):
        entries = DiaryEntry.objects.all()

        return render(
            request,
            'diary_display.html',
            {
                'entries': entries
            })


# def get_todo_list(request):
#     items = Item.objects.all()
#     context = {
#         'items': items
#     }
#     return render(request, 'todo/todo_list.html', context)