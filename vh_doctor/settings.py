# -*- coding: utf-8 -*-
from django.conf import settings
import os
UPLOAD_TO = getattr(settings, 'DOCTOR_SPEC_UPLOAD_TO', os.path.join('uploads','doctorspec'))