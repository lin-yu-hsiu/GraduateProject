// const mainRoutes = [
// {
//   path: '/',
//   name: 'redirect',
//   redirect: '/home',
//   meta: { requireAuth: true }
// },
// {
//   path: '/login',
//   name: 'login',
//   component: () => import('../views/LoginPage.vue'),
//   meta: { requireAuth: true }
// },
// {
//   path: '/edit-person/:personId',
//   name: 'editPerson',
//   component: () => import('../views/EditPersonView.vue'),
//   meta: { requireAuth: true }
// },
// {
//   path: '/404',
//   name: '404',
//   component: () => import('../views/PageNotFound404.vue'),
//   hidden: true,
//   meta: { requireAuth: true }
// },
// {
//   path: '/:pathMatch(.*)',
//   redirect: '/404',
//   hidden: true
// }
// ]


const routes = [
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginPage.vue'),
  },
  {
    name: 'layout',
    path: '/',
    component: () => import('../layouts/PageView.vue'),
    // children: mainRoutes
  },
]

export default routes