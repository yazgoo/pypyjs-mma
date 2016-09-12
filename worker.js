importScripts( "./lib/Promise.min.js", "./lib/FunctionPromise.js", "./lib/pypyjs.js");
pypyjs.ready().then(function() {
    return pypyjs.execfile('mma-lib.py');
})
onmessage = function(e) {
  console.log('Message received from main script');
  pypyjs.execfile('mma.py').catch(function(e) {
      console.log(e);
      console.log(e.trace);
  }).then(function() {
      return pypyjs.get('midi');
  }).then(function(x) {
      console.log("midi is", x);
      postMessage(x);
  })
}
