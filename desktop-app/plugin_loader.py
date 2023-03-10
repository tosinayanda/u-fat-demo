import importlib.util
import os


"""
MIT License

Copyright (c) 2023 OluwaTosin Ayanda

Please share comments and questions at:
    https://github.com/PythonForensics/PythonForensicsCookbook
    or email ayandaoluwatosin@gmail.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

__authors__ = ["OluwaTosin Ayanda"]
__date__ = 20230310
__description__ = "Load Plugins and Modules Application"

# Define the directory where the modules and plugins are located
MODULES_DIR = 'modules'
COMPONENTS_DIR = 'components'
PLUGINS_DIR = 'plugins'

def __load_components_and_plugins__():
    # Define the module names and plugin names
    MODULES = []
    PLUGINS = []
    COMPONENTS=[]

    # Load the modules dynamically
    for module_name in MODULES:
        module_path = os.path.join(MODULES_DIR, f"{module_name}.py")
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Call a function from the module
        module.say_hello()

    # Load the plugins dynamically
    for plugin_name in PLUGINS:
        plugin_path = os.path.join(PLUGINS_DIR, f"{plugin_name}.py")
        spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
        plugin = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(plugin)

        # Call a function from the plugin
        plugin.run_plugin()

    return MODULES, PLUGINS , COMPONENTS