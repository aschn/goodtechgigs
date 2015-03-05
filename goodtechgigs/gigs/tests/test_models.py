from django.test import TestCase
from django.db import IntegrityError
from users.models import User
from profiles.models import GigPoster
from gigs.models import Gig


class TestGig(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='myname',
                                        email='me@me.com',
                                        password='mypw')
        self.poster = GigPoster.objects.create(user=self.user)

    def test_null_create_fails(self):
        self.assertRaises(IntegrityError, Gig.objects.create)

    def test_poster_required(self):
        gig = Gig.objects.create(poster=self.poster)
        self.assertIsNotNone(gig)

    def test_has_title(self):
        gig = Gig.objects.create(poster=self.poster, title='thing to do')
        self.assertEqual(gig.title, 'thing to do')

    def test_has_description(self):
        gig = Gig.objects.create(poster=self.poster, description='info about gig')
        self.assertEqual(gig.description, 'info about gig')

    def test_has_timestamps(self):
        gig = Gig.objects.create(poster=self.poster)
        self.assertLessEqual(gig.created, gig.modified)

    def test_has_status(self):
        # status is 'draft' by default
        gig = Gig.objects.create(poster=self.poster)
        self.assertEqual(gig.status, 'draft')
        self.assertGreaterEqual(gig.status_changed, gig.created)

    def test_has_skills_desired(self):
        gig = Gig.objects.create(poster=self.poster)
        self.assertEqual(gig.skills_desired.all().count(), 0)

        gig.skills_desired.add('python')
        self.assertItemsEqual(gig.skills_desired.names(), ['python'])

    def test_str_is_title(self):
        gig = Gig.objects.create(poster=self.poster, title='thing to do')
        self.assertEqual(gig.title, str(gig))
