#!/usr/bin/python3
if __name__ == "__main__":
    import importlib
    module = importlib.import_module("variable_load_5")

    try:
        a = module.a
        print(a)
    except AttributeError:
        print("The variable 'a' is not present in variable_load_5.py")
