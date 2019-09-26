<template>
    <dark-row class="text-center">
        <h1 v-if="notRegistered">Något blev fel, så du är ännu inte anmäld!</h1>
        <h1 v-else-if="!coming">Tack för din avanmälan!</h1>
        <div v-else>
            <h1>Tack för din anmälan!</h1>
            <div class="guest-form" v-for="guest in party.guests" v-bind:key="guest.name">
                <h2>{{ guest.name }}</h2>
                <h3>{{ texts.osaForm.coming.heading }}</h3>
                <p>{{ texts.osaForm.coming.answer[guest.coming] }}</p>
                <h3>{{ texts.osaForm.food.heading }}</h3>
                <p>{{ texts.osaForm.food.answer[guest.food] }}</p>
                <h3>{{ texts.osaForm.drink.heading }}</h3>
                <p>{{ texts.osaForm.drink.answer[guest.drink] }}</p>
                <h3>{{ texts.osaForm.allergy.heading }}</h3>
                <p>{{ guest.allergy || "Ingen" }}</p>
            </div>
        </div>
    </dark-row>
</template>

<script>
import GuestsService from '../services/guests-service.js'
import ObjectUtils from '../utils/objectUtils.js'
import DarkRow from '../vue/dark-row.component.vue'
import texts from '../texts.js'

const guestsService = new GuestsService()
const urlParams = new URLSearchParams(window.location.search)
const hash = urlParams.get('hash')
const objectUtils = new ObjectUtils();

export default {
    data: function() {
        return {
            party: Object,
            texts: texts
        }
    },
    components: {
        'darkRow': DarkRow
    },
    created: function() {
        guestsService.getParty(hash).then((response) => {
            this.party = response;
        }).catch((err) => {
            console.log(err)
        })
    },
    computed: {
        coming: function() {
            return (objectUtils.getNested(this, ['party', 'guests']) || []).some((guest) => guest.coming === true);
        },
        notRegistered: function() {
            return (objectUtils.getNested(this, ['party', 'guests']) || []).some((guest) => guest.coming === null);
        }
    }
}
</script>