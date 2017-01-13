#include <stdio.h>
#include <Python.h>

/**
* print_pyhton_list - print some basic info about Python lists
* @p: python object
* Return: nothing
**/
void print_python_list(PyObject *p)
{
	printf("%p\n", (void *)p);
}

/**
* print_python_bytes -
* @p: python object
* Return: nothing print some basic info about Python bytes objects
**/
void print_python_bytes(PyObject *p)
{
	char *s;
	Py_ssize_t len;

	printf("[.] bytes object info\n");
	PyBytes_AsStringAndSize(p, &s, &len);
	printf("size: %d\n", (int)len);
	printf("trying string: %s\n", s);
}
