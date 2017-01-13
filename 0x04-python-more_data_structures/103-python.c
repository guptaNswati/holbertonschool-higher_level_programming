#include <stdio.h>
#include <Python.h>


/**
* print_python_bytes -
* @p: python object
* Return: nothing print some basic info about Python bytes objects
**/
void print_python_bytes(PyObject *p)
{
	char *s;
	Py_ssize_t len, i;

	printf("[.] bytes object info\n");
	if (!p)
		printf("[ERROR] Invalid Bytes Object\n");
	PyBytes_AsStringAndSize(p, &s, &len);
	printf("size: %d\n", (int)len);
	printf("trying string: %s\n", s);
	if (len > 10)
		len = 10;
	else
		len++;
	printf("first %d bytes: ", (int)len);
	for (i = 0; i < len - 1; i++)
		printf("%02x ", s[i]);
	printf("%02x\n",s[len - 1]);
}


/**
* print_pyhton_list - print some basic info about Python lists
* @p: python object
* Return: nothing
**/
void print_python_list(PyObject *p)
{
/*	char *s;
	Py_ssize_t len, i; */

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", (int)PyBytes_Size(p));
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
/*	for (i = 0; i < len; i++)
	{
		printf("Element %d: bytes\n", (int)i);
		print_python_bytes((PyObject *)PyBytes_FromString(s[i]));
		} */
}
