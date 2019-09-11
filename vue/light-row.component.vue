<template>
<div class="flex-center-container">
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

<style scoped>
</style>
