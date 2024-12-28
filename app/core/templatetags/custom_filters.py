from django import template

register = template.Library()


@register.filter(name="getattr")
def get_attribute(value, arg):
    """Mimics Python's getattr function for templates."""
    attr = getattr(value, arg, None)
    if "." in arg:
        attr = value
        for argv in arg.split("."):
            attr = getattr(attr, argv)
    return attr() if callable(attr) else attr


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    """Custom template tag to update query parameters in pagination links."""
    query = context["request"].GET.copy()
    query.update(kwargs)
    return query.urlencode()