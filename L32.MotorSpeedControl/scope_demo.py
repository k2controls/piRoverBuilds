''' variable scope demonstration
'''

a = 10

def test_variable_scope_get():
    print(a)

def test_variable_scope_set():
    a = a + 1
    print(a)

def test_global_variable():
    global a
    a = a + 1
    print(a)

test_variable_scope_get()
#test_variable_scope_set()
test_global_variable()