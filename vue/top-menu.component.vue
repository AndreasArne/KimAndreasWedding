<template>
    <div class="flex-center-container top-menu dark-row">
        <ul>
            <li><a href="#invitation">Inbjudan</a></li>
            <li><a href="#us">Oss</a></li>
            <li><a href="#our-wedding">Vårt bröllop</a></li>
            <li><a href="#wishlist">Önskelistan</a></li>
            <li><a href="#hotel">Hotellet</a></li>
            <li><a href="#contact">Kontakta oss</a></li>
        </ul>
    </div>
</template>

<script type="text/javascript">
    import DarkRow from './dark-row.component.vue'

    export default {
        components: {
            'darkRow': DarkRow
        }
    }
</script>

<style scoped>
    .top-menu {
        padding: 15px;
    }

    ul {
        list-style-type: none;
        margin: 0;
        padding: 5px;
    }
    li {
        display: inline-block;
        margin: 0 2rem;
    }
    a {
        color: white;
        font-size: larger;
    }
</style>