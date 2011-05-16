from django.db import models

class TestSuite(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class TestCase(models.Model):
    TYPE_CHOICES = (
        (u'Automated', u'Automated'),
        (u'Functionality', u'Functionality'),
        (u'Performance', u'Performance'),
        (u'Regression', u'Regression'),
        (u'Usability', u'Usability'),
        (u'Other', u'Other')
    )
    PRIORITY = (
        (u'1', u'1 - high'),
        (u'2', u'2 - med'),
        (u'3', u'3 - low'),
    )
    MILESTONE = (
        (u'm1', u'm1'),
        (u'm2', u'm2'),
        (u'm3', u'm3'),
    )
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    priority = models.CharField(max_length=10, choices=PRIORITY)
    milestone = models.CharField(max_length=10, choices=MILESTONE)
    setup_steps = models.CharField(max_length=200)
    steps = models.CharField(max_length=200)
    expected_results = models.CharField(max_length=200)

    def __unicode__(self):
        return self.title

