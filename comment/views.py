from django.shortcuts import render,redirect
from .models import Comment
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Reply_form


# Create your views here.
