from rest_framework.renderers import JSONRenderer


class IdentJsonRenderer(JSONRenderer):
    """Class responsible to ident the content."""
    def get_indent(self, accepted_media_type, renderer_context):
        return 4

