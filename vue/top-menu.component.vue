<template>
    <div class="flex-center-container top-menu dark-row">
        <ul>
            <li><a href="#">När Var Hur</a></li>
            <li><a href="#">Gäster</a></li>
            <li><a href="#">Galleri</a></li>
            <li><a href="#">Kontakt</a></li>
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