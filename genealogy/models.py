from django.db import models

class Tree(models.Model):
    name = models.CharField(max_length=100 ,db_index=True)
    description = models.CharField(max_length=1000)
    created_at = models.DateTimeField("Data de criação")

class Person(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300, db_index=True)
    class SexOptions(models.TextChoices):
        MASCULINO = 'M', 'Masculino'
        FEMININO = 'F', 'Feminino'
    sex = models.CharField(
        max_length=1,
        choices=SexOptions.choices,
        default=SexOptions.MASCULINO
    )
    birth_date = models.DateField() # aqui tem um problema... como representar "entre 1719 e 1722?" ou "antes de 1750?"
    death_date = models.DateField(null=True)

class Event(models.Model):
    class EventType(models.TextChoices):
        BIRTH = 'B', 'Nascimento'
        WEDDING = 'W','Casamento'
        DEATH = 'D','Óbito'
    event_type = models.CharField(
        max_length=1,
        choices=EventType.choices,
        default=EventType.BIRTH
    )
    participants = models.ManyToManyField(
        Person,
        related_name='events',
        through="EventParticipant"
    )
    event_date = models.DateField("Data do evento")
    event_location = models.CharField(max_length=200)
    description = models.TextField()

class Document(models.Model):
    class DocType(models.TextChoices):
        CERTIFICATE = 'C', 'Certidão'
        PHOTOGRAPH = 'P', 'Fotografia'
        TRANSLATION = 'T', 'Tradução'
        PARISH_RECORD = 'R', 'Registro Paroquial'  # 'R' de Record para não repetir o 'P'
        CENSUS = 'N', 'Censo'                      # 'N' de ceNsus para não repetir o 'C'
        INVENTORY = 'I', 'Inventário'
    doc_type = models.CharField(
        max_length=1,
        choices=DocType.choices,
        default=DocType.CERTIFICATE
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="documents")
    file = models.FileField(upload_to="documentos/%Y/%m/%d/")
    transcription = models.TextField(blank=True, null=True)
    observations = models.TextField(blank=True, null=True)

class EventParticipant(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    class Role(models.TextChoices):
        FATHER = 'F', 'Pai'
        MOTHER = 'M', 'Mãe'
        CHILD = 'C', 'Criança'
        GROOM = 'G', 'Noivo'
        BRIDE = 'B', 'Noiva'
        PRIEST = 'P', 'Padre'
        WITNESS = 'W', 'Testemunha'
    role = models.CharField(
        max_length=1,
        choices= Role.choices,
        default=Role.FATHER
    )

