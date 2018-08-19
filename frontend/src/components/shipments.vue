<template>
  <div class>
    <button v-on:click='get_shipments' class="btn btn-basic">show shipments</button>
     <table class="table">
        <tr>
          <th> tracking_no </th>
          <th> product </th>
          <th> shipping date </th>
          <th> delivery date </th>
          <th> status </th>

        </tr>
        <tr v-for="shipment in shipments">
          <td>{{shipment.tracking_no}}</td>
          <td>{{shipment.product}}</td>
          <td>{{shipment.shipping_date}}</td>
          <td>{{shipment.delivery_date}}</td>
          <td>{{shipment.status}}</td>
        </tr>
    </table> 
  </div>
</template>

<script>
export default {
  name: 'shipments',
  data () {
    return {
      shipments: ''
    }
  },
  methods: {
    get_shipments: function(){
      this.$http.get('http://localhost:8000/api/v2/shipments/').then(response => {
      this.shipments = response.body
      })
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
