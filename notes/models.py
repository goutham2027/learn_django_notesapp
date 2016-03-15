from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from reversion import revisions as reversion

class CommonInfo(models.Model):
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(models.Model):
    '''
    UserProfile is to extend default User model.
    '''
    user = models.OneToOneField(User, related_name='profile')

    class Meta:
        db_table = 'user_profile'

    def my_notes(self):
        my_notes = Note.objects.filter(user=self.user).order_by('-created_at')
        return my_notes

    def has_credits(self):
        membership = Membership.objects.filter(user=self.user).first()
        return membership.credits_left > 0

    def credits(self):
        membership = Membership.objects.filter(user=self.user).first()
        return membership.credits_left

class Note(CommonInfo):
    user = models.ForeignKey(User)
    notes_text = models.TextField()

    class Meta:
        db_table = 'notes'

    def __str__(self):
        return '%s' % (self.notes_text)

reversion.register(Note)

class Plan(CommonInfo):
    '''
     free - credits(100)
     paid - credits(infinity)
    1 credit is 1 note
    '''

    class Meta:
        db_table = 'plans'

    plan_name = models.CharField(max_length=100)
    credits = models.IntegerField(default=100)

    def __str__(self):
        return '%s -  %s' % (self.plan_name, self.credits)


class Membership(CommonInfo):
    # fields: user_id, plan_id, credits_left
    user = models.ForeignKey(User)
    plan = models.ForeignKey(Plan)
    credits_left = models.IntegerField()

    class Meta:
        db_table = 'memberships'

    def __str__(self):
        return '%s - %s' % (self.user.username, self.credits_left)
