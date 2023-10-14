#include <Python.h>

void print_python_list(PyObject *p) {
    PyObject *obj;
    Py_ssize_t size;
    Py_ssize_t i;

    if (!PyList_Check(p)) {
        printf("Invalid list object\n");
        return;
    }

    size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p)) {
        printf("[.] Invalid Bytes Object\n");
        return;
    }

    size = ((PyVarObject *)p)->ob_size;
    str = ((PyBytesObject *)p)->ob_sval;

    printf("[.] bytes object info\n");
    printf("  [.] Size: %ld\n", size);
    printf("  [.] Trying string: %s\n", str);
    printf("  [.] Address of the object: %p\n", (void *)p);
    printf("  [.] first %ld bytes: ", (size < 10) ? size : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02hhx", str[i]);
        if (i < 9 && i < size - 1) {
            printf(" ");
        }
    }
    printf("\n");
}

int main(void) {
    // Example usage
    Py_Initialize();
    PyRun_SimpleString("l = [1, 2, 3]\n");
    PyRun_SimpleString("s = b'Hello'\n");

    PyObject *l = PyList_GetItem(PyEval_GetLocals(), 0);
    PyObject *s = PyList_GetItem(PyEval_GetLocals(), 1);

    print_python_list(l);
    print_python_bytes(s);

    Py_Finalize();
    return 0;
}
