from django.test import TestCase
from django.db import IntegrityError
from users.models import User
from profiles.models import GigSeeker, GigPoster


class TestGigSeeker(TestCase):
    def setUp(self):
        self.u = User.objects.create(username='myname',
                                     email='me@me.com',
                                     password='mysecret')

    def test_null_create_fails(self):
        self.assertRaises(IntegrityError, GigSeeker.objects.create)

    def test_user_required(self):
        seeker = GigSeeker.objects.create(user=self.u)
        self.assertIsNotNone(seeker)

    def test_has_timestamps(self):
        seeker = GigSeeker.objects.create(user=self.u)
        self.assertLessEqual(seeker.created, seeker.modified)

    def test_has_location(self):
        seeker = GigSeeker.objects.create(user=self.u, location='here')
        self.assertEqual(seeker.location, 'here')

    def test_has_about(self):
        seeker = GigSeeker.objects.create(user=self.u, about='this is me')
        self.assertEqual(seeker.about, 'this is me')

    def test_has_skills(self):
        seeker = GigSeeker.objects.create(user=self.u)
        self.assertEqual(seeker.skills.all().count(), 0)

        seeker.skills.add('python')
        self.assertItemsEqual(seeker.skills.names(), ['python'])

    def test_has_causes(self):
        seeker = GigSeeker.objects.create(user=self.u)
        self.assertEqual(seeker.causes.all().count(), 0)

        seeker.causes.add('energy')
        self.assertItemsEqual(seeker.causes.names(), ['energy'])


class TestGigPoster(TestCase):
    def setUp(self):
        self.u = User.objects.create(username='myname',
                                     email='me@me.com',
                                     password='mysecret')

    def test_null_create_fails(self):
        self.assertRaises(IntegrityError, GigPoster.objects.create)

    def test_user_required(self):
        poster = GigPoster.objects.create(user=self.u)
        self.assertIsNotNone(poster)

    def test_has_timestamps(self):
        seeker = GigSeeker.objects.create(user=self.u)
        self.assertLessEqual(seeker.created, seeker.modified)
        
    def test_has_location(self):
        poster = GigPoster.objects.create(user=self.u, location='here')
        self.assertEqual(poster.location, 'here')

    def test_has_about(self):
        poster = GigPoster.objects.create(user=self.u, about='this is me')
        self.assertEqual(poster.about, 'this is me')

    def test_has_causes(self):
        poster = GigPoster.objects.create(user=self.u)
        self.assertEqual(poster.causes.all().count(), 0)

        poster.causes.add('energy')
        self.assertItemsEqual(poster.causes.names(), ['energy'])

    def test_has_name(self):
        poster = GigPoster.objects.create(user=self.u, org_name='my org')
        self.assertEqual(poster.org_name, 'my org')

    def test_name_is_unique(self):
        org_name = 'my org'
        GigPoster.objects.create(user=self.u, org_name=org_name)
        self.assertRaises(IntegrityError, GigPoster.objects.create, user=self.u, org_name=org_name)

    def test_str_is_name(self):
        poster = GigPoster.objects.create(user=self.u, org_name='my org')
        self.assertEqual(poster.org_name, str(poster))
