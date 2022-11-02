import inspect
import colorama
print(inspect.isclass(colorama))
print(callable(colorama))

# colorama.init - приймає деякі кв-аргументи, щоб перевизначити поведінку за умовчанням.

for method in dir(colorama):
    print(method)
print(inspect.isclass(colorama.init))
print(inspect.ismodule(colorama.init))
print(callable(colorama.init))
for method in dir(colorama.init):
    print(method)