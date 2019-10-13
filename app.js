import Vue from 'vue'
import Index from './vue/index.component.vue'
import OSA from './vue/osa.component.vue'
import Registered from './vue/registered.component.vue'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.use(VueGoogleMaps, {
    load: {
        key: "<API-KEY>",
        region: 'SV',
        language: 'sv',
    }
})

const NotFound = { template: '<p>Page not found</p>' }

const routes = {
    '/': Index,
    '/osa': OSA,
    '/registered': Registered
}

const app = new Vue({ 
    el: '#app',
    data: {
        currentRoute: window.location.pathname
    },
    computed: {
        ViewComponent () {
            return routes[this.currentRoute] || NotFound
        }
    },
    render (h) { return h(this.ViewComponent) }
})
