<template>
<div>
    <div>
    <v-text-field v-model="sub_id" label="subject's id" :rules="rules" hide-details="auto" ></v-text-field>
    <v-text-field v-model="sub_name" label="subject's name" :rules="rules" hide-details="auto" ></v-text-field>
    <v-text-field v-model="sub_teacher" label="teacher" :rules="rules" hide-details="auto" ></v-text-field>
    <v-text-field v-model="sub_start" label="date start" :rules="rules" hide-details="auto" ></v-text-field>
    <v-text-field v-model="sub_stop" label="date stop" :rules="rules" hide-details="auto" ></v-text-field>
    <v-btn style="margin-top:1em" @click="postSubmit()"> Save </v-btn>
  </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    layout:'header',
    data() {
        return {
            sub_id:'',
            sub_name:'',
            sub_teacher:'',
            sub_start:null,
            sub_stop:null
        }
    },
    postSubmit() {
        axios.post('http://127.0.0.1:8000/InsertSubject', {
            sub_id:this.sub_id,
            sub_name:this.sub_name,
            sub_teacher:this.sub_teacher,
            sub_start:this.sub_start,
            sub_stop:this.sub_stop
        }).then(response => {})
    }
}
</script>       

<style>

</style>