<template>
<div class="flex-center-container dark-row">
    <div class="text-container">
        <h1 v-if="heading" class="text-center">{{ heading }}</h1>
        <slot></slot>
    </div>
</div>
</template>

<script>
export default {
    props: ['heading']
}
</script>

<style>
.color-block-row {
    background-color: gainsboro;
}

.color-block-row .row-content {
    background-color: white;
}
</style>
