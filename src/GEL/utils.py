from django.utils.text import slugify
from django.conf import settings
import random
import string
import threading
import mailchimp


def random_string_generator(
    size=10,
    chars=string.ascii_lowercase + string.digits
):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug


class SendSubscribeMail(object):
    def __init__(self, email):
        self.email = email
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        API_KEY = settings.MAILCHIMP_API_KEY
        LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID
        api = mailchimp.Mailchimp(API_KEY)
        try:
            api.lists.subscribe(LIST_ID, {'email': self.email})
        except:
            return False
