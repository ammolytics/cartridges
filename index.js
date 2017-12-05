_cache = {};


function _cache_get(key) {
  if (_cache[key] === undefined) {
    _cache[key] = require(key);
  }
  return _cache[key];
}


module.exports = {

  get names() {
    return _cache_get('./data/cartridges.json');
  },

  pistol: {
    get cip() {
      return _cache_get('./data/pistol/cip.json');
    },
    get nato() {
      return _cache_get('./data/pistol/nato.json');
    },
    get proprietary() {
      return _cache_get('./data/pistol/proprietary.json');
    },
    get saami() {
      return _cache_get('./data/pistol/saami.json');
    }
  },

  rifle: {
    get cip() {
      return _cache_get('./data/rifle/cip.json');
    },
    get nato() {
      return _cache_get('./data/rifle/nato.json');
    },
    get proprietary() {
      return _cache_get('./data/rifle/proprietary.json');
    },
    get saami() {
      return _cache_get('./data/rifle/saami.json');
    }
  },

  rimfire: {
    get cip() {
      return _cache_get('./data/rimfire/cip.json');
    },
    get nato() {
      return _cache_get('./data/rimfire/nato.json');
    },
    get proprietary() {
      return _cache_get('./data/rimfire/proprietary.json');
    },
    get saami() {
      return _cache_get('./data/rimfire/saami.json');
    }
  },

  shotshell: {
    get cip() {
      return _cache_get('./data/shotshell/cip.json');
    },
    get nato() {
      return _cache_get('./data/shotshell/nato.json');
    },
    get proprietary() {
      return _cache_get('./data/shotshell/proprietary.json');
    },
    get saami() {
      return _cache_get('./data/shotshell/saami.json');
    }
  }
};
