from __future__ import absolute_import, unicode_literals

from mezzanine.conf import register_setting


register_setting(name="FACEBOOK_APP_ID", label="Facebook App ID", editable=True, default="")

register_setting(
    name="FACEBOOK_APP_SECRET", label="Facebook App Secret", editable=True, default=""
)

register_setting(
    name="FACEBOOK_LOGIN_SCOPE",
    label="Facebook Login Scope (permissions)",
    description="https://developers.facebook.com/docs/facebook-login/permissions/",
    editable=False,
    default="",
)
