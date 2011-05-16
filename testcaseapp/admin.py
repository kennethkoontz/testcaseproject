from testcaseapp.models import TestSuite, Milestone, TestCase
from django.contrib import admin

admin.site.register(TestSuite, TestCase, Milestone)


