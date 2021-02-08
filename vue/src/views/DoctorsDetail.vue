<template>

  <div>

            <div class="row">

                <div class="col">

                  <img v-bind:src="doctor.img" width="500"/>

                </div>
                <div class="col" >


                        <h1 class="text-center">
                            {{ doctor.name }}
                        </h1>

                <br>
                  <br>
                    <br>
                    <div class="row-cols-lg-6 row-cols-md-6 row-cols-sm-6">
                        <h3>Методы:</h3>
                        <br>
                        <br>
                    </div>
                    <div class="row">
                         <div v-for="method in doctor.methods"
                             :key="method.id">
                              <div class="col-md-12">
                                  {{method.method}}
                              </div>
                        </div>
                    </div>

                </div>
            </div>
  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "DoctorsDetail",
  data () {
    return {
      doctorId: this.$route.params.id,
      doctor: {}
    }
  },
  mounted () {
    axios.get('http://127.0.0.1:8000/doctors/' + this.doctorId)
      .then(response => {
        this.doctor = response.data
      })
  }
}
</script>

<style scoped>

</style>
