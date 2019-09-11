<template>
<div class="flex-center-container color-block-row">
    <div class="text-container row-content">
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

<style scoped>
.color-block-row {
    background-color: gainsboro;
    margin-bottom: 15px;
}

.color-block-row .row-content {
    background-color: white;
}
</style>
