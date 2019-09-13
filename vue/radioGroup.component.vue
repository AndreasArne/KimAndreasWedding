<template>
    <div class="">
        <h3>{{ title }}</h3>
        <div class="radio-input" v-for="(val, key, index) in contentObject" v-bind:key="key">
            <input type="radio" :name="key + index" :id="key + index" :value="val.value" v-model="selected" v-on:change="$emit('change', $event.target.value)">
            <label :for="key">{{ val.name }}</label>
        </div>
    </div>
</template>

<script>
export default {
    props: { title: String, contentObject: Object, data: String },
    model: {
        prop: 'data',
        event: 'change'
    },
    data: function() {
        return {
            selected: String
        }
    }
}
</script>

<style scoped>
    .radio-input {
        display: inline-block;
        margin-right: 15px;
    }
</style>