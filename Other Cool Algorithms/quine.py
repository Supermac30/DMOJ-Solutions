def f():
    import inspect
    print(inspect.getsource(f), end='')
    print("f()")
f()
