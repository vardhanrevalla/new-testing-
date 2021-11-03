# Created this for more readablity in code and to follow the existing django
# structure instead of just putting categories in setting.context processors

from Storage.models import Category


def categories(request):
    """
    make categories available all over the site
    :param request:
    :return: Category List
    """
    return {
        'categories': Category.objects.all()
    }
