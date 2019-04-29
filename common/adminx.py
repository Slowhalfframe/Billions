import xadmin
from . import models
from xadmin import views


# xadmin修改顶部django， 修改底部公司
class GlobalSetting(object):
    site_title ="博客后台管理系统"
    site_footer ="Circle"
    # menu_style ="accordion"


class BaseSetting(object):
    enable_themes =True
    use_bootswatch =True


class Nav(object):
    # 展示管路员可见字段
    list_display = ["id", 'name', 'link', 'parent', 'add_time']
    # 设置管理员可编辑字段
    list_editable = ['name', 'link', 'parent', 'add_time']
    # 每页显示多少条
    list_per_page = 10
    # 设置显示外键字段
    # fk_fields = []
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('name', 'link', 'parent',  'add_time')


class Logo(object):
    # 展示管路员可见字段
    list_display = ["id", 'logo_content', 'logo_src', 'add_time']
    # 设置管理员可编辑字段
    list_editable = ['logo_content', 'logo_src', 'add_time']
    # 每页显示多少条
    list_per_page = 10
    # 设置显示外键字段
    # fk_fields = []
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('logo_content', 'logo_src', 'add_time')


class TopBox(object):
    # 展示管路员可见字段
    list_display = ["id", 'content', 'add_time']
    # 设置管理员可编辑字段
    list_editable = ['content', 'add_time']
    # 每页显示多少条
    list_per_page = 10
    # 设置显示外键字段
    # fk_fields = []
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('content', 'add_time')


class Footer(object):
    # 展示管路员可见字段
    list_display = ["id", 'contact1', 'contact1_info', 'contact2', 'contact2_info', 'jianjie', 'copyright', 'email_adress', 'record_number', 'add_time']
    # 设置管理员可编辑字段
    list_editable = [ 'contact1', 'contact1_info', 'contact2', 'contact2_info', 'jianjie', 'copyright', 'email_adress', 'record_number', 'add_time']
    # 每页显示多少条
    list_per_page = 10
    # 设置显示外键字段
    # fk_fields = []
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ( 'contact1', 'contact1_info', 'contact2', 'contact2_info', 'jianjie', 'copyright', 'email_adress', 'record_number', 'add_time')


class FriendsLink(object):
    # 展示管路员可见字段
    list_display = ["id", 'friends_name', 'friends_link', 'add_time']
    # 设置管理员可编辑字段
    list_editable = ['friends_name', 'friends_link',  'add_time']
    # 每页显示多少条
    list_per_page = 10
    # 设置显示外键字段
    # fk_fields = []
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('friends_name', 'friends_link', 'add_time')


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(models.Nav, Nav)
xadmin.site.register(models.Logo, Logo)
xadmin.site.register(models.TopBox, TopBox)
xadmin.site.register(models.Footer, Footer)
xadmin.site.register(models.FriendsLink, FriendsLink)