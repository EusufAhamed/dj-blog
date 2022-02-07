from post.models import Category

def context_data(req):
    data = {}
    data['categories'] = Category.objects.all()

    return data