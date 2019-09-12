<template>
    <div class="">
        <h3>{{ title }}</h3>
        <div class="radio-input" v-for="(value, key) in contentObject">
            <input type="radio" :name="key" :id="key">
            <label :for="key">{{ value }}</label>
        </div>
    </div>
</template>

<script>
export default {
    props: [ 'title', 'contentObject' ]
}
</script>

<style scoped>
    .radio-input {
        display: inline-block;
        margin-right: 15px;
    }
</style>