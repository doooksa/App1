from django.db import models

class News(models.Model):
    date = models.DateTimeField('Дата')
    title = models.CharField('Название', max_length=50)
    post = models.TextField('Описание')


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Сourses(models.Model):
    title = models.CharField('Название', max_length=65)
    post = models.TextField('Описание')
    image = models.ImageField(null=True, blank=True, upload_to="img/course/images/",
                                      verbose_name=u'Изображение', )

    def __str__(self):
        return self.title

    def bit(self):
        if self.image:
            return u'<img src="%s" width="70"/>' % self.image.url
        else:
            return u'(none)'

    bit.short_descriptio = u'Изображение'
    bit.allow_tags = True

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'