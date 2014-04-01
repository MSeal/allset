import os, pkgutil, sys

def _get_module_directory(namespace):
    return os.path.dirname(namespace['__file__'])

def _get_module_name(namespace):
    return namespace['__name__']
    #return os.path.basename(_get_module_directory(namespace))

def _get_submodules(namespace):
    return list(pkgutil.iter_modules([_get_module_name(namespace)]))

def _assign_modules_names(filter_mods, namespace, import_modules):
    namespace['__all__'] = filter_mods([module[1] for module in import_modules])
    return namespace['__all__']

def _pass_through(arg):
    return arg

def _load_modules(namespace, import_modules):
    for module_loader, name, ispkg in import_modules:
        submodule = '.'.join([_get_module_name(namespace), name])
        if submodule in sys.modules:
            module = sys.modules[submodule]
        else:
            module = module_loader.find_module(submodule).load_module(submodule)
        namespace[name] = module

def _run_over_modules(namespace, runner):
    old_dir = os.getcwd()
    try:
        modules = _get_submodules(namespace)
        if not modules:
            # This is a hack to trick pkgutil into loading modules from site-packages
            os.chdir(_get_module_directory(namespace))
            modules = _get_submodules({'__name__': '.'})
        return runner(namespace, modules)
    finally:
        os.chdir(old_dir)

def set_all_submodules(namespace, filter_mods=None):
    all_assigner = lambda ns, mods: _assign_modules_names(filter_mods or _pass_through, ns, mods)
    return _run_over_modules(namespace, all_assigner)

def bind_all_submodules(namespace):
    _run_over_modules(namespace, _load_modules)
