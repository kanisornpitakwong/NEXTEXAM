<template>
    <div>
        <form method = "POST">
            <v-text-field v-model="teacher_name" name="teacher_name" label="teacher name"  hide-details="auto" ></v-text-field>
            <v-text-field v-model="created_by" name="created_by" label="subject name"  hide-details="auto" ></v-text-field>
            <v-text-field v-model="subject_name" name="subject_name" label="teacher name"  hide-details="auto" ></v-text-field>
            <v-text-field v-model="subject_id" name="subject_id" label="subject id"  hide-details="auto" ></v-text-field>
            <v-text-field v-model="start_time" name="start_time" label="start time"  hide-details="auto" ></v-text-field>
            <v-text-field v-model="end_time" name="end_time" label="stop time"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="easy" name="easy" label="easy"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="medium" name="medium" label="medium"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="hard" name="hard" label="hard"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="backward" name="backward" label="backward"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="scoring_method" name="scoring_method" label="scoring method"  hide-details="auto" ></v-text-field>
            <v-text-field type="number" v-model="show_score" name="show_score" label="show score"  hide-details="auto" ></v-text-field>
            <v-btn style="margin-top:1em" @click="postSubmit()"> Save </v-btn>
        </form>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    layout:'header',
    data() {
        return {
            teacher_name:'',
            created_by:'',
            subject_name:'',
            subject_id:'',
            start_time:'',
            end_time:'',
            easy:0,
            medium:0,
            hard:0,
            backward:0,
            scoring_method:0,
            show_score:0
        }
    },
    methods: {
        async postSubmit() {
            await axios.post('http://127.0.0.1:8000/InsertSubject' ,{
            teacher_name:this.teacher_name,
            created_by:this.created_by,
            subject_name:this.subject_name,
            subject_id:this.subject_id,
            start_time:this.start_time,
            end_time:this.end_time,
            easy:this.easy,
            medium:this.medium,
            hard:this.hard,
            backward:this.backward,
            scoring_method:this.scoring_method,
            show_score:this.show_score
            })
            .then((res) => console.log(res.data))
            .catch((err) => console.log(err))
            console.log('posted')
        }
    }
}
</script>       

<style>

</style>