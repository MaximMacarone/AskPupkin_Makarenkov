import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from app.models import Question, Answer, Tag, QuestionLike, AnswerLike, Profile

class Command(BaseCommand):
    help = 'Fill the database with test data based on the specified ratio.'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='The coefficient for the amount of data to generate')

    def handle(self, *args, **options):
        ratio = options['ratio']

        superuser = User.objects.filter(is_superuser=True).first()
        if superuser:
            self.stdout.write(self.style.SUCCESS(f'Found superuser: {superuser.username}'))

        User.objects.exclude(id=superuser.id).delete()
        Profile.objects.all().delete()
        Question.objects.all().delete()
        Answer.objects.all().delete()
        Tag.objects.all().delete()
        QuestionLike.objects.all().delete()
        AnswerLike.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('All data cleared (except superuser).'))

        users = []
        for i in range(1, ratio+1):
            user = User(username=f'user{i}', email=f'user{i}@example.com')
            users.append(user)
        User.objects.bulk_create(users)
        profiles = [Profile(user=user, nickname=f'User {i}') for i, user in enumerate(users)]
        Profile.objects.bulk_create(profiles)
        self.stdout.write(self.style.SUCCESS(f'Created {ratio} users and profiles.'))

        tags = [Tag(name=f'Tag{i}') for i in range(ratio)]
        Tag.objects.bulk_create(tags)
        self.stdout.write(self.style.SUCCESS(f'Created {ratio} tags.'))

        questions = []
        for i in range(ratio * 10):
            question = Question(
                title=f'Question Title {i}',
                body=f'Body of question {i}',
                author=random.choice(users),
                created_at=timezone.now()
            )
            questions.append(question)
        Question.objects.bulk_create(questions)
        for question in questions:
            question.tags.set(random.sample(tags, k=min(3, len(tags))))
        self.stdout.write(self.style.SUCCESS(f'Created {ratio * 10} questions.'))

        answers = []
        for i in range(ratio * 100):
            answer = Answer(
                content=f'Content of answer {i}',
                question=random.choice(questions),
                is_correct=random.choice([True, False]),
                author=random.choice(users),
                created_at=timezone.now()
            )
            answers.append(answer)
        Answer.objects.bulk_create(answers)
        self.stdout.write(self.style.SUCCESS(f'Created {ratio * 100} answers.'))

        question_likes = set()
        question_likes_count = min(len(questions) * len(users), ratio * 100)
        while len(question_likes) < question_likes_count:
            question = random.choice(questions)
            user = random.choice(users)
            question_likes.add((question, user))
        question_likes = [QuestionLike(question=ql[0], user=ql[1]) for ql in question_likes]
        QuestionLike.objects.bulk_create(question_likes)
        self.stdout.write(self.style.SUCCESS(f'Created {len(question_likes)} question likes.'))

        answer_likes = set()
        answer_likes_count = min(len(questions) * len(users), ratio * 100)
        while len(answer_likes) < answer_likes_count:
            answer = random.choice(answers)
            user = random.choice(users)
            answer_likes.add((answer, user))
        answer_likes = [AnswerLike(answer=al[0], user=al[1]) for al in answer_likes]
        AnswerLike.objects.bulk_create(answer_likes)
        self.stdout.write(self.style.SUCCESS(f'Created {len(answer_likes)} answer likes.'))

        self.stdout.write(self.style.SUCCESS('Database filled successfully.'))