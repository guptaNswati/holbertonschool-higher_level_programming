#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	printf("[p->size] %d", Py_SIZE(p));
}
