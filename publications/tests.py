from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from publications.models import Publication
from users.models import User


class PublicationViewTest(TestCase):
    """Тест публикаций """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(phone='89319891111', password='qwe123@@@QQM', is_active=True)
        # self.client.login(phone='89319891111', password='qwe123@@@QQM@@@QQM')
        self.client.force_login(self.user)

    def test_get_post(self):
        """Тест создания публикации """
        response = self.client.get(reverse('publications:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publications/publication_form.html')
        data = {
            'title': 'Test Publication',
            'body': 'This is a test publication.',
        }
        response = self.client.post(reverse('publications:create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('publications:index'))
        self.assertEqual(Publication.objects.all().filter(author_id=self.user).first().title, 'Test Publication')

    # def test_list(self):
        """Тест списка публикации """
        response = self.client.get(reverse('publications:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Publication.objects.count(), 1)

    # def test_updaate(self):
        """Тест обновления публикации """
        self.pub_update = Publication.objects.all().filter(author_id=self.user).first()
        response = self.client.get(reverse_lazy('publications:update', kwargs={'pk': self.pub_update.id}))
        self.assertEqual(response.status_code, 200)
        data = {'title': 'Updated test publication',
                'body': 'Updated test content'}
        response = self.client.post(reverse('publications:update', kwargs={'pk': self.pub_update.id}), data=data)
        self.assertEqual(response.status_code, 302)
        self.pub_update.refresh_from_db()
        self.assertEqual(self.pub_update.title, 'Updated test publication')
        self.assertEqual(self.pub_update.body, 'Updated test content')

    # def test_main_public():
        """Тест страницы мои публикации"""
        self.client.get(reverse_lazy('publications:my_public'))
        self.assertEqual(response.status_code, 302)

    # def test_delete(self):
        """Тест удаления публикации """
        self.pub_delete = Publication.objects.all().filter(author_id=self.user).first()
        response = self.client.get(reverse_lazy('publications:delete', kwargs={'pk': self.pub_delete.id}))
        self.assertEqual(response.status_code, 200)
        self.client.delete(reverse_lazy('publications:delete', kwargs={'pk': self.pub_update.id}))
        self.assertEqual(Publication.objects.count(), 0)
