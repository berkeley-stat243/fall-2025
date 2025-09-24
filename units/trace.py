import traceback

def function_a():
    function_b()  # line 2 within function, line 4 overall

def function_b():
    # some comment
    # another comment
    function_c()  # line 4 within function, line 9 overall

def function_c():
    traceback.print_stack() # line 2 within, line 12 overall
    # raise RuntimeError("A fake error")

function_a()    # line 1 relative to the call, line 15 overall
