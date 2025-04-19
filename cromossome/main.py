run_flag = False
if __name__ == "__main__":
    print ("You have run cromossome")
    run_flag = True
else:
    print ("You have imported cromossome")
hooks = {}

manifest_versions = ["v1-repl"]

def call_get_bindings(file):

    lib = getattr(__import__("imports."+file[:-3]),file[:-3])
    
    if hasattr(lib,"get_bindings"):
        return getattr(lib,"get_bindings")()
    else:
        raise ImportWarning(f"The file '{file}' isn't a command")

def load_hooks_from_manifesto(nln_object:dict):

    if not (nln_object["manifest"]["_val"] in manifest_versions):

        raise ImportError(f"the manifest version {nln_object['manifest']['_val']} is invalid or isn't suported by this version of cromossome (suported manifestos: {manifest_versions})")

    version = nln_object["manifest"]["_val"]
    data:dict = nln_object["manifest"]
    del data["_val"]
    for key in data.keys():
        if isinstance(data[key],dict):
            if data[key]["_val"] == "true":
                data[key]["_res"] = call_get_bindings(key) 
            else:
                del data[key] # rewrite this if cascade to combine these into the same line

        else:

            if data[key] == "true":

                data[key] = {"_res":call_get_bindings(key)}
            else:

                del data[key] # rewrite this if cascade to combine these into the same line

    hooks = {}
    processed = False
    match version:

        case "v1-repl":
            print ("Now decoding a 'v1-repl' manifesto")
            processed = True
            for key in data.keys():

                prefix = ''

                if hasattr(data[key],"prefix"):

                    prefix = data[key]["prefix"]+" "
                    del data[key]["prefix"]

                for (command,bind) in data[key]["_res"]:
                    print("biding command '"+prefix+command+"'")
                    hooks[prefix+command] = bind

    
    if not processed:

        raise NotImplementedError(f"The method for processing the manifest version {version} is missing")

    return hooks 

if run_flag:
    print("The default behaivor when launching cromossome directly is to launch an simple test, you can disable this by editing out line 4")

    import nln as nln

    data = ""
    with open("test_manifesto.nln") as f:
        data = nln.parse(f.read())

    print(load_hooks_from_manifesto(data))