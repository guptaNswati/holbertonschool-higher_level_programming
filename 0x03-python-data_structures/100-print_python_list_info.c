#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	const char *s;

	PyArg_ParseTuple(p, "", &s);
/*	printf("[p->size] %p", (void *)p->ob_refcnt); */
}
