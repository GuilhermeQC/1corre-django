from django.db import models
 
class Endereco(models.Model): #Relação OneToOne // Uma pessoa só pode ter um endereço
    cep = models.CharField(max_length=8, blank=False) #CEP
    road = models.CharField(max_length=100, blank=False) #Rua/ Avenida
    number = models.CharField(max_length=6, null=True) #Número
    neighborhood = models.CharField(max_length=50, blank=False) #Bairro
    city = models.CharField(max_length=50, blank=False) #Cidade 
    state = models.CharField(max_length=30, blank=False) #Estado

    class Meta: #Metadados 
        ordering =['city'] #Returna dados organizados pela cidade em ordem crescente

class Telefone(models.Model): #Relação OneToOne // Uma pessoa só pode ter um endereço
    tel = models.CharField(max_length=11, blank=False) #telefone

class Pessoa(models.Model):
    #O Atributo ID da tabela é setado e administrado por padrão pelo Django

    #Dados Pessoais
    first_name = models.CharField(max_length=80, blank=False)
    sec_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=False)
    birth_date = models.DateField(blank=False) #Data nasc
    cpf = models.CharField(max_length=11, blank=False) #CPF // Desconsiderei o RG
    address = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    phone_number = models.OneToOneField(Telefone, on_delete=models.CASCADE)
    
    #Dados de Usuário
    user = models.CharField(max_length=120, blank=False) #Usuario 
    email = models.CharField(max_length=120, blank=False) #Email 
    password = models.CharField(max_length=120, blank=False) #Senha // Eu acho que isso aqui não deveria ser na tabela pessoa, mas eu não sei oq seria melhor, ent deixa asssim
    created_at = models.DateTimeField(auto_now_add=True) #Criação do registro
    updated_at = models.DateTimeField(auto_now=True) #Ultima atualização do registro

    class Meta:
        ordering = ['first_name', 'sec_name', 'last_name']
    
class Cliente(models.Model):
    pessoa_id = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    class Meta:
        ordering = ['pessoa_id.first_name'] # Não sei se isso funciona, teria que testar

class Freelancer(models.Model):    
    pessoa_id = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

class Area(models.Model):
    name = models.CharField(max_length=100, blank=False)
    class Meta:
        ordering = ['name']

class Servico(models.Model):
    name = models.CharField(max_length=120, blank=False)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    class Meta:
        ordering = ['name']

class Oferta(models.Model):
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    service = models.ForeignKey(Servico, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)

# class Amostra(models.Model): ### Amostra? Acho que isso ficou desatualizado da nossa primeira ideia
#     pass

class Situacao(models.Model):
    EA = "Em andamento"
    Choices = {
        "NC": "Não concluido",
        "EA": "Em andamento",
        "CD": "Concluido",
    }
    situation = models.CharField(max_length=2, choices=Choices, default=EA)

class Acordo(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    oferta = models.ForeignKey(Oferta, on_delete=models.CASCADE)
    final_price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(max_length=300, blank=False)
    situation = models.ForeignKey(Situacao, on_delete=models.CASCADE)
   #modality = models.CharField() # // Falta adicionar esse atributo, seja lá oq ele signifique


### FALTA CONCLUIR MAIS 3 TABELAS