<template>
    <dark-row heading="OSA">
        <form class="" v-if="!user">
            <div class="text-center">
                <label for="hash">Skriv in din kod</label>
                <input type="text" name="hash" id="hash">
            </div>
            <div class="text-center">
                <button type="button" v-on:click="submitHash">OSA</button>
            </div>
        </form>
        <h2 class="text-center">Hej {{ user }}!</h2>
        <osa-form></osa-form>
        <hr>
    </dark-row>
</template>

<script>
import DarkRow from './dark-row.component.vue'
import OsaForm from './osa-form.component.vue'

export default {
    data: function() {
        return {
            user: "Kimelim",
        }
    },
    methods: {
        submitHash: function () {
            this.user = "Kimelim"
        }
    },
    components: {
        'darkRow': DarkRow,
        'osaForm': OsaForm 
    }
}
</script>