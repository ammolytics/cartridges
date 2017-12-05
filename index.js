_cache = {};


function _cache_get(key) {
  if (_cache[key] === undefined) {
    _cache[key] = require(key);
  }
  return _cache[key];
}


module.exports = {

  get names() {
    return _cache_get('./cartridges.json');
  },

  pistol: {
    get saami() {
      return _cache_get('./pistol/saami.json');
    }
  },

  rifle: {
    get saami() {
      return _cache_get('./rifle/saami.json');
    }
  },

  rimfire: {
    get saami() {
      return _cache_get('./rimfire/saami.json');
    }
  },

  shotshell: {
    get saami() {
      return _cache_get('./shotshell/saami.json');
    }
  }
};
