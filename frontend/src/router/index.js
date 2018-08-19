import Vue from 'vue'
import Router from 'vue-router'
import shipments from '@/components/shipments'
import companies from '@/components/companies'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'shipments',
      component: shipments
    },
    {
      path: '/companies',
      name: 'companies',
      component: companies
    }
  ]
})
