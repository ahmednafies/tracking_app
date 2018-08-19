<template>
  <div class>
    <button v-on:click='get_companies' class="btn btn-basic">companies</button>
     <table class="table">
        <tr>
          <th> ID </th>
          <th> Name </th>
          <th> Url </th>
          <th> Address </th>
        </tr>
        <tr v-for="company in companies">
          <td>{{company.id}}</td>
          <td>{{company.name}}</td>
          <td>{{company.url}}</td>
          <td>{{company.address}}</td>
        </tr>
    </table> 
  </div>
</template>

<script>
export default {
  name: 'companies',
  data () {
    return {
      companies: ''
    }
  },
  methods: {
    get_companies: function(){
      this.$http.get('http://localhost:8000/api/v2/companies/').then(response => {
      this.companies = response.body
      })
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
