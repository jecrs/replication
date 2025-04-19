
def test_comand(args):

    print ("Hello World"+args)

def get_bindings() -> list[tuple]:

    return [('test',test_comand)]
