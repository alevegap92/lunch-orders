from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from foodlunch.celery import app as celery_app
from django.template import Template, Context
from .models import Menu

REPORT_TEMPLATE = """
<center>
<b>Today's menu {% now "jS \o\f F" %}:</b>
<br></br>
{% if object_list %} 
    {% for menu in object_list %}

                <label>{{menu.menu_name}}</label>
                <br></br>
                
                <label>Contains:</label>
        {% for food in menu.menu_foodtype.all %}        
                <p>{{ food.name }}</p>
        {% endfor %}

                <label>price</label>
                <p>{{ menu.price}}</p>
                <br></br>
    {%endfor%} 
{% endif %}
</center>
"""
 
 
@celery_app.task
def task_mail():
    for user in get_user_model().objects.all():
        menus = Menu.objects.all()
        template = Template(REPORT_TEMPLATE)
 
        send_mail(
            'Today s menu',
            template.render(context=Context({'menus': menus})),
            'ravp92@gmail.com',
            [user.email],
            fail_silently=False,
        )