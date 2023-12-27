import os





BASE_DIR = os.path.dirname(os.path.abspath(__file__))


   
dir_files = [filename.lower() for filename in os.listdir(BA
files_list = ['program.py', 'readme.md']




def test_program():
    for filename in files_list:
        assert filename in dir_files, f'Файл `{filename}` не найден в корне репозитория'


ааа
    try:
        import program
    except Exception as e:
        assert False, (
            'Не удалоvfdvfdvdfvfdсь запустить `program.py`. '
            'Исправьте вx  x x x xнем ошибки:\n'
            f'{e}'
        )
