from web.test.common.file.aleter_file import alter

# dev
f1 = 'C:/opt/settings/server.properties'
old = 'env=local'
new = '#env=local\n'
alter(f1, old, new)
old = '#env=DEV'
new = 'env=DEV'
alter(f1, old, new)
