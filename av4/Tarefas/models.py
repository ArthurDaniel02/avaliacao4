from django.db import models
class Projeto(models.Model):
 nome = models.CharField(max_length=255) 
 descricao = models.CharField(max_length=255) 
 data_criacao = models.DateField()
 def __str__(self):
    return self.nome 
class Tarefa(models.Model):
 titulo = models.CharField(max_length=255) 
 projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE) 
 PRIORITY_CHOICES = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    ) 
 prioridade = models.CharField(choices=PRIORITY_CHOICES, default=1)
 STATUS_CHOICES = (
        ('Incompleta', 'Tarefa Incompleta'),
        ('Concluída', 'Tarefa Concluída'),
        ('Iniciado', 'Tarefa iniciada'),
        
    ) 
 status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Incompleta') 
 data_limite = models.DateField() 
 def __str__(self):
    return self.titulo 