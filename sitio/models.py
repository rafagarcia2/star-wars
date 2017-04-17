from django.db import models


class Membro(models.Model):
	name = models.CharField('nome', max_length=100)
	profission = models.CharField('profissão', max_length=100)
	twitter = models.CharField('Twitter', max_length=120)
	facebook = models.CharField('Facebook', max_length=120)
	linkendin = models.CharField('LinkendIn', max_length=120)

	photo = models.ImageField(upload_to='sitio/images', verbose_name='imagem', null=True, blank=True)


	def __str__(self):
		return self.name


class Servicos(models.Model):
	title = models.CharField('Título', max_length=100)
	descript = models.TextField('Descrição')

	image = models.ImageField(upload_to='sitio/images/services', verbose_name='imagem', null=True, blank=True)


	def __str__(self):
		return self.title


	class Meta:
		verbose_name = 'Serviço'
		verbose_name_plural = 'Serviços'