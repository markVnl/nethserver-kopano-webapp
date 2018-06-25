#
# 30 KOPANO WEBAPP
#
RewriteEngine On
RewriteRule ^/webapp(/.*)?$ https://%\{HTTP_HOST\}/webapp$1 [R=301,L]

