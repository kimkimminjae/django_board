from django.db import models

# Create your models here.

class Question(models.Model):
    subject = models.CharField(max_length=200) #길이제한 char
    content = models.TextField() #길이 제한x Text
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
    #id 대신 제목표시하기


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #기존 모델에 연결하려면 ForeignKey를 사용 ForeignKey는 다른 모델과 연결
    #on_delete=models.CASCADE 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제된다는 의미
    content = models.TextField()
    create_date = models.DateTimeField()