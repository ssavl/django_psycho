<template>

  <div>

    <div class="container">

            <div v-for="doctor in doctorsList"
                 :key="doctor.id"
                 class="doctor-list">
                <div class="row">
                  <div class="col">
                      <img v-bind:src="doctor.img" width="500"/>
                  </div>
                  <div class="col">
                    <router-link :to="/doctor/ + doctor.id "><h1>{{ doctor.name }}</h1></router-link>
                  </div>
                </div><br>
            </div>

    </div>

  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "DoctorsList",
  data () {
    return {
      doctorsList: []
    }
  },
  mounted () {
    axios.get('http://127.0.0.1:8000/doctors/')
      .then(response => {
        console.log(response)
        this.doctorsList = response.data
      })
  }
}
</script>

<style scoped>

</style>
