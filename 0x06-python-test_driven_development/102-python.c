#include <Python.h>
#include <stdio.h>
#include <string.h>

/**
* print_python_string - Prints info about python str
* @p: pointer to PyObject
* Return: Nothing
**/
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (strcmp(((PyObject *)p)->ob_type->tp_name, "str") != 0)
		printf("  [ERROR] Invalid String Object\n");
	else
	{
		if (((PyASCIIObject *)p)->state.ascii
		    && ((PyASCIIObject *)p)->state.compact)
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		printf("  length: %lu\n", ((PyVarObject *)p)->ob_size);
		if (((PyASCIIObject *)p)->state.ascii)
			printf("  value: %s\n", (char *)(void *)
			       ((PyASCIIObject *)p + 1));
		else if (((PyASCIIObject *)p)->state.compact)
			printf("  value: %s\n", (char *)(void *)
			       ((PyCompactUnicodeObject *)p + 1));
		else
			printf("  value: %s\n", (char *)(void *)
			       ((PyUnicodeObject *)p)->data.any);
	}
}
