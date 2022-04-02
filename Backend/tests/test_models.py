from django.test import TestCase
from django.contrib.auth.models import User
from Backend.models import Idea

class IdeaModelTest(TestCase):
    def setUp(self):
        """
            Boilerplate setup for testing
        """
        self.user_model = User.objects.create_user(
            username='Simeon',
            password='123',
        )

        self.idea_model = Idea.objects.create(
            owner=self.user_model,
            title="I have an idea",
            details="MY test detail",
            tags={
                "languages": ['python', 'javascript', 'ruby on rails']
                },
            repository_link="https://www.github.com/"
        )

    def test_if_auth_works(self):
        """
            To test if the authentication system is working
        """
        test_model = User.objects.get(username='Simeon')
        self.assertEquals(self.user_model, test_model, "Authentication officially works")
    
    def test_if_idea_model_works(self):
        """
            To test if the idea model is working as expected
        """
        self.assertEquals(self.idea_model.title, "I have an idea")
        return
    
