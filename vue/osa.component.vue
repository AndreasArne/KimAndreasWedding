<template>
    <dark-row>
        <div v-if="!party">
            <form class="" v-if="!party">
                <h1 class="text-center">Skriv in din kod</h1>
                <p class="text-center">Koden hittar du på ditt inbjudningskort.</p>
                <div class="text-center">
                    <label for="hash">Kod:</label>
                    <input v-model="hash" type="text" name="hash" id="hash">
                </div>
            </form>
            <div class="text-center">
                <button class="button" type="button" v-on:click="submitHash(hash)">Ok</button>
                <button class="button">Avbryt</button>
            </div>
        </div>
        <div v-if="party">
            <form class="text-center">
                <h1>Hej {{ guestNames }}!</h1>
                <div v-for="guest in party.guests" v-bind:key="guest.name" class="text-center guest-form">
                    <h2>{{ guest.name }}</h2>
                    <radio-group :title="coming.text" :contentObject="coming.values" v-model="guest.coming"></radio-group>
                    <radio-group v-for="(checkbox, key) in checkboxes" v-bind:key="checkbox.text" :title="checkbox.text" :contentObject="checkbox.values" v-model="guest[key]"></radio-group>
                    <h3>Har du några allergier?</h3>
                    <label for="allergies">Allergier:</label>
                    <input type="text" name="allergy" id="allergy" v-model="guest.allergy">
                </div>
            </form>
            <div class="text-center">
                <button class="button" v-on:click="register">Anmäl</button>
                <button class="button">Avbryt</button>
            </div>
        </div>
    </dark-row>
</template>

<script>
import DarkRow from './dark-row.component.vue'
import GuestsService from '../services/guests-service.js'
import RadioGroup from './radioGroup.component.vue'

export default {
    data: function() {
        return {
            party: undefined,
            hash: undefined,
            guestsService: new GuestsService(),
            checkboxes: checkboxes,
            coming: {
                text: 'Kommer du på bröllopet?',
                values: { 'attending': { name: 'Ja, jag kommer', value: true }, 'notAttending': { name: 'Nej, jag kommer inte', value: false} }
            },
        }
    },
    methods: {
        submitHash: function(hash) {
            this.getGuests(hash);
        },
        getGuests: function(hash) {
            return this.guestsService.getMockGuests(hash).then((response) => {
                this.party = response;
                this.guestNames = this.party.guests.map((guest) => guest.name).join(', ')
            }).catch((err) => {
                console.log(err)
            })
        },
        register: function() {
            console.log(this.party.guests);
        }
    },
    components: {
        'darkRow': DarkRow,
        'radioGroup': RadioGroup,
    }
}

const checkboxes = {
    food: {
        text: 'Vad vill du äta?', 
        values: { 'meat': { name: 'Kött', value: 'meat' }, 'fish': { name: 'Fisk', value: 'fish' }, 'veg': { name: 'Vegetariskt', value: 'veg'} }
    },
    drink: {
        text: 'Vill du ha dryck med eller utan alkohol',
        values: { 'alcohol': { name: 'Ja, jag vill ha alkohol', value: true }, 'notAlcohol': { name: 'Nej, jag vill inte ha alkohol', value: false } }
    }
}
</script>

<style scoped>
    button {
        background: none;
        border-bottom: none;
        border-top: none;
        border-left: solid white 15px;
        border-right: solid white 15px;
        padding: 10px 20px;
        margin: 30px 15px 0 15px;
        color: white;
        font-family: 'Nanum Myeongjo', serif;
        font-size: 1rem;
    }

    button:hover {
        background-color: white;
        color: black;
    }

    input {
        padding: 10px;
        margin: 15px;
        border: solid gainsboro 1px;
    }

    .guest-form {
        margin-top: 50px;
    }
</style>