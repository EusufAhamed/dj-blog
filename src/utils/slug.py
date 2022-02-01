def slugify(name: str) -> str:
    slug = name.replace(' ', '-').lower()
    return f'{slug}'