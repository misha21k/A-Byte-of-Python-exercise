import os, platform, logging

if platform.platform().startswith('Windows'):
    loggingFile = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'), 'test.log')
else:
    loggingFile = os.path.join(os.getenv('HOME'), 'test.log')

print('Сохранить лог в', loggingFile)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=loggingFile,
    filemode='w',
)

logging.debug('Начало программы')
logging.info('Какие-то действия')
logging.warning('Программа умирает')
