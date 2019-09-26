<template>
    <div class="">
        <h3 :class="{'required': required}">{{ title }}</h3>
        <div class="radio-input" v-for="(val, key, index) in contentObject" v-bind:key="key">
            <input type="radio" :name="name" :id="name + index" :value="val.value" v-model="selected" v-on:change="$emit('change', selected)">
            <label :for="name + index">{{ val.name }}</label>
        </div>
    </div>
</template>

<script>
export default {
    props: [ 'title', 'contentObject', 'data', 'name', 'required' ],
    model: {
        prop: 'data',
        event: 'change'
    },
    data: function() {
        return {
            selected: undefined
        }
    },
}
</script>

<style scoped>
    .radio-input {
        display: inline-block;
        margin-right: 15px;
    }
</style>