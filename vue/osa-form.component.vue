<template>
    <form class="text-center">
        <radio-group :title="attendance.text" :contentObject="attendance.values"></radio-group>
        <radio-group v-for="checkbox in checkboxes" v-bind:key="checkbox" :title="checkbox.text" :contentObject="checkbox.values"></radio-group>
        <h3>Har du några allergier?</h3>
        <label for="allergies">Allergier</label>
        <input type="text" name="allergies" id="allergies">
    </form>
</template>

<script>
import RadioGroup from './radioGroup.component.vue'

export default {
    data: function() {
        return {
            checkboxes: checkboxes,
            attendance: {
                text: 'Kommer du på bröllopet?',
                values: { 'attending': 'Ja, jag kommer', 'notAttending': 'Nej, jag kommer inte' }
            },
            allergies: {
                text: 'Har du några allergier',
                values: { 'allergies': 'Allergier' }
            }
        }
    },
    components: {
        'radioGroup': RadioGroup
    }
}

const checkboxes = {
    food: {
        text: 'Vad vill du äta?', 
        values: { 'meat': 'Kött', 'fish': 'Fisk', 'veg': 'Vegetariskt' }
    },
    alcohol: {
        text: 'Vill du ha dryck med eller utan alkohol',
        values: { 'alcohol': 'Ja, jag vill ha alkohol', 'notAlcohol': 'Nej, jag vill inte ha alkohol' }
    }
}
</script>