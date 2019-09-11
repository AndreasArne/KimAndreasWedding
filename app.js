import Vue from 'vue'
import TopMenu from './vue/top-menu.component.vue'
import ColorBlockRow from './vue/color-block-row.component.vue'
import DarkRow from './vue/dark-row.component.vue'
import LightRow from './vue/light-row.component.vue'

const app = new Vue({ 
    el: '#app',
    components: {
        'top-menu': TopMenu,
        'colorBlockRow': ColorBlockRow,
        'darkRow': DarkRow,
        'lightRow': LightRow
    }
})