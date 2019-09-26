import Vue from 'vue'
import Index from './vue/index.component.vue'
import OSA from './vue/osa.component.vue'
import Registered from './vue/registered.component.vue'

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