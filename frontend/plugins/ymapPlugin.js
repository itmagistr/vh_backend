import Vue from 'vue'
import YmapPlugin from 'vue-yandex-maps'

const settings = {
    coords: [
      [55.734876, 37.59308], // Lva Tolstogo street
    ]
  };

Vue.use(YmapPlugin, settings);