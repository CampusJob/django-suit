try:
    # Python 3.
    from urllib.parse import parse_qs
except ImportError:
    # Python 2.6+
    from urlparse import parse_qs

try:
    from django.template.defaulttags import url
except ImportError:
    from django.templatetags.future import url
