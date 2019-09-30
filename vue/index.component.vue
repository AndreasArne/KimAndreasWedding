<template>
<div>
    <top-menu></top-menu>
    <div class="flex-center-container content-row">
        <img class="kim-andreas-branch"
                src="../assets/branchWithNames.png"
                alt="Kim & Andreas 2020">
    </div>
    <color-block-row id="invitation" heading="Välkommen till vårt bröllop">
        <div class="two-part-list">
            <div class="left">
                <h2>Vigseln</h2>
                <p>Vigseln äger rum 16.45 på trappan utanför Verket i Avesta</p>
                <h2>Festen</h2>
                <p>Efter vigseln samlas vi inne på verket för att fira! Vi bjuder på mat och dryck.</p>
            </div>
            <div class="right">
                <h2>Klädkod</h2>
                <p>Mörk kostym</p>
                <h2>Boende</h2>
                <p>Vi har bokat en pool av rum för er som reser långväga. Hotellet vi har valt är Best Western Nya Star Hotel, och även vi kommer att sova där från fredag till söndag.</p>
                <h2>OSA</h2>
                <p>OSA senast den *DATUM HÄR*. OSA eller se din anmälan <a href="./osa">här</a></p>
            </div>
        </div>
        <div class="flex-center-container content-row">
            <p>Mer information om bröllopet finns <a href="#our-wedding">här</a></p>
        </div>
        <div class="flex-center-container">
            <img class="kimAndreasGif" src="../assets/kimAndreasLarge.gif">
        </div>
    </color-block-row>
    <div class="flex-center-container image-row">
        <img class="wide-image"
            src="../assets/us.png"
            alt="Vi">
    </div>
    <color-block-row id="us" heading="Oss">
        <p>Förhoppningsvis känner ni oss, eller i alla fall en av oss, men här är lite mer info om oss. Alltså vi som gifter oss!</p>
        <div class="two-part-list">
            <div class="left">
                <h2 class="text-center">Kim</h2>
                Massa info
            </div>
            <div class="right">
                <h2 class="text-center">Andreas</h2>
                massa info
            </div>
        </div>
        <h2 class="text-center">Vi</h2>
        <p>Andreas ville plugga. Han skulle plugga till ett jobb där han kunde tjäna så mycket pengar som möjligt, men jobba så lite som möjligt.
            Han valde Software Engineering-utbildningen på BTH, Blekinge tekniska högskola, i Karlskrona.
            Kim ville bli optiker, men ångrade sig, och ville ha ett jobb där man fick skapa och vara lite kreativ. Gärna inom IT.
            Hon valde Civilingenjör inom data- och medieteknik. Ja, hon ångrade sig och bytte, även hon till Software Engineering.
        </p>
    </color-block-row>
    <light-row id="our-wedding" heading="Bröllop i detalj">
        <h2 class="text-center">Vigseln</h2>
        <p>Vigseln kommer att hållas 17.45 på trappan utanför verket.
            Förhoppningen är att vi ska kunna ha vigseln utomhus, så packa med varma ytterkläder!
            Vigseln kommer att vara en borgerlig vigsel som kommer ta cirka 15 minuter.
            Innan vigseln samlas ni, minglar lite och vi bjuder på varm choklad.
        </p>
        <h2 class="text-center">Festen</h2>
        <p>Efter vigseln samlas vi alla och minglar inne på verket, för att sedan fortsätta till middagen.
            Det serveras tre rätter där ni får välja kött, fisk eller vegetariskt. Ni får även välja om ni vill ha alkohol eller ej.
            Medtag av egen alkohol är okej om man vill!
            Efter middagen firar och festar vi järnet.
        </p>
        <h2 class="text-center">Platsen</h2>
        <p>Lokalen där vi kommer att hålla till är fantastiska verket i Avesta.
            Berätta mer om verket osv.
        </p>
        <h2 class="text-center">Sociala medier</h2>
        <p>Ni får jättegärna fota och dela bilder på sociala medier.
            Tagga gärna oss i bilderna, och om ni lägger ut bilderna på instagram kan ni använda får hashtag: #kimandreasawesomeness2020
        </p>
    </light-row>
    <color-block-row heading="Gäster">
        <p class="text-center">Här visar vi er gäster som kommer på bröllopet, allt eftersom att ni anmält er.</p>
        <div class="two-part-list">
            <div class="left">
                <h3 class="text-center">Familj</h3>
                <div class="flex-center-container">
                    <ul>
                        <li>Namn</li>
                        <li>Namn</li>
                    </ul>
                </div>
            </div>
            <div class="right">
                <h3 class="text-center">Vänner</h3>
                <div class="flex-center-container">
                    <ul>
                        <li>Namn</li>
                        <li>Namn</li>
                    </ul>
                </div>
            </div>
        </div>
    </color-block-row>
    <light-row id="wishlist" heading="Önskelista">
        <div class="flex-center-container">
            <p>Spreadsheet här</p>
            <ul>
                <li>Sponsra gärna vår bröllopsresa</li>
                <li>Kolla på cervera</li>
                <li>...</li>
            </ul>
        </div>
    </light-row>
    <color-block-row id="hotel" heading="Hotellet">
        <p>Här skriver vi en massa om boendet, vart det är, vart man bokas osv</p>
        <p>Boka rum med koden på er inbjudan på deras hemsida <a href="https://www.nyastarhotel.com/">här</a> eller på telefon: 0226-56000</p>
    </color-block-row>
    <dark-row id="contact" heading="Kontakta oss">
        <p class="text-center">Om du har några frågor kan du kontakta oss:</p>
        <div class="two-part-list">
            <div class="left text-center">
                <p>Kim Svensson Sand<br>
                    Tel: Telefonnummer här<br>
                    Email: Email här
                </p>
            </div>
            <div class="right text-center">
                <p>Andreas Arnesson<br>
                    Tel: Telefonnummer här <br>
                    Email: Email här
                </p>
            </div>
        </div>
    </dark-row>
</div>
</template>

<script>
import TopMenu from './top-menu.component.vue'
import ColorBlockRow from './color-block-row.component.vue'
import DarkRow from './dark-row.component.vue'
import LightRow from './light-row.component.vue'

export default {
    components: {
        'top-menu': TopMenu,
        'colorBlockRow': ColorBlockRow,
        'darkRow': DarkRow,
        'lightRow': LightRow
    }
}
</script>

<style scoped>
    .kimAndreasGif {
        width: 256px;
    }
</style>