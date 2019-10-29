<template>
    <dark-row>
        <div v-if="!party">
            <form v-if="!party" novalidate @submit.prevent="submitHash(hash)">
                <h1 class="text-center">{{ texts.osaForm.hash.heading }}</h1>
                <p class="text-center">{{ texts.osaForm.hash.help }}</p>
                <p class="text-center error" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                <div class="text-center">
                    <label for="hash">Kod:</label>
                    <input v-model="hash" type="text" name="hash" id="hash">
                </div>
            </form>
            <div class="text-center">
                <button class="submit" type="button" v-on:click="submitHash(hash)">Ok</button>
                <button class="button" v-on:click="cancel">Avbryt</button>
            </div>
        </div>
        <div v-if="party">
            <form class="text-center" novalidate @submit.prevent="register">
                <h1>Hej {{ guestNames }}!</h1>
                <div v-for="(guest, index) in party.guests" v-bind:key="guest.name" class="text-center guest-form">
                    <h2>{{ guest.name }}</h2>
                    <radio-group :title="coming.text"
                        :contentObject="coming.values"
                        :required="true"
                        :name="'coming' + index"
                        v-model="guest.coming"></radio-group>
                    <div v-if="guest.coming !== false">
                        <radio-group 
                        v-for="(checkbox, key) in checkboxes"
                        v-bind:key="checkbox.text"
                        required="true"
                        :title="checkbox.text"
                        :name="key + index"
                        :contentObject="checkbox.values" v-model="guest[key]"></radio-group>
                        <h3>{{ texts.osaForm.allergy.heading }}</h3>
                        <label for="allergies">Allergier:</label>
                        <input type="text" name="allergy" id="allergy" v-model="guest.allergy">
                        <div class="air" v-if="index < party.guests.length - 1"></div> 
                    </div>
                </div>
            </form>
            <div class="text-center">
                <p class="error" v-for="error in errors" v-bind:key="error">{{ error }}</p>
                <button class="submit" v-on:click="register">Anmäl</button>
                <button class="button" v-on:click="cancel">Avbryt</button>
            </div>
        </div>
    </dark-row>
</template>

<script>
import DarkRow from './dark-row.component.vue'
import GuestsService from '../services/guests-service.js'
import RadioGroup from './radioGroup.component.vue'
import texts from '../texts.js'

export default {
    data: function() {
        return {
            party: undefined,
            hash: undefined,
            guestsService: new GuestsService(),
            checkboxes: checkboxes,
            coming: {
                text: texts.osaForm.coming.heading,
                values: { 'attending': { name: texts.osaForm.coming.answer[true], value: true },
                    'notAttending': { name: texts.osaForm.coming.answer[false], value: false} }
            },
            errors: [],
            texts: texts
        }
    },
    methods: {
        submitHash: function(hash) {
            this.errors = [];
            if (hash && hash.length === 10) {
                this.getParty(hash);
            } else {
                this.errors.push('Koden är inte korrekt')
            }
        },
        getParty: function(hash) {
            return this.guestsService.getParty(hash).then((response) => {
                this.party = response;
                if (this.party.osa) {
                    window.location.href = '../registered?hash=' + hash + '&earlier=true'
                    return 
                }

                this.guestNames = this.party.guests.map((guest) => { 
                    guest.allergy = ""
                    return guest.name }).join(', ')
            }).catch((err) => {
                this.errors.push('Koden är inte korrekt')
            })
        },
        register: function() {
            this.errors = [];
            if (validateParty(this.party)) {
                this.guestsService.putParty(this.party).then((response) => {
                    window.location.href = '../registered?hash=' + this.hash + '&earlier=false'
                }).catch(() => {
                    this.errors.push('Något gick fel. Försök igen eller kontakta Kim och Andreas')
                });
            } else {
                this.errors.push('Du måste fylla i alla fält')
            }
        },
        cancel: function() {
            window.location.href = '../'
        },
        validateGuest: function(guest) {
            return validateGuest(guest)
        }
    },
    components: {
        'darkRow': DarkRow,
        'radioGroup': RadioGroup,
    }
}

function validateParty(party) {
    return party.guests.every(guest => validateGuest(guest))
}

function validateGuest(guest) {
    return guest.coming === false || !Object.values(guest).some(value => value === null || value === undefined)
}

const checkboxes = {
    food: {
        text: texts.osaForm.food.heading, 
        values: { 'meat': { name: texts.osaForm.food.answer.meat, value: 'meat' },
            'fish': { name: texts.osaForm.food.answer.fish, value: 'fish' },
            'veg': { name: texts.osaForm.food.answer.veg, value: 'veg'} }
    },
    drink: {
        text: texts.osaForm.drink.heading,
        values: { 'alcohol': { name: texts.osaForm.drink.answer[true], value: true },
            'notAlcohol': { name: texts.osaForm.drink.answer[false], value: false } }
    }
}
</script>

<style>
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

    input[type="text"] {
        padding: 10px;
        border: solid gainsboro 1px;
    }

    input[type="radio"]:hover + label {
        border-bottom: 1px solid white;
    }

    .guest-form {
        margin-bottom: 25px;
        margin-top: 25px;
    }

    .guest-form:not(:last-child) {
        margin-bottom: 50px;
    }

    .error {
        color: red;
    }

    .required::after {
        content: "*"
    }
</style>