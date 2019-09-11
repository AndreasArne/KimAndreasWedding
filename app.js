import Vue from 'vue'
import TopMenu from './vue/top-menu.component.vue'
import KimAndreasImage from './vue/kim-andreas-image.component.vue'
import Invitation from './vue/invitation.component.vue'
import Us from './vue/us.component.vue'

const app = new Vue({ 
    el: '#app',
    components: {
        'top-menu': TopMenu,
        'kim-andreas-image': KimAndreasImage,
        'invitation': Invitation,
        'us': Us
    }
})