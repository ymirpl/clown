# coding: utf-8
import sys
import os
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = "Create test users"

    def handle_noargs(self, **options):
        sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../"))
        from django.contrib.auth.models import User
        from django.db import transaction
        from registration.models import RegistrationProfile

        def print_progress(cnt, total):
            if not cnt % 100:
                print "%.2f%% done" % (cnt*100./total)

        normal_count = 1000
        creators_count = 1000

        cnt = 0

        with transaction.commit_on_success():
            for i in xrange(normal_count):
                cnt += 1
                RegistrationProfile.objects.create_inactive_user('nu_%d' % i, 'nu_%d@askthepony.com' % i, 'nu_%d' % i, None)
                print_progress(cnt, normal_count+creators_count)
            for i in xrange(creators_count):
                cnt += 1
                RegistrationProfile.objects.create_inactive_user('cc_%d' % i, 'cc_%d@askthepony.com' % i, 'cc_%d' % i, None)
                print_progress(cnt, normal_count+creators_count)

        print "Activating all the accounts..."
        RegistrationProfile.objects.all().update(activation_key="ALREADY_ACTIVATED")
        User.objects.all().update(is_active=True)
        print "All done."
