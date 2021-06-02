# -*- coding: utf-8 -*-
from django.conf import settings
import os
UPLOAD_TO = getattr(settings, 'CATEGORY_UPLOAD_TO', os.path.join('uploads','category'))