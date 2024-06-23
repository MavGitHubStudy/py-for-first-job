"""
Настройка окружения
"""

# Установить нужную версию Python;
# Создать виртуальное окружение;
# Работа с зависимостями (pip list, pip freeze, pip install/uninstall);

# "Pip install Packages" - система управления пакетами
#
# Большинство дистрибутивов Python уже содержат pip. Если pip отсутствует, то
# его можно установить при помощи системы управления пакетами или через cURL,
# утилиту для загрузки через интернет:
#
# curl https://boostrap.pypa.io/get-pip.py | python
#
# pip install some-package-name
#
# pip uninstall some-package-name
#
# Важно, что pip предоставляет возможность управлять всеми пакетами и их
# версиями с помощью файла requirements.txt. Это позволяет эффективно
# воспроизводить весь необходимый список пакетов в отдельном окружении
# (например, на другом компьютере) или в виртуальном окружении. Это
# достигается с помощью правильно составленного файла requirements.txt
# и следующей команды:
#
# pip install -r requirements.txt
#
# Установка некоторых пакетов для конкретных версий python, где ${version}
# заменяется на 2, 3, 3.6, и т. д.:
#
# pip${version} install some-package-name
#
# Формирование файла зависимостей requirements.txt:
#
# pip freeze > requirements.txt
#