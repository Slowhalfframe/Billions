from django.db import models


class Nav(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12, verbose_name="导航名字")
    link = models.CharField(max_length=100, null=True, blank=True, verbose_name="导航链接")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="关联一级菜单")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '导航'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Logo(models.Model):
    id = models.AutoField(primary_key=True)
    logo_content = models.CharField(max_length=12, null=True, verbose_name="网站标题")
    logo_link = models.CharField(max_length=55, null=True, blank=True, verbose_name="网站logo链接")
    logo_src = models.ImageField(upload_to='static/common/logo', verbose_name="LOGO图片地址")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = 'LOGO'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.logo_content


class TopBox(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=256, null=True, blank=True, verbose_name="顶部通告")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '顶部通告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Footer(models.Model):
    id = models.AutoField(primary_key=True)
    contact1 = models.ImageField(upload_to='static/common/contact', null=True, blank=True, verbose_name="联系方式1地址")
    contact1_info = models.CharField(max_length=125, null=True, blank=True, verbose_name="联系方式1 脚注")
    contact2 = models.ImageField(upload_to='static/common/contact', null=True, blank=True, verbose_name="联系方式2地址")
    contact2_info = models.CharField(max_length=125, null=True, blank=True, verbose_name="联系方式2 脚注")
    jianjie = models.TextField(null=True, blank=True, verbose_name="网站简介")
    copyright = models.TextField(null=True, blank=True, verbose_name="网站版权")
    email_adress = models.CharField(max_length=128, null=True, blank=True, verbose_name="联系邮箱")
    record_number = models.CharField(max_length=46, null=True, blank=True, verbose_name="备案号")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '页脚'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.jianjie


class FriendsLink(models.Model):
    id = models.AutoField(primary_key=True)
    friends_name = models.CharField(max_length=48, verbose_name="友情链接名称")
    friends_link = models.CharField(max_length=55, verbose_name="友情链接地址")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.friends_name