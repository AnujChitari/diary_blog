from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from diary_app.models import DiaryEntry
from .forms import DiaryEntryForm
from .forms import DiaryForm
from django.utils import timezone


def diary_entry_detail(request, entry_id):
    entry = DiaryEntry.objects.get(id=entry_id)
    context = {
        'entry': entry,
    }
    return render(request, 'diary_entry_detail.html', context)

def create_entry(request):
    if request.method == 'POST':
        entry_date = request.POST['entry_date']
        content = request.POST['content']
        DiaryEntry.objects.create(entry_date=entry_date, content=content)
        return redirect('diary_entries')
    return render(request, 'create_entry.html')

def edit_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, pk=entry_id)
    if request.method == 'POST':
        entry_date = request.POST['entry_date']
        content = request.POST['content']
        entry.entry_date = entry_date
        entry.content = content
        entry.save()
        # return redirect('diary_entries')
        return redirect('save_diary', entry_id=entry_id)
    return render(request, 'edit_entry.html', {'entry': entry})

def diary_entries(request):
    entries = DiaryEntry.objects.all().order_by('-entry_date')
    paginator = Paginator(entries, 5)  # Show 5 entries per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    entry_id = 1

    context = {
        'page_obj': page_obj,
        'entry_id': entry_id,  # Provide a default value for entry_id
    }
    
    return render(request, 'diary_entries.html', context)

def save_diary(request, entry_id):
    if request.method == 'POST':
        form = DiaryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.entry_date = timezone.now()
            entry.save()
            return redirect('diary_entries')
    else:
        form = DiaryForm()

    return render(request, 'diary_form.html', {'form': form, 'entry_id': entry_id})


# def save_diary(request, entry_id):
#     if request.method == 'POST':
#         entry_id = request.POST['entry_id']  # Retrieve entry_id from the form data
#         entry = DiaryEntry.objects.get(id=entry_id)
#         form = DiaryForm(request.POST, instance=entry)
#         if form.is_valid():
#             entry.entry_date = timezone.now()
#             form.save()
#             return redirect('diary_entries')
#     else:
#         form = DiaryForm()

#     return render(request, 'diary_form.html', {'form': form})


# def save_diary(request, entry_id):
#     entry = DiaryEntry.objects.get(id=entry_id)
    
#     if request.method == 'POST':
#         form = DiaryForm(request.POST, instance=entry)
#         if form.is_valid():
#             entry.entry_date = timezone.now()
#             form.save()
#             return redirect('diary_entries')
#     else:
#         form = DiaryForm(instance=entry)

#     # context = {
#     #     'form': form,
#     #     'entry': entry,
#     #     'entry_id': entry_id,  # Add entry_id to the context
#     # }         
    
#     return render(request, 'diary_form.html', {'form':form})

def edit_diary_entry(request, entry_id):
    entry = get_object_or_404(DiaryEntry, id=entry_id)
    
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('diary_entry_detail', entry_id=entry.id)
    else:
        form = DiaryEntryForm(instance=entry)
    
    # context = {
    #     'form': form,
    #     'entry': entry,
    # }
    return render(request, 'edit_diary_entry.html', {'form': form})