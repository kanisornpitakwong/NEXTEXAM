<template>
    <div class="card-area">
        <h1>xxx</h1>
        <div v-for="data in datas" :key="data.id" class="col-sm-6 col-lg-3">
            <div class="card">
                <div clsss="card-body">
                    <h1 class="title"> {{ data.sub_name }} </h1>
                    <h3> {{ data.sub_id }} </h3>
                    <h3> {{ data.sub_teacher }} </h3>
                    <h3> {{ data.sub_start }} </h3>
                    <h3> {{ data.sub_stop }} </h3>
                </div>
            </div>
        </div>
        <div class="col-sm-6 col-lg-3"> 
            <a href="create">
                <div class="card">
                    <div class="card-body">
                        <h1 class ="title">
                            Create Subject 
                        </h1>
                    </div>
                </div>
            </a>
        </div>
    </div>
        

</template>

<script>
import axios from 'axios'
export default {
    layouts:'header',
    async asyncData(){
        const { data } = await axios.get(
            'http://127.0.0.1:8000/ShowSubject'
        )
        return { datas : data}
    }
}
</script>

<style>
.card {
    background-color: white;
    margin-bottom: 30px;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    height: 10em;
}
.card-body {
    padding: 0 14px 12px;
}
@media (min-width: 768px){
    .col-sm-6 {
        float: left;
        width: 50%;
        position: relative;
        min-height: 1px;
        padding-right: 15px;
        padding-left: 15px;
    }
}
.col-lg-3{
    position: relative;
    min-height: 1px;
    padding-right: 15px;
    padding-left: 15px;
}
@media (min-width: 1200px){
    .col-lg-3 {
        float: left;
        width: 25%;
    }
}
.title{
    text-align: center;
    font-size: 1em;
}
.card-area{
    padding: 0 15em 0 15em;
}


</style>