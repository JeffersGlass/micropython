import('../../build/micropython.mjs').then(mp=>{
mp.loadMicroPython({url:"../../build/micropython.wasm"}).then(py=>{
    py.runPython("import sys");
    py.runPython("print(sys.modules)");
    py.runPython("import mip");
    py.runPython("mip.install(keyword)); import keyword");
    py.runPython("print(keyword.kwlist")
});
});
