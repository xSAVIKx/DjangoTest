from django.template.base import TemplateSyntaxError, Node, VariableDoesNotExist, Library, Variable

__author__ = 'iurii'
register = Library()


@register.tag('edit')
def edit_tag(parser, token):
    try:
        tag_name, object_to_get_absolute_url = token.split_contents()
    except ValueError:
        raise TemplateSyntaxError("%r  tag requires exactly one argument" % token.contents.split()[0])

    return EditUrlNode(object_to_get_absolute_url)


class EditUrlNode(Node):
    def __init__(self, object_to_get_absolute_url):
        self.object_to_get_absolute_url = object_to_get_absolute_url

    def render(self, context):
        try:
            actual_object = Variable(self.object_to_get_absolute_url).resolve(context)
            absolute_url = actual_object.get_absolute_url()
            return self.get_admin_absolute_url(absolute_url)
        except VariableDoesNotExist:
            return ''

    def get_admin_absolute_url(self, absolute_url):
        return "admin" + absolute_url