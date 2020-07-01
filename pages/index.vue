<template>
  <div class="main">
  <a href="/teacher/dashboard">
    <v-btn> Click Me </v-btn>
  </a>
  </div>
</template>

<script>
export default {
  layout:'header',
  methods: {
    refresh() {
      this.$fetch();
    }
  }
}
</script>
