import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l(1)
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
