import gzip
import random
import re
import struct
from io import BytesIO
from urllib.parse import quote

from django.conf import settings
from django.core import mail
from django.core.exceptions import PermissionDenied
from django.http import (
    FileResponse,
    HttpRequest,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
    StreamingHttpResponse,
)
from django.middleware.clickjacking import XFrameOptionsMiddleware
from django.middleware.common import BrokenLinkEmailsMiddleware, CommonMiddleware
from django.middleware.gzip import GZipMiddleware
from django.middleware.http import ConditionalGetMiddleware
from django.test import RequestFactory, SimpleTestCase, override_settings

int2byte = struct.Struct(">B").pack


def get_response_empty(request):
    return HttpResponse()


def get_response_404(request):
    return HttpResponseNotFound()


@override_settings(ROOT_URLCONF="middleware.urls")
class CommonMiddlewareTest(SimpleTestCase):

    rf = RequestFactory()

    @override_settings(APPEND_SLASH=True)
    def test_append_slash_have_slash(self):
        """
        URLs with slashes should go unmolested.
        """
        request = self.rf.get("/slash/")