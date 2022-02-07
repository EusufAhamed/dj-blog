from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# pagination
def pagination(request, object_list):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(object_list, 3)

    try:
        obj = paginator.page(page_num)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(1)

    return obj

# except(EmptyPage, InvalidPage):