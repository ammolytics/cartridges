var assert = require('assert');

exports['test require module'] = function() {
  assert.doesNotThrow(function() {
    require('../../index.js');
  }, 'Could not require module.');
}


exports['test top-level structure'] = function() {
  var cartridges = require('../../index.js');
  
  assert(cartridges.names !== undefined);
  assert(cartridges.pistol !== undefined);
  assert(cartridges.rifle !== undefined);
  assert(cartridges.rimfire !== undefined);
  assert(cartridges.shotshell !== undefined);
}


exports['test length of names'] = function() {
  var cartridges = require('../../index.js');

  assert(cartridges.names.pistol.length !== 0);
  assert(cartridges.names.rifle.length !== 0);
  assert(cartridges.names.rimfire.length !== 0);
  assert(cartridges.names.shotshell.length !== 0);
}


if (module == require.main) require('test').run(exports)
