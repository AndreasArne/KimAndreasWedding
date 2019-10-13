<template>
    <dark-row class="text-center">
        <div v-if="notFound">
            <h1>Något fick fel!</h1>
            <p>Kontakta <a href="../#contact">Kim och Andreas</a></p>
        </div>
        <div v-else-if="notRegistered">
            <h1 v-if="notRegistered">Något blev fel, så du är ännu inte anmäld!</h1>
            <p>Kontakta <a href="../#contact">Kim och Andreas</a></p>
        </div>
        <div v-else>
            <div v-if="alreadyRegistered">
                <h1>Du har redan svarat!</h1>
                <p>Här kan du se dina svar:</p>
            </div>
            <h1 v-else>Tack för ditt svar!</h1>
            <div v-if="coming">
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
            <h2 v-else>Du har svarat att du inte kommer.</h2>
            <p>Är det något som inte stämmer? Kontakta <a href="../#contact">Kim och Andreas</a></p>
        </div>
        <button class="button" v-on:click="home">Tillbaka till startsidan</button>
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
const earlier = urlParams.get('earlier')
const objectUtils = new ObjectUtils();

export default {
    data: function() {
        return {
            party: Object,
            texts: texts,
            alreadyRegistered: earlier === "true",
            notFound: false
        }
    },
    components: {
        'darkRow': DarkRow
    },
    created: function() {
        guestsService.getParty(hash).then((response) => {
            this.party = response;
        }).catch((err) => {
            this.notFound = true;
        })
    },
    methods: {
        home: function() {
            window.location.href = '../'
        }
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