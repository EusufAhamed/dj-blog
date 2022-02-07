import random
from post.models import Post

def slugify(name: str) -> str:
    slug = name.replace(' ', '-').lower()
    try:
        post_slug = Post.objects.get(slug=slug)
    except:
        post_slug = None

    if post_slug:
        return f'{slug}-{random.randint(1000, 9999)}'
    else:
        return f'{slug}'