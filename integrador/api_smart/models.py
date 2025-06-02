from django.db import models

class Sensores(models.Model):
    SENSOR_ESCOLHA = ( # opções de escolha para o sensor
        ('temperatura', 'temperatura'),
        ('luminosidade', 'luminosidade'),
        ('umidade', 'umidade'),
        ('contador', 'contador')
    )

    UNIDADE_ESCOLHA = ( # opções de escolha para a unidade de medida
        ('°C', '°C'),
        ('lux', 'lux'),
        ('%', '%'),
        ('num', 'num')
    )

    STATUS_ESCOLHA = ( # opções de escolha para status
        ('ativo', 'ativo'),
        ('inativo', 'inativo')
    )

    sensor = models.CharField(max_length=20, choices=SENSOR_ESCOLHA)
    mac_address = models.CharField(max_length=50)
    unidade_med = models.CharField(max_length=4, choices=UNIDADE_ESCOLHA)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=10, choices=STATUS_ESCOLHA)

    def __str__(self):
        return self.get_sensor_display() # forma de mostrar o valor da escolha do sensor
    
    class Meta:
        verbose_name_plural = "Sensores" # forma para colocar o nome da model no plural

    
class Ambientes(models.Model):
    sig = models.IntegerField()
    descricao = models.CharField(max_length=255, blank=True, null=True)
    ni = models.CharField(max_length=10)
    responsavel = models.CharField(max_length=30)

    REQUIRED_FIELDS = ['sig', 'ni', 'responsavel'] # campos obrigatórios

    def __str__(self):
        return self.responsavel
    
    class Meta:
        verbose_name_plural = "Ambientes" # forma para colocar o nome da model no plural


class Historico(models.Model):
    sensor = models.ForeignKey(Sensores, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambientes, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.DateTimeField()