def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    print("Я тут просто так")
    inner_function()

test_function()
# inner_function() - выдает NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
