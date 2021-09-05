from django.core.management import call_command

def my_dbbackup():
  try:
    call_command('dbbackup')
  except:
    pass