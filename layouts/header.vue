<template>
  <div>
    <v-app-bar dark>
        <img class="icon" src="~/assets/image/book_logo.png">
      <v-toolbar-title>NEXTEXAM</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn icon>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>
      </v-btn>
    </v-app-bar>
    <nuxt />
  </div>
</template>

<script>
import book from '~/assets/image/book_logo.png'
export default {
   components: {
    book
  }
}
</script>

<style >
.icon {
    width:2%;
    margin-right:1em;
}
</style>
