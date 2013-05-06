# coding: utf-8
import sys
import os
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):
    help = "Create test users"

    def handle_noargs(self, **options):
        try:
            from django.contrib.auth.models import User
            from django.db import transaction

            def print_progress(cnt, total):
                if not cnt % 100:
                    print "%.2f%% done" % (cnt*100./total)

            normal_count = 1000
            creators_count = 1000

            cnt = 0

            with transaction.commit_on_success():
                for i in xrange(normal_count):
                    cnt += 1
                    User.objects.create_user('nu_%d' % i, 'nu_%d@askthepony.com' % i, 'nu_%d' % i)
                    print_progress(cnt, normal_count+creators_count)
                for i in xrange(creators_count):
                    cnt += 1
                    User.objects.create_user('cc_%d' % i, 'cc_%d@askthepony.com' % i, 'cc_%d' % i)
                    print_progress(cnt, normal_count+creators_count)

            print "Activating all the accounts..."
            User.objects.all().update(is_active=True)
            print "All done."
        except Exception:
            import traceback
            traceback.print_exc(file=sys.stdout)
