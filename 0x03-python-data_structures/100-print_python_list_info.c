#include <stdio.h>
#include <Python.h>

/**
* print_python_list_info - in C, print some basic info about Python lists.
* @p: a python object to be parsed
* Return: nothing
**/
void print_python_list_info(PyObject *p)
{
	int i;

	printf("[*] Size of the Python List = %d\n", (int)Py_SIZE(p));
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

	for (i = 0; i < (int)Py_SIZE(p); i++)
		printf("Element %d: %s\n", i,
		       Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
