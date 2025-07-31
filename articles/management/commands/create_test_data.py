from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from articles.models import Section, Article
from django.utils import timezone

User = get_user_model()

class Command(BaseCommand):
    help = 'Create test data for the application'

    def handle(self, *args, **options):
        # Create Authors group
        authors_group, created = Group.objects.get_or_create(name='Authors')
        if created:
            self.stdout.write(self.style.SUCCESS('Created Authors group'))

        # Create test user
        user, created = User.objects.get_or_create(
            username='testauthor',
            defaults={
                'email': 'test@example.com',
                'first_name': 'Test',
                'last_name': 'Author',
                'bio': 'Experienced technology writer and content creator with a passion for sharing knowledge about the latest developments in software, AI, and digital innovation. I love exploring new technologies and helping others understand complex topics through clear, engaging writing.'
            }
        )
        if created:
            user.set_password('testpass123')
            user.save()
            user.groups.add(authors_group)
            self.stdout.write(self.style.SUCCESS('Created test author user'))
        else:
            # Update bio if user already exists
            user.bio = 'Experienced technology writer and content creator with a passion for sharing knowledge about the latest developments in software, AI, and digital innovation. I love exploring new technologies and helping others understand complex topics through clear, engaging writing.'
            user.save()

        # Create test sections
        sections_data = [
            {'name': 'Technology', 'slug': 'technology'},
            {'name': 'Science', 'slug': 'science'},
            {'name': 'Politics', 'slug': 'politics'},
        ]

        for section_data in sections_data:
            section, created = Section.objects.get_or_create(
                slug=section_data['slug'],
                defaults={'name': section_data['name']}
            )
            if created:
                section.authors.add(user)
                self.stdout.write(self.style.SUCCESS(f'Created section: {section.name}'))

        # Create test articles
        articles_data = [
            {
                'title': 'Sample Published Article',
                'body': '<p>This is a sample published article with some content about technology and innovation. It demonstrates how articles look when published on the platform.</p>',
                'status': Article.PUBLISHED,
                'section': Section.objects.get(slug='technology'),
                'published_at': timezone.now()
            },
            {
                'title': 'Sample Draft Article',
                'body': '<p>This is a sample draft article that needs to be reviewed and completed. It shows how draft articles appear in the system.</p>',
                'status': Article.DRAFT,
                'section': Section.objects.get(slug='science')
            }
        ]

        for article_data in articles_data:
            article, created = Article.objects.get_or_create(
                title=article_data['title'],
                defaults=article_data
            )
            if created:
                article.authors.add(user)
                self.stdout.write(self.style.SUCCESS(f'Created article: {article.title}'))

        self.stdout.write(self.style.SUCCESS('Test data created successfully!'))
        self.stdout.write('You can login with: testauthor / testpass123') 