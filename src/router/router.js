const mainRoutes = [
  {
    path: '/',
    name: 'redirect',
    component: () => import('../views/HomePageView.vue'),
    meta: { requireAuth: true }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/LoginPageView.vue'),
    meta: { requireAuth: true }
  },
  {
    path: '/addregion',
    name: 'addregion',
    component: () => import('../views/AddRegionView.vue'),
    meta: { requireAuth: true }
  },
  {
    path: '/switchregion',
    name: 'switchregion',
    component: () => import('../views/SwitchRegionView.vue'),
    meta: { requireAuth: true }
  },
  {
    path: '/adddevice',
    name: 'adddevice',
    component: () => import('../views/AddDeviceView.vue'),
    meta: { requireAuth: true }
  },
  {
    path: '/viewdevice',
    name: 'viewdevice',
    component: () => import('../views/ViewDeviceView.vue'),
    meta: { requireAuth: true }
  },
  {
    path: '/404',
    name: '404',
    component: () => import('../views/PageNotFound404.vue'),
    hidden: true,
    meta: { requireAuth: true }
  },
  {
    path: '/:pathMatch(.*)',
    redirect: '/404',
    hidden: true
  }
]


const routes = [
  {
    name: 'layout',
    path: '/',
    component: () => import('../layouts/PageView.vue'),
    children: mainRoutes
  },
]

export default routes