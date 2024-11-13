from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


class ProfileManager(models.Manager):
    def get_best(self):
        return self.annotate(like_count=Count('user__answers__likes')).order_by('-like_count')[:10]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatars/default.jpg')
    nickname = models.CharField(max_length=50)

    objects = ProfileManager()

    def __str__(self):
        return self.user.username


class TagManager(models.Manager):
    def get_popular(self):
        return self.annotate(questions_count=Count('questions')).order_by("-questions_count")[:8]


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    objects = TagManager()

    def __str__(self):
        return self.name

class QuestionManager(models.Manager):
    def with_likes_count(self):
        return self.annotate(likes_count=models.Count('likes'))

    def best(self):
        return self.with_likes_count().order_by('-likes_count')

    def newest(self):
        return self.with_likes_count().order_by('-created_at')

    def tagged(self, tag_name):
        return self.with_likes_count().filter(tags__name__contains=tag_name)

    def get_question(self, question_id):
        return self.get(question_id=question_id)


class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    tags = models.ManyToManyField(Tag, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuestionManager()

    def __str__(self):
        return self.title


class Answer(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Answer by {self.author.username} on {self.question.title}"

class QuestionLike(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='question_likes')

    class Meta:
        unique_together = ('question', 'user')

    def __str__(self):
        return f"Like by {self.user.username} on {self.question.title}"


class AnswerLike(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answer_likes')

    class Meta:
        unique_together = ('answer', 'user')

    def __str__(self):
        return f"Like by {self.user.username} on {self.answer.question.title} answer"