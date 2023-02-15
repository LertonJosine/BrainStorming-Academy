from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class Curso(models.Model):
    alunos = models.ManyToManyField(get_user_model(), related_name="alunos")
    nome = models.CharField(max_length=100)
    professores = models.ManyToManyField(get_user_model(), related_name="professores")

    def __str__(self):
        return self.nome
        



class Modulo(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    aluno = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="aluno")
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    professor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="professor")
    nota = models.IntegerField()
