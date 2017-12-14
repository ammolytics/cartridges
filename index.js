module.exports = {

  get names() {
    return require('./data/cartridges.json');
  },

  pistol: {
    get cip() {
      return require('./data/pistol/cip.json');
    },
    get nato() {
      return require('./data/pistol/nato.json');
    },
    get proprietary() {
      return require('./data/pistol/proprietary.json');
    },
    get saami() {
      return require('./data/pistol/saami.json');
    }
  },

  rifle: {
    get cip() {
      return require('./data/rifle/cip.json');
    },
    get nato() {
      return require('./data/rifle/nato.json');
    },
    get proprietary() {
      return require('./data/rifle/proprietary.json');
    },
    get saami() {
      return require('./data/rifle/saami.json');
    }
  },

  rimfire: {
    get cip() {
      return require('./data/rimfire/cip.json');
    },
    get nato() {
      return require('./data/rimfire/nato.json');
    },
    get proprietary() {
      return require('./data/rimfire/proprietary.json');
    },
    get saami() {
      return require('./data/rimfire/saami.json');
    }
  },

  shotshell: {
    get cip() {
      return require('./data/shotshell/cip.json');
    },
    get nato() {
      return require('./data/shotshell/nato.json');
    },
    get proprietary() {
      return require('./data/shotshell/proprietary.json');
    },
    get saami() {
      return require('./data/shotshell/saami.json');
    }
  }
};
